#metrics.py = nyckeltals-funktioner

def top_3_category_by_revenue(df):
    top_3 = df.groupby('category')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).head(3)

    return top_3



def top_3_date_by_revenue(df):
    top_3 = df.groupby('date')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).head(3)

    return top_3
import pandas as pd

def revenue_per_category(df):
    """
    Beräknar total intäkt per kategori.
    
    Argument:
        df (DataFrame): DataFrame med kolumnerna 'category' och 'revenue'
    
    Returnerar:
        DataFrame sorterad efter total intäkt per kategori (högst först)
    """
    revenue_df = (
        df.groupby("category", as_index=False)["revenue"]
        .sum()
        .sort_values(by="revenue", ascending=False)
    )
    return revenue_df
