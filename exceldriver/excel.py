from pythoncom import com_error
import time

from .tools import _load_excel

class Excel:
    def __init__(self, visible=True):
        self.visible = visible

    def __enter__(self):
        self.xl = load_excel()
        return self.xl

    def __exit__(self, *args):
        self.xl.quit()

def load_excel():
    xl = _load_excel()

    return xl