# as long as the files being compared from are in the same folder as this file
# you can put the name of the file in the ' ' on lines 55 for the AD and 58 for the invoice
# if they are not in the same folder you wil have to put in the files full path

# the file name on line 34 should be changed if the name has been used before 
# if it is not then it will be added on to the end of the file with the same name

# this can be used for different columns as well
# just change the white text after "file." on lines 56 and 59
from collections import Counter
import pandas


def handleColumn(column):
    # converts all the names into strings so they can be converted to uppercase 
    # converted to uppercase so that theres no issue matching them due to case sensitvity
    for i in range(0,len(column)):
        column[i]=str(column[i])
        column[i]=column[i].upper()
    noduplicates={}
    # creates a dictionary of names since all dictionary entries must be unique
    # this prevents a name from matching later with itself and falsely appearing in
    # both the AD and invoice
    noduplicates=Counter(column)
    noduplicate_list=[]
    # adds the names to the list 
    for key,val in noduplicates.items():
        noduplicate_list.append(key)
    return noduplicate_list
def compare(dictionary, invoice, active_directory):
    # opens file to save output
    # out3 because I had a few minor mistakes in the first few outputs
    # mainly semantics errors but I worked them out
    with open('outTest.txt', 'w') as f:
        # print(word_dict, '\n\n', file=f) 
        nonMatch=[]
        # checks all items in the dictionary for a nonmatch, val = 1
        for key,val in dictionary.items():
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
def main():
    # imports the AD csv and pulls the display names into the variable 
    file = pandas.read_csv('AD-5-31-full.csv')
    displayname=list(file.displayname)
    active_directory_list=handleColumn(displayname)
    file = pandas.read_csv('detail_report.csv')
    usernames =list(file.Username)
    invoice_list=handleColumn(usernames)
    combined_list=[]
    combined_list+=invoice_list
    combined_list+=active_directory_list
    # uses the combined list to count each time a unique name was found in a dictionary
    word_dict = Counter(combined_list)
    compare(word_dict, invoice_list, active_directory_list)

if __name__ == "__main__":
    main()