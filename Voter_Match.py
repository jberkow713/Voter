import pandas as pd

data = pd.read_csv('District_1.txt', sep=',')
usable = ['LAST_NAME','FIRST_NAME', 'DATE_OF_BIRTH',\
    'RESIDENTIAL_CITY',\
        'RESIDENTIAL_STATE', 'RESIDENTIAL_ZIP','SOS_VOTERID']
data = data[usable]
data['birth_year']=data['DATE_OF_BIRTH'].str.split('-').str[0]
final_usable = ['LAST_NAME', 'FIRST_NAME', 'RESIDENTIAL_ZIP', 'RESIDENTIAL_CITY',\
    'birth_year','SOS_VOTERID']
District = data[final_usable]
District = District.apply(lambda x: x.astype(str).str.lower())

Search =  pd.read_csv("voter_data.csv")
Search = Search.dropna()
Search['RESIDENTIAL_ZIP']=Search['zip'].astype(int)
Search['birth_year']=Search['birth_year'].astype(int)
new = Search["name"].str.split(" ", expand = True) 
# making separate first name column from new data frame
Search["FIRST_NAME"]= new[0] 
# making separate last name column from new data frame
Search['LAST_NAME'] = Search['name'].str.split().str[-1]
Search['RESIDENTIAL_CITY']=Search['city']
usable_csv = ['LAST_NAME', 'FIRST_NAME', 'RESIDENTIAL_ZIP', 'RESIDENTIAL_CITY', 'birth_year']
Final_Search = Search[usable_csv]
Final_Search = Final_Search.apply(lambda x: x.astype(str).str.lower())

print(District.head())
print(Final_Search.head())

# print(Search.head())
# Search['zip'] = Search['zip'].astype(int)
# print(Search.head())

# Need to create class that takes one csv file, parses a specific text file, and from the info
# Finds the SOS_VOTERID for everyone in the csv who occurs in that district
# ['row', 'name', 'birth_year', 'address', 'city', 'state', 'zip'] this exists in CSV
