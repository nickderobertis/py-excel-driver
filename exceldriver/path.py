from typing import Sequence, Tuple
import winreg
import os

RegistryTuple = Tuple[str, str, int]


def get_excel_path():
    handle = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE,
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\excel.exe"
    )
    tuples = _registry_tuples_from_handle(handle)
    excel_root_path = _get_key_value_from_registry_tuples(tuples, 'Path')
    excel_path = os.path.join(excel_root_path, 'EXCEL.EXE')
    return excel_path


def _get_key_value_from_registry_tuples(tuples: Sequence[RegistryTuple], key: str) -> str:
    for tup in tuples:
        match_key = tup[0]
        if key == match_key:
            return tup[1]
    raise ValueError(f'none of the passed tuples had the key {key}')


def _registry_tuples_from_handle(handle) -> Sequence[RegistryTuple]:
    num_values = winreg.QueryInfoKey(handle)[1]
    tuples = []
    for i in range(num_values):
        tuples.append(winreg.EnumValue(handle, i))
    return tuples