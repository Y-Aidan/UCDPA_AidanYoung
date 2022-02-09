import pandas as pd

#Importing the CSV again as normal
df = pd.read_csv(r'C:\Users\Aido\Downloads\lei-records.csv', sep=',', dtype=object)
df = df.dropna(axis=1)
df_clean = df.rename(columns={"Entity.LegalName": "LegalName",
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
#The most basic iterator. I couldn't think of an Interesting use within the project.
output = iter(df.LEI)

print(next(output))
print(next(output))
print(next(output))
