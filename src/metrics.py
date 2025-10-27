#metrics.py = nyckeltals-funktioner

def top_3_category_by_revenue(df):
    top_3 = df.groupby('category')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).head(3)

    return top_3





# Ny funktion för att få top 3 datum med högst intäkter / DR

def top_3_date_by_revenue(df):
    top_3 = df.groupby('date')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).head(3)

    return top_3



#säsongsmönster-funktion

def month_by_month_revenue(df):
    df['month'] = df['date'].str.slice(5,7).astype(int)

    monthly_revenue = df.groupby('month')['revenue'].sum().reset_index().sort_values('month')

    return monthly_revenue

