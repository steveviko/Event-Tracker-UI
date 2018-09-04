import os

# read from file
def read_file(file_to_read):
    # define empty list   
    names = []
    # open file and read the content in a list
    with open('file_to_read', 'r') as vip:  
     names = [current_name.rstrip() for current_name in vip.readlines()]
    
    return names

    # prompt user for their name
def get_user_input():
    names = read_file('vip_list.txt')
    username = input('Username: ')
    new_name = username   
    
    print(new_name)

    if username in names:
        print('On vip guest lists')
    else:
        print('on Odinary lists')
    return ''

get_user_input()