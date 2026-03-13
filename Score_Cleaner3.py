import pandas as pd
# Load file
try:
  df = pd.read_excel('Task2.xlsx')
except FileNotFoundError:
  print("File not found. Make sure it's uploaded.")
  raise
except Exception as e:
  print(f'File not found: {e}')
  raise # Stop running when error occurred
try:
  # Data cleaning
  df = df.drop_duplicates() # Remove duplicates
  df.Math = df.Math.fillna(df.Math.mean().round(0)).astype(int) # Handle missing values
  df.Physics = df.Physics.fillna(df.Physics.mean().round(0)).astype(int)
  df.Chemistry = df.Chemistry.fillna(df.Chemistry.mean().round(0)).astype(int)
  df.to_excel('cleaned_Task2.xlsx') # Export file
  # Compuitng grade coutns
  def calc_grades(value):
    if value >= 70:
      return 'A'
    elif value >= 60:
      return 'B'
    elif value >= 50:
      return 'C'
    else:
      return 'D'
  summary = pd.concat([df.Math.apply(calc_grades).value_counts().rename('Math'),
                       df.Physics.apply(calc_grades).value_counts().rename('Physics'),
                       df.Chemistry.apply(calc_grades).value_counts().rename('Chemistry')],axis = 'columns').fillna(0).astype(int) # Merging grade counts of different subjects
  # Add basic stats(removing quartiles)
  summary = pd.concat([summary,df.loc[:,['Math','Physics','Chemistry']].describe()],axis = 'index').drop(index = ['25%','50%','75%']).astype(int)
except KeyError as e:
  print(f'Column not found: {e}')
  raise
except Exception as e:
  print(f'Other error: {e}')
  raise # Stop running when error occurred
summary.to_excel('Task2_summary.xlsx')
print('Files cleaned_Task2.xlsx and Task2_summary.xlsx created.') # Export file
