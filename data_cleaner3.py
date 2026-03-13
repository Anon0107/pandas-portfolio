import pandas as pd
# Load file
try:
  df = pd.read_excel('grades_sample.xlsx')
except FileNotFoundError:
  print(f"File not found. Make sure it's uploaded.")
  raise
except Exception as e:
  print(f'Error loading file: {e}')
  raise #Stop here if error

#Data cleaning
try:
  df = df.drop_duplicates() # Remove duplicates
  df['Math Score'] = df['Math Score'].fillna(df['Math Score'].mean().round(0)).astype(int) # Handle Missing Values
  df['Physics Score'] = df['Physics Score'].fillna(df['Physics Score'].mean().round(0)).astype(int)
except KeyError as e:
  print(f'Column not found: {e}')
  raise
except Exception as e:
  print(f'Other error: {e}')
# save to new file
df.to_excel('cleaned_grades_sample.xlsx', index = False) # Save cleaned file
print("Done! Check cleaned_grades_sample.xlsx")

