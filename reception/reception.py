Ordinary_list=[]
Vip_list =[]

#check username from guest list  
def registration_checker(name):

    guest_list_ordinary =open('odinary_list.txt', 'r')
    for guest in guest_list_ordinary:
        Ordinary_list.append(guest.strip())

    guest_list_vip =open('vip_list.txt', 'r')
    for guest in guest_list_vip:
        Vip_list.append(guest.strip())

    name =input("please enter guest name")

    if name ==0:
        print(" please enter a name ")
    else:
        guest_name=[g for g in Vip_list if name.lower() == g.lower()]
        ordinary_name=[g for g in Ordinary_list if name.lower() == g.lower()]
        if guest_name:
            print(guest_name[0], "on vip") 
        elif ordinary_name:
            print(ordinary_name[0],"on ordinary list")
        else:
            print("not a guest")


