import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('AB_NYC_2019.csv')

# Define custom dark red color for the plots
plotly_dark_red_theme = {
    'plot_bgcolor': 'black',  # Dark background
    'paper_bgcolor': 'black',  # Dark background
    'font': {'color': 'white'},  # White font color
    'xaxis': {'showgrid': False, 'color': 'white'},  # White axis labels
    'yaxis': {'showgrid': False, 'color': 'white'}   # White axis labels
}

# Binning the price column into ranges (e.g., 0-100, 101-200, ...)
bins = [0, 100, 200, 300, 400, 500]
labels = ['0-100', '101-200', '201-300', '301-400', '401-500']
df['price_range'] = pd.cut(df['price'], bins=bins, labels=labels, right=False)

# Price Distribution Plot (showing separate bars for each price range)
# Explicitly sort the values by price range
price_dist_fig = px.histogram(df, x="price_range", title="Price Distribution by Range")

# Update the histogram appearance
price_dist_fig.update_layout(
    title={'font': {'color': 'white'}},  # White title
    coloraxis_showscale=False,  # Remove color scale
    barmode='overlay',  # Adjust bar overlay if necessary
    template='plotly_dark',  # Use a dark theme for the plot
    xaxis_title="Price Range",
    yaxis_title="Count",
    xaxis={'categoryorder': 'array', 'categoryarray': labels}  # Ensure proper order
)
price_dist_fig.update_layout(plotly_dark_red_theme)
price_dist_fig.write_html("price_distribution.html")

# Other plots remain unchanged, as per previous code...
# Neighborhood Group Count Plot
neighborhood_counts = df['neighbourhood_group'].value_counts().reset_index()
neighborhood_counts.columns = ['neighbourhood_group', 'count']

neighborhood_count_fig = px.bar(neighborhood_counts,
                                x='neighbourhood_group', y='count',
                                labels={'neighbourhood_group': 'Neighborhood Group', 'count': 'Count'},
                                title="Neighborhood Group Count")
neighborhood_count_fig.update_layout(
    title={'font': {'color': 'white'}},
    template='plotly_dark',
    xaxis_title="Neighborhood Group",
    yaxis_title="Count"
)
neighborhood_count_fig.update_layout(plotly_dark_red_theme)
neighborhood_count_fig.write_html("neighborhood_count.html")

# Price by Neighborhood Plot
price_by_neighborhood_fig = px.bar(df.groupby('neighbourhood_group')['price'].mean().reset_index(),
                                   x='neighbourhood_group', y='price',
                                   labels={'neighbourhood_group': 'Neighborhood Group', 'price': 'Average Price'},
                                   title="Price by Neighborhood")
price_by_neighborhood_fig.update_layout(
    title={'font': {'color': 'white'}},  # White title
    template='plotly_dark',  # Use a dark theme for the plot
    xaxis_title="Neighborhood Group",
    yaxis_title="Average Price"
)
price_by_neighborhood_fig.update_layout(plotly_dark_red_theme)
price_by_neighborhood_fig.write_html("price_by_neighborhood.html")