import pandas as pd

# Load the file
try:
    df = pd.read_excel('sample_laptop_sales.xlsx')
except FileNotFoundError:
    print("File not found. Make sure it's uploaded.")
except Exception as e:
    print(f'File not found: {e}') # Stop here if error
# Add column 'Profit per Sale' and 'Total Profit'
try:
    df['Profit per Sale'] = df.Sales - df.Cost
    df['Total Profit'] = df['Profit per Sale'] * df.Amount
except KeyError as e:
    print(f'Column not found: {e}')
except Exception as e:
    print(f'Other error: {e}')
# Save processed file
df.to_excel('Cleaned_sample_laptop_sales.xlsx', index=False)

print("Done! Check Cleaned_sample_laptop_sales.xlsx")
