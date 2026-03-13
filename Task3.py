import pandas as pd
# Load file
try:
  df = pd.read_excel('Task3.xlsx')
except FileNotFoundError:
  print("File not found. Make sure it's uploaded.")
  raise # Stops if error
except Exception as e:
  print(f'File not found: {e}')
  raise
try:
  # Data cleaning
  df = df.drop_duplicates() # Rmeove duplicates
  df = df.drop(df[(df.Stock < 0) | (df.Stock.isna())].index) # Remove invalid values
  df.to_excel('cleaned_Task3.xlsx')
  # Group by Category
  summary = (df.groupby('Category').Stock.sum().astype(int))
  # Add low stock flag
  summary = pd.concat([summary,(summary<10).rename('Low_stock(<10)')],axis = 1)
except KeyError as e:
  print(f"Column not found: {e}")
  raise
except Exception as e:
  print(f'Other error: {e}')
  raise # Stops if error
summary.to_excel('Task3_summary.xlsx') # Saves report
print('Files cleaned_Task3.xlsx and Task3_summary.xlsx created.') 
