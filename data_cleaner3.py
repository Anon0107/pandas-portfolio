import pandas as pd

# Load the file
try:
    df = pd.read_excel('BanG Dream! Characters.xlsx')
except FileNotFoundError:
    print("File not found. Make sure it's uploaded.")
    # Stop here if error
# Simple change: merge role1 and role2
df = df.fillna(False)
def mergeroles(row):
  if row.Role2:
     row.Role1 = row.Role1 + ', ' + row.Role2
  return row


df = df.apply(mergeroles,axis = 'columns')
df = df.drop('Role2', axis = 'columns')
df = df.rename(columns = {'Role1':'Roles'})

# Save new file
df.to_excel('Bang Dream! Characters(cleaned).xlsx', index=False)

print("Done! Check Bang Dream! Characters(cleaned).xlsx")