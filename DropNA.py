import pandas as pd

#df = pd.read_csv(r'C:\Users\Aido\Downloads\lei-records.csv', sep=',')
test(df)
df = df.dropna(axis=1)

#print(df.info())

#unique_types1 = df['Entity.EntityStatus'].unique()
#unique_types2 = df['Registration.RegistrationStatus'].unique()
unique_types3 = df['Entity.LegalForm.EntityLegalFormCode'].unique()

#print('Entity Statuses possible - ', unique_types1)
#print('Registration Statuses possible - ', unique_types2)
print(unique_types3)
