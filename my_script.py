import platform
import os
import sys
import getpass
import json

os_name= platform.system()
if os_name == 'Darwin': os_name = 'macOS'

report = {
    'os_name': os_name,
    'os_release': platform.release(),
    'os_version': platform.version(),
    'architecture': platform.machine(),
    'processor': platform.processor(),
    'cpu_count': os.cpu_count(),
    'python_version': platform.python_version(),
    'python_interpreter_path': sys.executable,
    'hostname': platform.node(),
    'username': getpass.getuser(),
}
with open("os_report.json", "w") as f:
    json.dump(report, f, indent=4)