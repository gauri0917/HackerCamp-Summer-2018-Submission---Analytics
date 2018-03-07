
def uniq(df):

            first_unique=df['fn'].unique() #unique first names
            last_unique=df['ln'].unique() #unique last names
            
            first_unique=df['fn'].unique() #unique first names
            last_unique=df['ln'].unique() #unique last names
            two_first_unique=[] #unique first names having 2 words
            for i in range(0,len(first_unique)):
                l=first_unique[i].find(" ") #if space exists then append it to the list
                if(l!=-1):
                    two_first_unique.append(first_unique[i])
            #saving unique first with suffix
            with open('first_suffix.txt','w') as file_handler:
                for item in two_first_unique:
                    file_handler.write("{}\n".format(item))
            
            two_last_unique=[] #unique last names having 2 words
            for i in range(0,len(last_unique)):
                l=last_unique[i].find(" ") #if space exists then append it to the list
                if(l!=-1):
                    two_last_unique.append(last_unique[i])
                    
            #saving unique first with suffix
            with open('last_suffix.txt','w') as file_handler:
                for item in two_last_unique:
                    file_handler.write("{}\n".format(item))
            