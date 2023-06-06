from collections import Counter
import pandas

# imports the AD csv and pulls the display names into the variable 
df = pandas.read_csv('AD-5-31-full.csv')
displayname=list(df.displayname)
# converts all the names into strings so they can be converted to uppercase 
# converted to uppercase so that theres no issue matching them due to case sensitvity
for i in range(0,len(displayname)):
    displayname[i]=str(displayname[i])
    displayname[i]=displayname[i].upper()
active_directory={}
# creates a dictionary of names since all dictionary entries must be unique
# this prevents a name from matching later with itself and falsely appearing in
# both the AD and invoice
active_directory=Counter(displayname)
active_directory_list=[]
# adds the names to the list 
for key,val in active_directory.items():
    active_directory_list.append(key)
# repeats above steps for the invoice 
df = pandas.read_csv('detail_report.csv')
usernames =list(df.Username)
for i in range(0,len(usernames)):
    usernames[i]=str(usernames[i])
    usernames[i]=usernames[i].upper()
invoice={}
invoice=Counter(usernames)
invoice_list=[]
for key,val in invoice.items():
    invoice_list.append(key)
# combines the 2 lists of names into one list 
combined_list=[]
combined_list+=invoice_list
combined_list+=active_directory_list
# uses the combined list to count each time a unique name was found in a dictionary
word_dict = Counter(combined_list)
# opens file to save output
# out3 because I had a few minor mistakes in the first few outputs
# mainly semantics errors but I worked them out
with open('out3.txt', 'w') as f:
    # print(word_dict, '\n\n', file=f) 
    nonMatch=[]
    # checks all items in the dictionary for a nonmatch, val = 1
    for key,val in word_dict.items():
        if(val==1):
            nonMatch.append(key)

    print("non matched names are: ", nonMatch , '\n\n', file=f)
    for item in nonMatch:
        # searches through the list of names that were not matched 
        # to see if it was in the invoice or AD
        if(item in invoice):
            print(item, "only found in invoice", file=f)
        elif(item in active_directory):
            print(item, "only found in AD", file=f)
        # saftey net to make sure no entries were missed
        else:
            print(item, "????", file=f)