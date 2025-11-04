#data/io_utils.py = utility funktioner som t.ex: load_data(...) – kan vara csv/open eller pandas.read_csv

import pandas as pd

    
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

import pandas as pd

def clean_data(df) -> pd.DataFrame:
    """
    Rengör försäljningsdatan
    
    Steg:
    - Ta bort dubbletter
    - Hantera saknade värden
    - Justera datatyper
    - Kontrollera så intäkten stämmer överens samt fyll i siffror om något fält saknas.
    - Standardisera textformatet
    """
    df = df.copy()
    
    # 1
    df = df.drop_duplicates()
    
    # 2
    df = df.dropna(subset=['order_id', 'date', 'city'])
    df = df[df[['price', 'units', 'revenue']].isna().sum(axis=1) < 2]
    df['category'] = df['category'].fillna('Unknown')

    # 3
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['units'] = pd.to_numeric(df['units'], errors='coerce')
    df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')

    
    # 4
    mask_price = df['price'].isna() & df['units'].notna() & df['revenue'].notna()
    df.loc[mask_price, 'price'] = df.loc[mask_price, 'revenue'] / df.loc[mask_price, 'units']
    
    mask_units = df['units'].isna() & df['price'].notna() & df['revenue'].notna()
    df.loc[mask_units, 'units'] = df.loc[mask_units, 'revenue'] / df.loc[mask_units, 'price']
    
    mask_revenue = df['revenue'].isna() & df['price'].notna() & df['units'].notna()
    df.loc[mask_revenue, 'revenue'] = df.loc[mask_revenue, 'price'] * df.loc[mask_revenue, 'units']
    
    mask_all_exist = df['price'].notna() & df['units'].notna() & df['revenue'].notna()
    df.loc[mask_all_exist, 'revenue'] = df.loc[mask_all_exist, 'price'] * df.loc[mask_all_exist, 'units']
    
    # 5
    df['city'] = df['city'].str.strip().str.title()
    df['category'] = df['category'].str.strip().str.title()
    
    # 6. Reset index
    df.reset_index(drop=True, inplace=True)
    
    return df

