import os
import pathlib
import pandas as pd

def read_data(file:str):
    path = pathlib.Path(os.path.abspath(file))
    df = pd.read_csv(
    path,
    delim_whitespace=True,   # or use sep='\s+' if needed
    comment='#',             # treat lines starting with '#' as comments
    header=None              # no header detected by default because of '#'
    )

    # Now manually extract the header line and apply it
    with open(path) as f:
        for line in f:
            if line.startswith('#'):
                columns = line[1:].strip().split()
                break

    df.columns = columns
    return df