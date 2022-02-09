import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import statsmodels.formula.api as smf
import seaborn as sns

#Downloading large file from GLEIF.org with LEI details for Euronext LEI Codes.
#CSV file is sparse so DropNA is used to remove excess columns
#Columns all have . in name so I renamed them to be able to work with them.
df = pd.read_csv(r'C:\Users\Aido\Downloads\lei-records.csv', sep=',', low_memory=False)
df = df.dropna(axis=1)
df = df.drop(labels=["Entity.LegalAddress.FirstAddressLine",
                     "Entity.HeadquartersAddress.FirstAddressLine",
                      "Entity.HeadquartersAddress.Country",
                      "Entity.RegistrationAuthority.RegistrationAuthorityID",
                      "Registration.ManagingLOU",
                      "Registration.ValidationSources",
                     "Entity.LegalJurisdiction",
                      "Registration.ValidationAuthority.ValidationAuthorityID"], axis=1, inplace=False)
df = df.rename(columns={"Entity.LegalName": "LegalName",
                              "Entity.LegalAddress.Country": "Country",
                              "Entity.LegalForm.EntityLegalFormCode": "ELFCode",
                              "Entity.EntityStatus": "EntityStatus",
                              "Registration.InitialRegistrationDate": "RegistrationDate",
                              "Registration.LastUpdateDate": "LastUpdate",
                              "Registration.RegistrationStatus": "Status",
                              "Registration.NextRenewalDate": "NextRenewalDate",
                              })

df['RegistrationDate'] = df['RegistrationDate'].str.replace(r'-.*','')
df['NextRenewalDate'] = df['NextRenewalDate'].str.replace(r'-.*','')
df['LastUpdate'] = df['LastUpdate'].str.replace(r'-.*','')

df['LEIAge'] = df['NextRenewalDate'] - df['RegistrationDate']

#print(df['LEIAge'])

#x = (df['RegistrationDate'],df['NextRenewalDate'])
#df.sort_index(axis=1)
#print(df.head())
#plt.hist(x, bins=50, density=True, histtype='bar')
#plt.show()

sns.heatmap(df.corr(), square=True, cmap='RdYlGn')