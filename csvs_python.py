import numpy as np
import pandas as pd

# Sample data
data = "data/Scatterplot data/scatterplot_dist.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(data)

# Group by 'Bedroom2' and 'Type', and calculate the mean price for each group
grouped_df = df.groupby(['Distance', 'Type'])['Price'].mean().reset_index()

# Rename the 'Price' column to 'Average Price'
grouped_df = grouped_df.rename(columns={'Price': 'Average Price'})

# To display the first few rows of the new DataFrame:
print(grouped_df.head())

# Save the new DataFrame to a CSV file
grouped_df.to_csv('average_prices_by_bedroom_type.csv', index=False)


grouped_df.to_csv('average_prices_by_Distance.csv', index=False)
