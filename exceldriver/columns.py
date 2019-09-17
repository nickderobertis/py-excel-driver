import itertools
import string


def excel_cols():
    """
    Generator for excel columns, A, B ... AA, AB... AAA, AAB, etc.

    :return:
    :rtype:
    """
    n = 1
    while True:
        yield from (''.join(group) for group in itertools.product(string.ascii_uppercase, repeat=n))
        n += 1


def get_n_cols_after_col(col: str, n: int) -> str:
    """
    Gets column which is number of columns after passed column.

    Examples:
        >>> get_n_cols_after_col('AA', 3)
        'AD'

    :param col:
    :param n:
    :return:
    """
    col_gen = excel_cols()
    found_col = False
    col_index = -1
    # Keep iterating on generator until at the passed col
    while not found_col:
        col_index += 1
        current_col = next(col_gen)
        if col == current_col:
            found_col = True

    # Iterate generator n times
    for _ in range(n):
        current_col = next(col_gen)

    return current_col