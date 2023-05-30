import os
import requests
import random
os.system("git pull")
# clear terminal screen
os.system("clear")

# logo with fancy colors
def logo():
    print("""\033[1;92m
########  ##     ## ##     ## ########  ######## ########  
##     ## ##     ## ###   ### ##     ## ##       ##     ## 
##     ## ##     ## #### #### ##     ## ##       ##     ## 
##     ## ##     ## ## ### ## ########  ######   ########  
##     ## ##     ## ##     ## ##        ##       ##   ##   
##     ## ##     ## ##     ## ##        ##       ##    ##  
########   #######  ##     ## ##        ######## ##     ##
\033[1;32m--------------------------------------------------
[+] AUTHOR   :     HAMAYON KHAN
[+] GITHUB   :     HLS706
[+] CODE     :     RANDOM DUMP OPEN CODE
[+] VERSION  :     DUMPER-1
\033[1;32m--------------------------------------------------""")

def menu():
    print('[1] DUMP UID NEW \n[2] DUMP UID OLD \n[3] FB GROUP \n[4] EXIT TOOLS')

# main function
def HLS():
    tanya = input("[+] Choice: ")

    if tanya == "1":
        output = input("\n[+] Enter the name of the file: ")
        id = int(input("[+] Limit: "))
        random_numbers = ["100093" + str(random.randint(11111111111, 99999999999)) for i in range(id)]
        print ("[+] Total IDs:",len(random_numbers))

        with open(output, 'w') as file:
            for number in random_numbers:
                file.write(str(number) + '\n')
        print ("\n[+] Done...")
        print ("[+] IDs saved in:", output)

    elif tanya == "2":
        output = input("\n[+] Enter the name of the file: ")
        id = int(input("[+] Limit: "))
        random_numbers = ["100000" + str(random.randint(111111111, 999999999)) for i in range(id)]
        print ("[+] Total IDs:",len(random_numbers))

        with open(output, 'w') as file:
            for number in random_numbers:
                file.write(str(number) + '\n')
        print ("\n[+] Done...")
        print ("[+] IDs saved in:", output)

    elif tanya == "4":
        exit()

    elif tanya == "3":
        os.system('xdg-open  https://www.facebook.com/gsriyad11/') 
    else:
        exit()

# run the main function with logo and menu
logo()
menu()
HLS()
