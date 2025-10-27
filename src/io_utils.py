#data/io_utils.py = utility funktioner som t.ex: load_data(...) – kan vara csv/open eller pandas.read_csv

import pandas as pd

def load_data(csv_file):
    return pd.read_csv(csv_file)
    