#viz.py = plot-funktioner

import matplotlib.pyplot as plt

def top_3_category_by_revenue_graph(df):
    # Get top 3 categories
    top_3 = df.groupby('category')['revenue'].sum().reset_index()
    top_3 = top_3.sort_values('revenue', ascending=False).head(3)
    colors = ['#FF5733', '#33C1FF', '#33FF57']  
    
    plt.figure(figsize=(5,5))
    plt.bar(top_3['category'], top_3['revenue'], color=colors)
    plt.title('Top 3 Categories by Revenue')
    plt.xlabel('Category')
    plt.ylabel('Revenue')
    plt.show()