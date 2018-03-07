#clean the data
#extracting text files
with open("prefix.txt", 'r') as f:
    prefix = [line.rstrip('\n') for line in f]
with open("suffix.txt", 'r') as f:
    suffix = [line.rstrip('\n') for line in f]


#This function processes/cleans the First name of the dataframe
def process1(x):
    i=x.find(" ") #return the index of space if there are more than one word in name
    if(i!=-1):
        if(x[0:i] in prefix): #if it is a prefix
            x=x[i+1:len(x)] #returns the name without prefix
        else:
            x=x[0:i+2] #returns the name with one letter of suffix to avoid confusion
        
        
    return x

#This function processes/cleans the Last name of the dataframe
def process2(x):
    i=x.find(" ") #return the index of space if there are more than one word in name
   
    if(i!=-1):
        if(x[i+1:len(x)]in suffix): #if it is a suffix
            x=x[0:i] #returns the name without suffix
        else:
            x=x[0:i+2] #returns the name with one letter of suffix to avoid confusion
        
    
        
        
    return x
