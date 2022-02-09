#My original file for getting a handle on the ELF-Code-List Dataframe

import pandas as pd

df_ELF = pd.read_csv(r'C:\Users\Aido\Downloads\elf-code-list.csv', sep=',', dtype=object)
df_ELF = df_ELF.drop([0,1])
df_ELF = df_ELF.dropna(axis=1)
df_ELF = df_ELF.drop(labels=['Country Code (ISO 3166-1)',
                             'Language Code (ISO 639-1)','Date created YYYY-MM-DD (ISO 8601)',
                             'ELF Status ACTV/INAC'], axis=1, inplace=False)
df_ELF = df_ELF.rename(columns={'Entity Legal Form name Local name':'Legal Form Name'})
print(df_ELF['Entity Legal Form name Local name'].equals(df_ELF['Legal Form Name']))
print(df_ELF.columns())