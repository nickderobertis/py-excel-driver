from pythoncom import com_error
import time

from .tools import _kill_excel, _load_excel

def load_addin(excel, addin_str, sleep_time=5):
    try:
        _load_addin(excel, addin_str, sleep_time=sleep_time)
    except com_error:
        print('Did not start excel correctly')
        time.sleep(10)
        print('Killing excel')
        _kill_excel()
        time.sleep(5)
        print('Launching new excel instance')
        excel = _load_excel()
        excel = load_addin(excel, addin_str, sleep_time=sleep_time)

    return excel

def _load_addin(excel, addin_str, sleep_time=5):
    print(f'Loading add-in {addin_str}')
    excel.AddIns(addin_str).Installed = False
    time.sleep(sleep_time)
    excel.AddIns(addin_str).Installed = True