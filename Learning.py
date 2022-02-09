import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import statsmodels.formula.api as smf

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
#Changing the type of the dates from Objects to Dates
df['RegistrationDate'] = df['RegistrationDate'].astype('datetime64[ns]')
df['NextRenewalDate'] = df['NextRenewalDate'].astype('datetime64[ns]')
df['LastUpdate'] = df['LastUpdate'].astype('datetime64[ns]')

#Setting up a Histogram to show the waves of New Issued, Last Updates, and the Next Renewal Dates. Renewal Dates in the past would be Lapsed
x = (df['RegistrationDate'], df['LastUpdate'], df['NextRenewalDate'])
df.sort_index(axis=1)
print(df['Status'].count())
plt.hist(x, bins=100, density=True, histtype='bar')
plt.show()

