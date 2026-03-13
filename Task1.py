import pandas as pd
# Load file
try:
  df = pd.read_excel('Task1.xlsx')
except FileNotFoundError:
  print(f"File not found. Make sure it's uploaded")
  raise
except Exception as e:
  print(f"File not found: {e}")
  raise # Stop running if error occured
try:
  # Data cleaning
  df = df.drop_duplicates() # Remove duplicates
  df.Quantity = df.Quantity.fillna(0).astype(int) # Handle missing values
  df.Price = df.Price.fillna(df.Price.mean()).astype(int) 
  # Add new column revenue
  df['Revenue'] = df.Quantity * df.Price
except KeyError as e:
  print(f"Column not found: {e}")
  raise
except Exception as e:
  print(f'Other error: {e}')
  raise # Stop running if error occured
df.to_excel('cleaned_Task1.xlsx') # Export file
print('File cleaned_Task1 created')
