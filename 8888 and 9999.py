import pandas as pd
import regex as re
import matplotlib.pyplot as plt
import seaborn as sns

#Downloading large file from GLEIF.org with LEI details for Euronext LEI Codes.
#CSV file is sparse so DropNA is used to remove excess columns
#Columns all have . in name so I renamed them to be able to work with them.
df = pd.read_csv(r'C:\Users\Aido\Downloads\lei-records.csv', sep=',', low_memory=False)
df = df.dropna(axis=1)
df = df.rename(columns={"Entity.LegalName": "LegalName",
                        "Entity.LegalAddress.Country": "Country",
                        "Entity.LegalForm.EntityLegalFormCode": "ELFCode",
                        "Entity.EntityStatus": "EntityStatus",
                        "Registration.InitialRegistrationDate": "RegistrationDate",
                        "Registration.LastUpdateDate": "LastUpdate",
                        "Registration.RegistrationStatus": "Status",
                        "Registration.NextRenewalDate": "NextRenewalDate",
                        })
df = df.drop(labels=["Entity.LegalAddress.FirstAddressLine",
                     "LEI",
                     "Entity.HeadquartersAddress.FirstAddressLine",
                      "Entity.HeadquartersAddress.Country",
                      "Entity.RegistrationAuthority.RegistrationAuthorityID",
                      "Registration.ManagingLOU",
                      "Registration.ValidationSources",
                     "Entity.LegalJurisdiction",
                     "Registration.ManagingLOU",
                     "Registration.ValidationSources",
                     "Registration.ValidationAuthority.ValidationAuthorityID",
                      "Registration.ValidationAuthority.ValidationAuthorityID"], axis=1, inplace=False)
df['RegistrationDate'] = df['RegistrationDate'].astype('datetime64[ns]')
df_Country = df.set_index("Country")
df_Country = df_Country.loc[['GB'],["ELFCode","Status","RegistrationDate", "EntityStatus"]]
data = pd.DataFrame({'x':df_Country['RegistrationDate'],
                     'y':df_Country['Status']})

#sns.stripplot(x='RegistrationDate', y='ELFCode', data=df_Country)
#plt.show()

