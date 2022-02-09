import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
# Load data
df = pd.read_csv(r'C:\Users\Aido\Downloads\lei-records.csv', sep=',', low_memory=False)
df = df.dropna(axis=1)

df['Registration.InitialRegistrationDate'] = df['Registration.InitialRegistrationDate'].str.replace(r'-.*','')
#df['Registration.InitialRegistrationDate'] = df['Registration.InitialRegistrationDate'].astype('datetime64[ns]')
df['Registration.LastUpdateDate'] = df['Registration.LastUpdateDate'].str.replace(r'-.*', '')
#df['Registration.LastUpdateDate'] = df['Registration.LastUpdateDate'].astype('datetime64[ns]')
df['Registration.NextRenewalDate'] = df['Registration.NextRenewalDate'].str.replace(r'-.*', '')
#df['Registration.NextRenewalDate'] = df['Registration.NextRenewalDate'].astype('datetime64[ns]')

df = df.rename(columns={"Registration.InitialRegistrationDate": "RegistrationDate",
                        "Registration.LastUpdateDate": "LastUpdate",
                        "Registration.NextRenewalDate": "NextRenewalDate",
                        "Registration.RegistrationStatus":"Status"})

df['RegistrationDate'] = df['RegistrationDate'].astype('datetime64[ns]')
df['NextRenewalDate'] = df['NextRenewalDate'].astype('datetime64[ns]')
dates = ['RegistrationDate', 'NextRenewalDate']

LEI_Dates = df[dates]
print(LEI_Dates.info())
plt.scatter(x=df['RegistrationDate'],y =df['Status'])
plt.show()
#print(df['Registration.InitialRegistrationDate'],df['Registration.LastUpdateDate'],df['Registration.NextRenewalDate'])
#print(df['Registration.LastUpdateDate'])
#print(df['Registration.NextRenewalDate'])
#print(df.info())

#plt.plot('RegistrationDate','LastUpdate')
#plt.show()