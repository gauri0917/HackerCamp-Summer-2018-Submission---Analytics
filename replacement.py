#extracting text files
with open("first_suffix.txt", 'r') as f:
    two_first_unique = [line.rstrip('\n') for line in f]

with open("last_suffix.txt", 'r') as f:
    two_last_unique = [line.rstrip('\n') for line in f]

# this function returns the unique name if there are same name but different suffix
def pp(k,l):
    u=l; #initialy it is same as first name without suffix
    for t in range(0,len(two_first_unique)): #iterate over all unique names with two words
        j=two_first_unique[t]
        y=j.find(" ")
        if(l==j[0:y] and k!=j): #if the first name is same but suffix is not
            u=k #return the name as unique
        
    return u

# this function returns the unique name if there are same name but different suffix
def pt(k,l):
    u=l; #initialy it is same as last name without suffix
    for t in range(0,len(two_last_unique)): #iterate over all unique names with two words
        j=two_last_unique[t]
        y=j.find(" ")
        if(l==j[0:y] and k!=j):#if the first name is same but suffix is not
            u=k #return the name as unique
       
    return u

#this funnction process to remove suffix
def process3(x):
    i=x.find(" ")
    if(i!=-1): #if there are two words
        x1=pp(x,x[0:i]) #check for its replacement
  
        x=x1
        
    return x

#this funnction process to remove suffix
def process4(x):
    i=x.find(" ")
    if(i!=-1):#if there are two words
        x1=pt(x,x[0:i]) #check for its replacement
  
        
        x=x1
        
    return x

