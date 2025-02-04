#navigate to text file location
#Open File
#Write to file 
#Print to screen



import os
def write_file():

    os.chdir('/Users/sonte/PyQt5-Practice-')
    #print(file_location)

    #print(friends_list_file)
    friends_list_file = 'friendslist.txt'
    with open(friends_list_file, 'a') as f:
        friend_added = input('Add Friend')
        f.write(friend_added +'\n')
        print('Friend Added')
        
#write_file()