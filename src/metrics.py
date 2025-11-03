#metrics.py = nyckeltals-funktioner

def top_3_category_by_revenue(df):
    """
    Ger tillbaka en DataFrame innehållande top 3 kategorier utifrån intäkt. Sorterade från högst till lägst.
    """

    top_3 = df.groupby('category')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).head(3).reset_index(drop=True)

    return top_3


def top_3_date_by_revenue(df):
    """
    Ger tillbaka en DataFrame innehållande top 3 datum utifrån intäkt. Sorterade från högst till lägst
    """
    top_3 = df.groupby('date')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).head(3).reset_index(drop=True)

    return top_3


def revenue_per_city(df):
    """
    Ger tillbaka en DataFrame innehållande intäkt per stad. Sorterade från högst till lägst
    """
    return (df.groupby("city")["revenue"]
    .agg(revenue = "sum").sort_values('revenue', ascending=False).reset_index())


def revenue_per_category(df):
    """
    Ger tillbaka en DataFrame innehållande intäkt per kategori. Sorterade från högst till lägst
    """
    return (df.groupby("category")["revenue"]
    .agg(revenue = "sum").sort_values('revenue', ascending=False).reset_index())


def total_revenue(df):
    """
    Ger tillbaka en summering av samtliga intäker från DataFrame
    """
    return df["revenue"].sum()


def total_units(df):
    """
    Ger tillbaka en summering av totala enheter sålda från DataFrame
    """
    return df["units"].sum()

def aov(df):
    """
    Ger tillbaka en snitt ordervärdet från DataFrame
    """
    return total_revenue(df) / (len(df) + 1)

def aov_per_category(df):
    """
    Ger tillbaka en DataFrame innehållande average order value (aov) per kategori. Sorterad högst till lägst.
    """
    df_grouped = df.groupby('category')[['units', 'revenue']].sum().reset_index()
    df_grouped['aov'] = (df_grouped['revenue'] / df_grouped['units'])
    df_grouped = df_grouped.sort_values('aov', ascending=False).reset_index(drop=True)

    return df_grouped[['category', 'aov']]

def summary_city(df):
    # Gruppindelning: räkna ihop intäkt, antal produkter och ordrar per stad
    city_data = df.groupby("city").agg(
        total_revenue=("revenue", "sum"),
        total_units=("units", "sum"),
        orders=("order_id", "nunique")
    ).reset_index()

    # Sortera städerna från högst till lägst intäkt
    city_data = city_data.sort_values("total_revenue", ascending=False).reset_index(drop=True)

    # Visa resultatet
    return city_data

import pandas as pd

def revenue_by_category(df: pd.DataFrame) -> dict:
    """
    Calculates total revenue per category.
    Returns a dictionary with the format:
    {"Electronics": 12000, "Clothing": 8000, ...}
    """
    grouped = df.groupby("category")["revenue"].sum()
    return grouped.to_dict()


def top_3_category_by_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the top 3 categories based on total revenue.
    """
    top_3 = (
        df.groupby("category")["revenue"]
        .sum()
        .reset_index()
        .sort_values("revenue", ascending=False)
        .head(3)
    )
    return top_3


def top_3_date_by_revenue(
    df: pd.DataFrame,
    date_col: str = "date",
    price_col: str = "price",
    qty_col: str = "quantity",
    revenue_col: str = "revenue",
) -> pd.DataFrame:
    """
    Returns the top 3 dates with the highest total revenue.
    """
    d = df.copy()

    if not pd.api.types.is_datetime64_any_dtype(d[date_col]):
        d[date_col] = pd.to_datetime(d[date_col], errors="coerce")

    # Calculate total revenue per date
    d[revenue_col] = d[price_col] * d[qty_col]
    top_3 = (
        d.groupby(date_col)[revenue_col]
        .sum()
        .reset_index()
        .sort_values(revenue_col, ascending=False)
        .head(3)
    )

    return top_3


def compute_revenue_by_city(df):
    """
    Beräknar total intäkt per stad.
    Returnerar en DataFrame sorterad från högst till lägst.
    """
    revenue = df.groupby('city')['revenue'].sum().reset_index()
    revenue = revenue.sort_values(by='revenue', ascending=False)
    return revenue
