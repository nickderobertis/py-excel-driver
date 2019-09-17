"""
A tool used to work with Excel from Python. It currently mainly handles starting and stopping
Excel, and getting the active Excel instance and workbook so that COM commands can be run on them.
"""
from .excel import Excel