import pandas as pd
# Load file
try:
  df = pd.read_excel('customer_feedback.xlsx')
except FileNotFoundError:
  print("File not found. Make sure it's uploaded.")
  raise
except Exception as e:
  print(f'File not found: {e}')
  raise # Stop if error
try:
  # Data Cleaning
  df = df.drop_duplicates() # Remove duplicates
  df = df.drop(index = df[(df.Rating.isna())|(df.Rating<0)].index) # Remove rows with missing and invalid ratings
  df = df.sort_values('Date') # Sort by date
  # Add column satisfaction
  def calc_satisfaction(value):
    if value >= 4:
      return 'High'
    elif value == 3:
      return 'Medium'
    else:
      return 'Low'
  df['Satisfaction'] = df.Rating.apply(calc_satisfaction)
  df.to_excel('cleaned_customer_feedback.xlsx',index = False) # Save cleaned file
  # Average rating per product group
  df = df.groupby('Product').Rating.mean().rename('Average Rating')
  df.to_excel('customer_feedback_summary.xlsx') # Save summary file
except IndexError as e:
  print(f'Column not found: {e}')
  raise
except Exception as e:
  print(f'Other error: {e}')
  raise # Stop if error
print('Files cleaned_customer_feedback.xlsx and customer_feedback_summary.xlsx created.')