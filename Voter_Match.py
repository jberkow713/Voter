import pandas as pd

class District:
    '''
    Creates dataframe for a given txt file
    '''
    def __init__(self, num):
        self.txt = f'District_{num}.txt'
        self.df = self.create_df()
    def create_df(self):
        data = pd.read_csv(self.txt, sep=',')
        usable = ['LAST_NAME','FIRST_NAME', 'DATE_OF_BIRTH',\
            'RESIDENTIAL_CITY', 'RESIDENTIAL_STATE', 'RESIDENTIAL_ZIP','SOS_VOTERID']
        data = data[usable]
        data['birth_year']=data['DATE_OF_BIRTH'].str.split('-').str[0]
        final_usable = ['LAST_NAME', 'FIRST_NAME', 'RESIDENTIAL_ZIP', 'RESIDENTIAL_CITY',\
            'birth_year','SOS_VOTERID']
        District = data[final_usable]
        return District.apply(lambda x: x.astype(str).str.lower())

class Search_List:
    '''
    Creates a list of districts to compare to, creates a dataframe to search from
    '''
    def __init__(self, csv,num_districts):
        self.csv = csv
        self.df = self.create_df()
        self.row_indices = self.df.index.values.tolist()
        self.num_districts = num_districts
        self.districts = self.create_districts()
         
    def create_df(self):
        Search =  pd.read_csv(self.csv)
        Search = Search.dropna()        
        Search['RESIDENTIAL_ZIP']=Search['zip'].astype(int)
        Search['birth_year']=Search['birth_year'].astype(int)
        new = Search["name"].str.split(" ", expand = True)        
        Search["FIRST_NAME"]= new[0]         
        Search['LAST_NAME'] = Search['name'].str.split().str[-1]
        Search['RESIDENTIAL_CITY']=Search['city']
        Search['ID']=None        
        usable_csv = ['LAST_NAME', 'FIRST_NAME', 'RESIDENTIAL_ZIP', 'RESIDENTIAL_CITY', 'birth_year','ID']
        Final_Search = Search[usable_csv]        
        return Final_Search.apply(lambda x: x.astype(str).str.lower())
    
    def create_districts(self):
        Districts = []
        for i in range(1,self.num_districts+1):
            Districts.append(District(i).df)           
        return Districts
    
    def find_IDS(self):
        '''
        Finds missing IDs based on the stored dataframes by looking for highest
        probability match. 
        '''        
        for i in range(len(self.row_indices)):
            Current = self.row_indices[i]
            Current_Search = self.df.loc[Current].to_list()
            L_name = Current_Search[0]
            current = 0
            ID = None
            for district in self.districts:
                # Initially filters by checking for last name
                New = district.loc[district['LAST_NAME']==L_name]
                D = {}
                # Runs secondary check if last name matches to check
                # how many other values match
                if len(New.values.tolist())>0:                    
                    for name in New.values.tolist():
                        count = 0
                        compare = name[:4]
                        id = name[5]
                        for i in range(4):
                            if Current_Search[i]==compare[i]:
                                count+=1
                        D[id]=count         
                    # Sets current value equal to the number of matches of the ID with highest value
                    max_value = max(D, key=D.get)                    
                    if D[max_value]>current:
                        # Sets current, or the ID, equal to the new ID
                        current = D[max_value]
                        ID =int(max_value[2:])
            # Sets the ID in place in the dataframe with highest probability ID
            Search.df.at[Current,'ID']=ID
            # Saves to new file
            Search.df.to_csv('voter_data.csv')
        return Search.df

Search = Search_List("original_data.csv",4)
Search.find_IDS()




