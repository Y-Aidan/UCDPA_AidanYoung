import pandas as pd

#Downloading large file from GLEIF.org with LEI details for Euronext LEI Codes.
#CSV file is sparse so DropNA is used to remove excess columns
#Drop unnecessary columns that don't aren't needed for this part
#Columns all have . in name so I renamed them to be able to work with them.
df = pd.read_csv(r'C:\Users\Aido\Downloads\lei-records.csv', sep=',', low_memory=False)
df = df.dropna(axis=1)
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

#Same as above but with the ELF (Entity Legal Form) List to replace ELF Codes with words.
#The ELF Code list were 4 character strings with no obvious meaning
df_ELF = pd.read_csv(r'C:\Users\Aido\Downloads\elf-code-list.csv', sep=',', dtype=object)
df_ELF = df_ELF.drop([0,1])
df_ELF = df_ELF.dropna(axis=1)
df_ELF = df_ELF.drop(labels=['Country Code (ISO 3166-1)',
                             'Language Code (ISO 639-1)','Date created YYYY-MM-DD (ISO 8601)',
                             'ELF Status ACTV/INAC'], axis=1, inplace=False)
df_ELF = df_ELF.rename(columns={'Entity Legal Form name Local name':'LegalFormName',
                                'ELF Code': 'ELFCode'})
#In my first attempt Irish Companys had their names written in Irish which would confuse my analysis.
#I put in the below fix to only return the English language Legal Forms
df_ELF = df_ELF.set_index("Language")
df_ELF = df_ELF.drop("Irish")

#Replicated the ELFCode column in the main Dataset.
#Now I want to cycle through the ELFCode column and replace it with LegalFormName from df_ELF
df['ELFName'] = df['ELFCode']
new_transformed_df = df.replace(dict(zip(df_ELF.ELFCode, df_ELF.LegalFormName)))

print(new_transformed_df)

#The Transformation doesn't take into account dummy ELF Codes 8888 and 9999 which I want to classify later
#                                            LegalName  ...                    ELFName
#0                                    MetLife SK, a.s.  ...                       9999
#1     The Irish Stock Exchange Public Limited Company  ...     Public Limited Company
#2                                   Seil and Motor AS  ...               Aksjeselskap
#3                                     MacMachineryLtd  ...                       8888
#4                             Raidió Teilifís Éireann  ...  Private Unlimited Company

new_transformed_df2 = new_transformed_df.set_index("ELFName")
new_transformed_df3 = new_transformed_df
new_transformed_df3 = new_transformed_df.set_index("ELFName")
new_transformed_df2 = new_transformed_df2.drop("8888")
new_transformed_df2 = new_transformed_df2.drop("9999")

print(new_transformed_df2)

study_df = set(new_transformed_df3['ELFCode']).difference(new_transformed_df2['ELFCode'])
study_df_rows = new_transformed_df3['ELFCode'].isin(study_df)
df4 = new_transformed_df3[study_df_rows]
#print(df4['LegalName'])
