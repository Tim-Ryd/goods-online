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


<<<<<<< HEAD
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
=======
>>>>>>> main
