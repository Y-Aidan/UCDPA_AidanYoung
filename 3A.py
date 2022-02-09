import pandas as pd
import regex as re

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
#Setting up the Regex to find the Company Type Designated Activity Company/DAC
LegalName = df_clean['LegalName']
regex = r".* [Dd]esignated +\w+\s\w+ |.* DAC|.* D.A.C"
count = 0

for object in LegalName:
    results = re.search(regex, object, re.IGNORECASE)

    if results:
        RegexResult = results.group()
        count = count+1
        print(RegexResult)
print(count)

#Again for PLCs. Interestingly the IGNORECASE does not bring in any extra DACs but triples the number of PLCs found.
regex2 = r".* plc|.* p\.l\.c|.* public\s*limited\s*company"
count2 = 0
for object in LegalName:
    results = re.search(regex2, object, re.IGNORECASE)

    if results:
        RegexResult = results.group()
        count2 = count2+1
        print(RegexResult)
print(count2)