import pandas as pd

# Importing my data
df = pd.read_csv(r'C:\Users\Aido\Downloads\lei-records.csv', delimiter=',')
# Inspecting the information
print(df.head())
print(df.info())
