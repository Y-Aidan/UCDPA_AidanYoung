#My Data doesn't have any any blank entries as I was quite aggressive in my dropna
#I should have almost no Duplicates as LEI Codes should be unique to entities
import pandas as pd

#Importing the CSV again as normal
df = pd.read_csv(r'C:\Users\Aido\Downloads\lei-records.csv', sep=',', dtype=object)
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

duplicates = df.duplicated(subset ='LegalName', keep = False)
duplicates_name = df[duplicates].sort_values('LegalName')
X = ['LegalName', 'LegalAddress', 'Status']
print(duplicates_name[X])
#                         LegalName                 LegalAddress     Status
#2826        Bacchantes Two Limited            First Names House    RETIRED
#4320        Bacchantes Two Limited            First Names House     LAPSED
#355   Carbery Food Ingredients Ltd                    Ballineen     ISSUED
#2321  Carbery Food Ingredients Ltd  Ballineen, Co Cork, Ireland  DUPLICATE
#193     The McLaughlin Partnership             49 Dawson Street     ISSUED
#3803    The McLaughlin Partnership           30 Beech Park Road     ISSUED

#Of the 6 above entities, only Carbery Food Ingredients Ltd is actually a Duplicate. The McLaughlin Partnerships are
#2 distinct Legal Entities with the same name and the original Bacchantes Two Limited dissolved before the second was
#created.

