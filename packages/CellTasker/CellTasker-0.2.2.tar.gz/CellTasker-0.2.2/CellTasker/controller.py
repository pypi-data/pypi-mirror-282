from pathlib import Path
import yaml
from time import sleep
from datetime import datetime, timedelta
from sys import argv
from .pub import TimeRange
import subprocess
import logging

log = logging.getLogger('CellTasker')
log.addHandler(logging.StreamHandler())


class Controller:
    def __init__(self, interval: int, register_path: Path | str) -> None:
        if not isinstance(interval, int):
            raise Exception('interval should be an integer')
        if isinstance(register_path, str):
            register_path = Path(register_path)
        if not register_path.exists() or not register_path.is_dir():
            raise Exception('register_path should be a directory')
        self.interval = interval
        self.register_path = register_path
        self.cell_configs = dict()
        self.time_task = dict()
        self.booting_time = dict()
        self.booting_times = dict()
        self.max_booting_times = 3

    @classmethod
    def check_cell_config(cls, cell_config):
        properties = ['name', 'timerange', 'interval', 'register_path', 'update_path', 'boot_cmd']
        for property in properties:
            if property not in cell_config:
                return False
        return True

    def collect_cells(self):
        for cell in self.register_path.iterdir():
            if cell.is_file():
                with open(cell, encoding='utf-8') as f:
                    cell_config = yaml.load(f, Loader=yaml.FullLoader)
                    if self.check_cell_config(cell_config):
                        self.cell_configs[cell_config['name']] = cell_config
                    else:
                        log.error(f'Invalid cell config file: {cell}, {cell_config}')
        log.info(f'registered {self.cell_configs}')

    def add_hook(self):
        for name, cell in self.cell_configs.items():
            timerange: TimeRange = cell['timerange']
            self.time_task.setdefault(timerange, []).append(name)

    def remove_hook(self, name):
        for timerange, names in self.time_task.items():
            if name in names:
                names.remove(name)
                log.debug(f'remove {name} from {timerange}')
                if len(names) == 0:
                    self.time_task.pop(timerange)
                break

    def is_cell_running(self, name):
        cell_config = self.cell_configs[name]
        update_file = Path(cell_config['update_path']) / f'{name}.txt'
        if not update_file.exists() or not update_file.is_file():
            return False
        read_times = 0
        while (read_times < 3):
            try:
                with open(update_file, encoding='utf-8') as f:
                    status, timestamp = f.readlines()
                    status = status.strip()
                    timestamp = timestamp.strip()
                break
            except Exception as e:
                read_times += 1
                log.error(f'for {read_times} times error reading {update_file}: {e}')
        updated_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        now = datetime.now()
        if now - updated_time > timedelta(seconds=cell_config['interval']+10):
            return False
        self.booting_time.pop(name, None)
        return True

    def start_cell(self, name):
        self.booting_times.setdefault(name, 1)

        if self.is_cell_running(name):
            log.debug(f'{name} is running, skip')
            self.booting_times[name] = 0
            return True

        cell_config = self.cell_configs[name]
        delta = timedelta(seconds=3*cell_config['interval'])
        if name in self.booting_time \
                and datetime.now() - self.booting_time[name] < delta:
            log.debug(f'{name} is booting, skip')
            return True

        if self.booting_times[name] > self.max_booting_times:
            log.debug(f'{name} has been booting {self.max_booting_times} times, skip')
            return False

        boot_cmd = cell_config['boot_cmd']
        log.info(f'starting [{name}] with [{boot_cmd}]')
        try:
            subprocess.Popen(boot_cmd, shell=True)
        except Exception as e:
            log.error(f'Error starting [{name}]: {e}')
        self.booting_times[name] += 1
        self.booting_time[name] = datetime.now()
        return True

    def run(self):
        while True:
            to_be_removed = []
            for timerange, names in self.time_task.items():
                timerange = TimeRange.from_str(timerange)
                if datetime.now() in timerange:
                    for name in names:
                        ok = self.start_cell(name)
                        if not ok:
                            to_be_removed.append(name)
            for name in to_be_removed:
                self.remove_hook(name)
            sleep(self.interval)
