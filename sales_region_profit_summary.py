import pandas as pd

# Load the file
try:
    df = pd.read_excel('sample_laptop_sales.xlsx')
except FileNotFoundError:
    print("File not found. Make sure it's uploaded.")
    raise
except Exception as e:
    print(f'File not found: {e}')
    raise  # Stop here if error

try:
    # Add column Profit per Sale and Total Profit
    df['Profit per Sale'] = df.Sales - df.Cost
    df['Total Profit'] = df['Profit per Sale'] * df.Amount
    
    # Show total profit by region
    print(df.groupby('Region')['Total Profit'].sum())
    
    # Delete products with Profit < 0
    df = (df.drop(index = df.loc[df['Profit per Sale'] <0].index).reset_index(drop = True))
except KeyError as e:
    print(f'Column not found: {e}')
    raise
except Exception as e:
    print(f'Other error: {e}')
    raise # Stop here if error

df.to_excel('Cleaned_sample_laptop_sales.xlsx', index=False) # Save cleaned file

print("Done! Check Cleaned_sample_laptop_sales.xlsx")

