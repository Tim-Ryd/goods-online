#metrics.py = nyckeltals-funktioner

def top_3_category_by_revenue(df):
    top_3 = df.groupby('category')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).head(3)

    return top_3



def top_3_date_by_revenue(df):
    top_3 = df.groupby('date')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).head(3)

    return top_3


def revenue_per_city(df):
    return (df.groupby("city")["revenue"]
    .agg(revenue = "sum").reset_index())


def revenue_per_category(df):
    return (df.groupby("category")["revenue"]
    .agg(revenue = "sum").reset_index())


def total_revenue(df):
    return df["revenue"].sum()


def total_units(df):
    return df["units"].sum()

def aov(df):
    return total_revenue(df) / (len(df) + 1)

def aov_per_category(df):
    df_grouped = df.groupby('category')[['units', 'revenue']].sum().reset_index()
    df_grouped['aov'] = df_grouped['revenue'] / df_grouped['units']

    return df_grouped[['category', 'aov']]

