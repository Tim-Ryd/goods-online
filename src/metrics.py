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
