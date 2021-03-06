import pandas as pd

#Downloading large file from GLEIF.org with LEI details for Euronext LEI Codes.
#CSV file is sparse so DropNA is used to remove excess columns
#Columns all have . in name so I renamed them to be able to work with them.
df = pd.read_csv(r'C:\Users\Aido\Downloads\lei-records.csv', sep=',', low_memory=False)
df = df.dropna(axis=1)
df = df.rename(columns={"Entity.LegalName": "LegalName",
                              "Entity.LegalAddress.FirstAddressLine": "LegalAddress",
                              "Entity.LegalAddress.Country": "Country",
                              "Entity.HeadquartersAddress.FirstAddressLine": "HQAddress",
                              "Entity.HeadquartersAddress.Country": "HQCountry",
                              "Entity.RegistrationAuthority.RegistrationAuthorityID": "RegistrationAuthority",
                              "Entity.LegalJurisdiction": "LegalJurisdiction",
                              "Entity.LegalForm.EntityLegalFormCode": "ELFCode",
                              "Entity.EntityStatus": "EntityStatus",
                              "Registration.InitialRegistrationDate": "RegistrationDate",
                              "Registration.LastUpdateDate": "LastUpdate",
                              "Registration.RegistrationStatus": "Status",
                              "Registration.NextRenewalDate": "NextRenewalDate",
                              "Registration.ManagingLOU": "LOU",
                              "Registration.ValidationSources": "ValidationSources",
                              "Registration.ValidationAuthority.ValidationAuthorityID": "ValidationAuthorityID"
                              })

#Same as above but with the ELF (Entity Legal Form) List.
df_ELF = pd.read_csv(r'C:\Users\Aido\Downloads\elf-code-list.csv', sep=',', dtype=object)
df_ELF = df_ELF.drop([0,1])
df_ELF = df_ELF.dropna(axis=1)
df_ELF = df_ELF.drop(labels=['Country Code (ISO 3166-1)','Language',
                             'Language Code (ISO 639-1)','Date created YYYY-MM-DD (ISO 8601)',
                             'ELF Status ACTV/INAC'], axis=1, inplace=False)
df_ELF = df_ELF.rename(columns={'Entity Legal Form name Local name':'LegalFormName',
                                'ELF Code':'ELFCode'})

#Replicated the ELFCode column in the main Dataset.
#Now I want to cycle through the ELFCode column and replace it with LegalFormName from df_ELF
df['ELFName'] = df['ELFCode']

new_transformed_df = df.replace(dict(zip(df_ELF.ELFCode, df_ELF.LegalFormName)))

#for df['ELFName'] in df
# if df['ELFName'][i] == df_ELF['ELFCode'][j]
# df['ELFName'][i] becomes df_ELF['LegalFormName[j]

print(new_transformed_df.describe())