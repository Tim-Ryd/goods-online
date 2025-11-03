#data/io_utils.py = utility funktioner som t.ex: load_data(...) – kan vara csv/open eller pandas.read_csv

import pandas as pd

<<<<<<< HEAD
def load_data(csv_file):
    return pd.read_csv(csv_file)
    
=======
REQUIRED = [
    "order_id","date","city","category","price","units","revenue"
]

def load_data(path: str) -> pd.DataFrame:
    """
    Läser in CSV fil samt gör om kolumner innehålande datum till datetime.
    """

    df = pd.read_csv(path, parse_dates=["date"])

    missing = [c for c in REQUIRED if c not in df.columns]

    if missing:
        raise ValueError(f"Saknade kolumner: {missing}")

    return df
>>>>>>> main
