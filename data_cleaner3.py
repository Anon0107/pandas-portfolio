import pandas as pd

# Load the file
try:
    df = pd.read_excel('BanG Dream! Characters.xlsx')
except FileNotFoundError:
    print("File not found. Make sure it's uploaded.")
    raise
except Exception as e:
    print(f'File not found: {e}')
    # Stop here if error
# Simple change: merge role1 and role2
try:
    df = df.fillna(False)
    def mergeroles(row):
      if row.Role2:
         row.Role1 = row.Role1 + ', ' + row.Role2
      return row
    
    
    df = df.apply(mergeroles,axis = 'columns')
    df = df.drop('Role2', axis = 'columns')
    df = df.rename(columns = {'Role1':'Roles'})
except KeyError as e:
    print(f'Column not found: {e}')
    raise
except Exception as e:
    print(f'Other error: {e}')

# Save new file
df.to_excel('Bang Dream! Characters(cleaned).xlsx', index=False)

print("Done! Check Bang Dream! Characters(cleaned).xlsx")
