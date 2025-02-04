#navigate to text file location
#Open File
#Read File contents
#Print to screen



import os
def read_file():

    os.chdir('/Users/sonte/PyQt5-Practice-')
    #print(file_location)

    #print(friends_list_file)
    friends_list_file = 'friendslist.txt'
    with open(friends_list_file, 'r') as f:
        contents = f.read()
        print(contents)
        
#read_file()