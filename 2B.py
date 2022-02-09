import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
#Downloading large file from GLEIF.org with LEI details for Euronext LEI Codes.
#CSV file is sparse so DropNA is used to remove excess columns
#Columns all have . in name so I renamed them to be able to work with them.
df = pd.read_csv(r'C:\Users\Aido\Downloads\lei-records.csv', sep=',', dtype= 'str')
#^^print(df.head()) here shows [5 rows x 228 columns]

#MSNO Matrix below can visualise how sparse the CSV file is.
msno.matrix(df)
plt.show()
df = df.dropna(axis=1)
#^^print(df.head()) here shows [5 rows x 17 columns] a huge improvement
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
df = df.rename(columns={"Entity.LegalName": "LegalName",
                        "Entity.LegalAddress.Country": "Country",
                        "Entity.LegalForm.EntityLegalFormCode": "ELFCode",
                        "Entity.EntityStatus": "EntityStatus",
                        "Registration.InitialRegistrationDate": "RegistrationDate",
                        "Registration.LastUpdateDate": "LastUpdate",
                        "Registration.RegistrationStatus": "Status",
                        "Registration.NextRenewalDate": "NextRenewalDate",
                        })
#print(df.columns)
#Index(['LegalName', 'Country', 'ELFCode', 'EntityStatus', 'RegistrationDate',
#       'LastUpdate', 'Status', 'NextRenewalDate'],
#      dtype='object')

#Changing the type of the dates from Objects to Dates
df['RegistrationDate'] = df['RegistrationDate'].astype('datetime64[ns]')
df['NextRenewalDate'] = df['NextRenewalDate'].astype('datetime64[ns]')
df['LastUpdate'] = df['LastUpdate'].astype('datetime64[ns]')
