import psutil
import pandas as pd
import numpy as np
import time
import json
import os

def collect_process_data():
    process_data = []
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'io_counters', 'threads', 'status']):
        try:
            io_counters = process.info['io_counters']
            read_bytes = io_counters.read_bytes if io_counters else 0
            write_bytes = io_counters.write_bytes if io_counters else 0

            process_data.append([
                process.info['pid'],
                process.info['name'],
                process.info['cpu_percent'],
                process.info['memory_percent'],
                read_bytes,
                write_bytes,
                process.info['threads'],
                process.info['status']
            ])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    columns = ['PID', 'Name', 'CPU', 'Memory', 'Read_Bytes', 'Write_Bytes', 'Threads', 'Status']
    return pd.DataFrame(process_data, columns=columns)


def save_data(data, filename='process_log.json'):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump([], f)
    with open(filename, 'r') as f:
        logs = json.load(f)
    logs.append(data.to_dict())
    with open(filename, 'w') as f:
        json.dump(logs, f, indent=4)