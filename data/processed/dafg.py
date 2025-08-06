import pandas as pd

df = pd.read_csv('./data/processed/data.csv', index_col=0, parse_dates=True)

# Reset the index to turn it into a column
df = df.reset_index()

# Rename the index column to 'datetime'
df = df.rename(columns={'index': 'datetime'})

# Save back to CSV
df.to_csv('./data/processed/data.csv', index=False)