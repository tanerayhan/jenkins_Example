from rich.table import Table as RichTable
from rich import print as rich_print
import numpy as np


class RichTableCreator:
    """RichTable Class"""

    def __init__(self, product):
        self.index = 0
        self.product = product

        self.table = RichTable(
            title=self.product.upper(), show_lines=False, expand=True
        )
        self.table.add_column("Chain", style="cyan")
        self.table.add_column("AB", style="magenta")
        self.table.add_column("AC", style="magenta")
        self.table.add_column("AD", style="magenta")
        self.table.add_column("BC", style="magenta")
        self.table.add_column("BD", style="magenta")
        self.table.add_column("CD", style="magenta")

    def update(self, _list):
        """table update"""
        self.index += 1
        self.table.add_row(
            str(self.index),
            str(_list[0]),
            str(_list[1]),
            str(_list[2]),
            str(_list[3]),
            str(_list[4]),
            str(_list[5]),
        )

    def print(self, _list):
        """show the table"""
        try:
            num_of_path = 6
            num_of_chain = int(len(_list) / num_of_path)
            _list = np.reshape(_list, (num_of_chain, num_of_path))
            for _i_ in range(num_of_chain):
                temp_list = _list[_i_, :]
                self.update(temp_list)

            rich_print(self.table)
        except Exception as err:
            return False
        return True


rich_table = RichTableCreator(product="Taner")
mylist = [
    "AASSADFASDGKASKDGKASGKAKSDGKSKDGA",
    2,
    3,
    4,
    5,
    6,
    "AASSADFASDGKASKDGKASGKAKSDGKSKDGA",
    8,
    9,
    10,
    11,
    12,
    "AASSADFASDGKASKDGKASGKAKSDGKSKDGA",
    14,
    15,
    16,
    17,
    18,
    "AASSADFASDGKASKDGKASGKAKSDGKSKDGA",
    20,
    21,
    22,
    23,
    24,
]
rich_table.print(mylist)

