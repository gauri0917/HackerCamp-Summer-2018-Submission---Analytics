# Analytics Assignment Innovacer

# Problem Statement 
Variation in names leads to difficulty in identifying a unique person and hence deduplication
of records is an unsolved challenge. The problem becomes more complicated in cases where
data is coming from multiple sources. Following variations are same as Vladimir Frometa:
* Vladimir Antonio Frometa Garo
* Vladimir A Frometa Garo
* Vladimir Frometa
* Vladimir Frometa G
* Vladimir A Frometa
* Vladimir A Frometa G

Train a model to identify unique patients in the dataset

# Dataset Description 
Dataset contains following fields:
* ln: Last name of the patient
* dob: Date of Birth of the patient
* gn: Gender of the patient
* fn: First Name of the patient

# Approach 
* Firstly I clean the data set and remove all the general prefixes annd suffix of a name.
* I prepared a list of all the unique first and last names and extrated the unique name having a prefix/suffix from the data frame.
* Then a algorithm is applied which checks for the replacement of the suffix/prefix by checking it from the unique list of names with prefix and sufix and hence the first and last names are processed to its simplst name possible.
* Then lastly,we apply the drop_duplicate function of pandas to drop the entries with same value in all the fields.

# Cleaning the DataSet
Input: strings name<br/>
Output: Processed Name<br/>
* Firstly we have a pre defined list of sufix and prefix(like Mr.,Mrs.,JR)then check that if the prefix or suffix belongs to anyone of them than it will be ignored or removed.
* If the above case doesn't apply then we return the nme with only the first letter of suffix/prefix since it is the simplest form of representing a prefix/sufix and its very low probability than on a same two persons with same name and diffrent suffix(but same 1st letter of suffix) occurs.
* It returns the name without any change if the name doesn't have suffix/prefix.

# Unique Elements
* It extracts the list of all unique first and last names by using the unique() function.
* Now from all the unique names we only have the use for names having any sufix,so we extract the name having a suffix and all the unique first and last names are stored in a seperate list.

# Replacement ALgorithm
Input: strings name<br/>
Output: Replaced Name<br/>
* Firstly all the name are send to a function which first check if the name has a suffix or not.
* If the sufix is present than the name is sent to another function to check if the name is unique and can be replaced without a suffix or some other name is present with same name but different sufix.
* If the above case exists the name is not replaced and is unique.



# How to run the program:
`python main.py` <br/>

Tools Used: 
* python 3.6
* pandas module
* numpy module


# File Descriptions:

* suffixes.txt: contains list of suffixes 
* prefixes.txt: contains list of prefixes
* unique_first_suffix: contains list of unique first names that have suffix
* unique_last_suffix: contains list of unique last names that have suffix
* clean.py: clean the data by removing common prefix/sufix
* unique.py: helps in creating the list of unique first and last name with suffix
* replacement.py: replaces the name with suffix with suitable name
* main.py: implements the functionality of reading the file and performing deduplication
* Deduplication Problem - Sample Dataset.csv: input dataset provided by innovaccer. I have added few more entries to test my algorithm
* Output.csv: contains the output of the algorithm.
