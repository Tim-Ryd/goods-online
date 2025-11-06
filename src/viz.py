#viz.py = plot-funktioner

import matplotlib.pyplot as plt
import pandas as pd
from . import metrics

def top_3_category_by_revenue_graph(df: pd.DataFrame):
    """
    Ger tillbaka ett stapeldiagram som visualiserar top 3 kategorier utifrån intäkt.
    """
    top_3 = df.groupby('category')['revenue'].sum().reset_index()
    top_3 = top_3.sort_values('revenue', ascending=False).head(3)
    colors = ['#FF5733', '#33C1FF', '#33FF57']  
    
    plt.figure(figsize=(5,5))
    plt.bar(top_3['category'], top_3['revenue'], color=colors)
    plt.title('Top 3 Categories by Revenue')
    plt.xlabel('Category')
    plt.ylabel('Revenue')
    plt.show()

def category_by_revenue_graph(df: pd.DataFrame):
    """
    Ger tillbaka ett stapeldiagram som visualiserar  kategorier utifrån intäkt.
    """
    category_df = df.groupby('category')['revenue'].sum().reset_index().sort_values('revenue', ascending=False)

    cmap = plt.get_cmap('tab10')  # tab10 har 10 tydligt olika färger
    colors = [cmap(i) for i in range(len(category_df))]
    
    plt.figure(figsize=(5,5))
    plt.bar(category_df['category'], category_df['revenue'], color=colors)
    plt.title('Categories by Revenue')
    plt.xlabel('Category')
    plt.ylabel('Revenue')
    plt.show()

def bar_graph(df: pd.DataFrame,x:str,y:str,title:str, xlabel:str, ylabel:str):
    """
    Skapar och visar ett stapeldiagram som visualiserar den totala summan av y för varje kategori i x.
    """
    category_df = df.groupby(x)[y].sum().reset_index().sort_values(y, ascending=False)

    cmap = plt.get_cmap('tab10')  # tab10 har 10 tydligt olika färger
    colors = [cmap(i) for i in range(len(category_df))]
    
    plt.figure(figsize=(5,5))
    plt.bar(category_df[x], category_df[y], color=colors)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()



def top_3_date_by_revenue_graph(df: pd.DataFrame):
    """
    Skapar och visar ett stapeldiagram som visualiserar de top 3 bästa försäljningsdatumen.
    
    """
    # Get top 3 dates
    top_3 = df.groupby('date', as_index=False)['revenue'].sum()
    top_3 = top_3.sort_values('revenue', ascending=False).head(3)
    colors = ['#FF5733', '#33C1FF', '#33FF57']  

    plt.figure(figsize=(5,5))
    plt.bar(top_3['date'].astype(str), top_3['revenue'], color=colors)
    plt.title('Top 3 Dates by Revenue')     
    plt.xlabel('date')
    plt.ylabel('revenue')
    plt.show()



def month_by_month_revenue_graph(df: pd.DataFrame):
    """

    Skapar och visar ett linjediagram som illustrerar intäkt per månad.
    
    """


    # Extrahera månad från datum
    df['month'] = df['date'].dt.month
    
    # Summera revenue per månad
    monthly_revenue = (
        df.groupby('month', as_index=False)['revenue']
          .sum()
          .sort_values('month')
    )

    # Rita linjediagram
    plt.figure(figsize=(5,5))
    plt.plot(monthly_revenue['month'], monthly_revenue['revenue'],
             marker='o', color='#335BFF')
    plt.title('Month by Month Revenue')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.xticks(monthly_revenue['month'])  # dynamisk x-axel
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def revenue_by_category(df: pd.DataFrame):
    """
    Skapar och visar ett linjediagram som visualiserar månatlig omsättning per kategori.
    
    """

    # Extrahera månad
    df['month'] = df['date'].dt.month
    
    # Summera revenue per month per category
    monthly_category_revenue = (
        df.groupby(['month', 'category'], as_index=False)['revenue']
          .sum()
          .sort_values(['category','month'])
    )
    #Unika kategorier
    categories = monthly_category_revenue['category'].unique()
    
    plt.figure(figsize=(5,5))
    # Rita respektive linje för kategorierna
    for cat in categories:
        cat_data = monthly_category_revenue[monthly_category_revenue['category'] == cat]
        plt.plot(
            cat_data['month'],
            cat_data['revenue'],
            marker='o',
            label=cat
        )
    # Namnge labels, titlar...
    plt.title('Month by Month Revenue per Category')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.grid(True)
    plt.legend(title='Category')
    # Sortera månaderna så de är i ordning samt namnge dem istället för siffor.
    months = sorted(monthly_category_revenue['month'].unique())
    month_names = [pd.Timestamp(2025, m, 1).strftime('%b') for m in months]
    plt.xticks(months, month_names)
    
    plt.tight_layout()
    plt.show()





def revenue_per_city(df: pd.DataFrame):
    """
    Skapar och visualiserar ett stapeldiagram som visar intäkt per stad.
    
    """
    city_data = metrics.summary_city(df)
    plt.figure(figsize=(8,5))
    plt.bar(city_data["city"], city_data["total_revenue"], color="pink")
    plt.title("Intäkt per stad")
    plt.xlabel("Stad")
    plt.ylabel("Total intäkt (kr)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()    
    
