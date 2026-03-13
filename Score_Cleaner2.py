import pandas as pd
# Load file
try:
  df = pd.read_excel('grades_sample.xlsx')
except FileNotFoundError:
    print('File not found. Make sure it is uploaded.')
    raise
except Exception as e:
    print(f'Error loading file: {e}')
    raise # Stops if error occurred

try:
  # data cleaning
  df = df.drop_duplicates() # Removes duplicate
  df['Math Score'] = df['Math Score'].fillna(df['Math Score'].mean().round(0)).astype(int) # Handle missing values
  df.to_excel('cleaned_grades_sample.xlsx') # Saves cleaned file
  # statistics for math and physics
  stats = df.describe().round(1).drop(index = ['25%','50%','75%']).rename(columns = {'Math Score':'Math','Physics Score':'Physics'})
  # count of grades
  def calc_grades(row):
    if row >= 70:
      return 'A'
    elif row >= 60:
      return 'B'
    elif row >= 50:
      return 'C'
    else:
      return 'D'
  math_scores = df['Math Score'].apply(calc_grades).value_counts() # math grade counts
  physics_scores = df['Physics Score'].apply(calc_grades).value_counts() # physics grade counts
  grades = pd.DataFrame({'Math':math_scores,'Physics':physics_scores}).fillna(0) # merging Series into dataframe
  summary = pd.concat([grades,stats],axis = 'index') # Merging grade counts and statistics
except KeyError as e:
  print(f'Column not found: {e}')
  raise
except Exception as e:
  print(f'Other error: {e}')
  raise # Stops if error
summary.to_excel('grades_sample_summary.xlsx')
print('Files cleaned_grades_sample.xlsx and grades_sample_summary.xlsx created.') # Saves cleaned and processed files
