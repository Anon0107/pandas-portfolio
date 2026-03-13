import pandas as pd

# Load the file
try:
    df = pd.read_excel('sample_laptop_sales.xlsx')
except FileNotFoundError:
    print("File not found. Make sure it's uploaded.")
    # Stop here if error
# Simple change: add column 'Profit per Sale' and 'Total Profit'

df['Profit per Sale'] = df.Sales - df.Cost
df['Total Profit'] = df['Profit per Sale'] * df.Amount

# Show total profit by region
print(df.groupby('Region')['Total Profit'].sum())

# Delete products with Profit < 0
df = (df.drop(index = df.loc[df['Profit per Sale'] <0].index).reset_index(drop = True))

# Save new file
df.to_excel('Cleaned_sample_laptop_sales.xlsx', index=False)

print("Done! Check Cleaned_sample_laptop_sales.xlsx")

