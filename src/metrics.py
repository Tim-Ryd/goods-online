#metrics.py = nyckeltals-funktioner

def top_3_category_by_revenue(df):
    """
    Ger tillbaka en DataFrame innehållande top 3 kategorier utifrån intäkt. Sorterade från högst till lägst.
    """

    top_3 = df.groupby('category')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).head(3).reset_index(drop=True)

    return top_3



def top_3_date_by_revenue(df):
    top_3 = df.groupby('date')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).head(3)

    return top_3