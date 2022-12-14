from rich.table import Table as RichTable
from rich.console import Console as RichConsole
from rich import print as rich_print
import numpy as np
from rich.pretty import pprint
import shutil

print(shutil.get_terminal_size())


class RichTableCreator:
    """RichTable Class"""

    def __init__(self):
        self.index = 0
        self.verification_data = []
        self.table = RichTable(title="Verification", show_lines=True)
        self.table.add_column("Index")
        self.table.add_column("Step")
        self.table.add_column("Envelope | Tested")
        self.table.add_column("Config | Expected")
        self.table.add_column("AirSniff")
        self.table.add_column("Result")

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
            # RichConsole().print(self.table)
            rich_print(self.table)
            # pprint(self.table)

        except Exception as err:
            return False
        return True

    def printer(self, _list):
        """show the table"""
        try:
            num_of_path = 5
            num_of_chain = int(len(_list) / num_of_path)
            _list = np.reshape(_list, (num_of_chain, num_of_path))
            for _i_ in range(num_of_chain):
                temp_list = _list[_i_, :]
                self.update(temp_list)
            RichConsole(width=200, force_interactive=True).print(self.table)

            # pprint(self.table)

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
]
rich_table.print(mylist)
rich_table.printer(mylist)
print(shutil.get_terminal_size())
