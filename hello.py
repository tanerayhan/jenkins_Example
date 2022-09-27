from rich.table import Table as RichTable
from rich.console import Console as RichConsole
from rich import print as rich_print
import numpy as np
from tabulate import tabulate


class RichTableCreator:
    """RichTable Class"""

    def __init__(self):
        self.index = 0
        self.verification_data = []
        self.table = RichTable(
            title="Verification",
            show_lines=True,
            expand=True,
        )
        self.console = RichConsole()
        self.table.add_column("Index", style="cyan", width=40)
        self.table.add_column("Step", style="magenta", width=40)
        self.table.add_column("Envelope | Tested", style="magenta", width=40)
        self.table.add_column("Config | Expected", style="magenta", width=40)
        self.table.add_column("AirSniff", style="magenta", width=40)
        self.table.add_column("Result", style="green", width=40)


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
        )

    def print(self, _list):
        """show the table"""
        try:
            num_of_path = 5
            num_of_chain = int(len(_list) / num_of_path)
            _list = np.reshape(_list, (num_of_chain, num_of_path))
            for _i_ in range(num_of_chain):
                temp_list = _list[_i_, :]
                self.update(temp_list)

            self.console.print(self.table)
            rich_print(self.table)

        except Exception as err:
            return False
        return True


rich_table = RichTableCreator()
mylist = [
    "AASSADFASDGKAS GKAKSDG",
    2,
    3,
    4,
    5,
    "AirtiesWirelessNetwork",
    "AASSADFASGKA GKSKDGA",
    8,
    9,
    10,
    11,
    12,
    "AASSADFASDGKAS GKADGA",
    14,
    15,
    16,
    17,
    18,
    "AASSADFASDGKASKDGKAAA",
    20,
    21,
    22,
    23,
    24,
    25,
]
rich_table.print(mylist)
col_names = [
    "Index",
    "Step",
    "Envelope | Tested",
    "Config| Expected",
    "AirSniff",
    "Result",
]

# display table
data = [
    [
        1,
        "SomeDetailed Text",
        3,
        4,
        5,
        "AirtiesWireleKSKSKK",
    ],
    [
        2,
        8,
        9,
        10,
        11,
        12,
    ],
    [
        3,
        14,
        15,
        16,
        17,
        "AGGAAGGAAGAGAGG",
    ],
    ["AASSADFASDGKASKDG", 20, 21, 22, 23, 24],
]
print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
