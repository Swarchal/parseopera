import os
import string
from collections import namedtuple


def parse_filepath(filepath):
   """
   0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17
   0|0|3|0|0|3|-|1|-|0|0 |1 |0 |0 |1 |0 |0 | 1

   example:
       >>> filepath = "003003-1-001001001.tif"
       >>> parse_filepath(filepath)
       ("well": "C03",
         "site": 1,
         "z": 1,
         "channel": 1,
         "filepath": "003003-1-001001001.tif",
         "row": 3,
         "column": 3)
    """
    final_path = filepath.split(os.sep)[-1]
    if final_path.endswith(".tif"):
        final_path = final_path.replace(".tif", "")
    output = namedtuple(
        "Columbus",
        ["well", "site", "z", "channel", "filepath", "row", "column"]
    )
    row = int(final_path[1:3])
    column = int(final_path[4:6])
    well = row_col_to_well(row, column)
    site = int(final_path.split("-")[1])
    z = int(final_path[13:15])
    channel = int(final_path[16:])
    return output(well, site, z, channel, filepath, row, column)


def row_col_to_well(row, column):
    letters = string.ascii_uppercase
    return "{}{:02d}".format(letters[row-1], column)

