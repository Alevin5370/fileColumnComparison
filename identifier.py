from collections import Counter
import pandas, os


def handleColumn(column):
    for i in range(0,len(column)):
        column[i]=str(column[i])
        column[i]=column[i].upper()
        column[i]=column[i].lstrip('{')
        column[i]=column[i].rstrip('}"')
    noduplicates={}
    noduplicates=Counter(column)
    noduplicate_list=[]
    for key,val in noduplicates.items():
        noduplicate_list.append(key)
    
    return noduplicate_list

def main():
    directory = 'activity_logs'
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        # print(file)
        if os.path.isfile(filepath):
            openfile = pandas.read_csv(filepath)
            application=list(openfile.APPLICATION)
            application_list=handleColumn(application)
            SOURCELog=list(openfile.SOURCE_LOG)
            SOURCELOG_list=handleColumn(SOURCELog)
            cleanlist=[]
            for part in SOURCELOG_list:
                splitted=part.split("|")
                temp=''
                for i in range(0, len(splitted)):
                    section=splitted[i]
                    if "DECISION" in section:
                        temp+=section
                        temp+='|'
                    elif "VERSION" in section:
                        temp+=section
                        temp+='|'
                    elif "STATUS_CODE" in section:
                        temp+=section
                        temp+='|'
                    elif "HOST" in section:
                        temp+=section
                        temp+='|'
                    elif "URI" in section:
                        temp+=section
                        temp+='|'
                if temp != '':
                    cleanlist.append(temp)
                else:
                    cleanlist.append("N/A")
            with open('Hostnames3.txt', 'a') as f:
                print(filepath, file=f)
                for item, piece in zip(application_list, cleanlist):    
                    print(item, "|", piece, file=f)
            

if __name__ == "__main__":
    main()