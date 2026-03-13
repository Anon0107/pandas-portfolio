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

# Save new file
df.to_excel('Cleaned_sample_laptop_sales.xlsx', index=False)

print("Done! Check Cleaned_sample_laptop_sales.xlsx")