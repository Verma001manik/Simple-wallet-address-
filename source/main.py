import string 
import random,secrets
from threading import Timer
from getpass_asterisk.getpass_asterisk import getpass_asterisk
import json 
filename = "./users.json"


# user_input = ''
def login_register():
    
    print("Welcome to the Chain ")
    print("[0] : Login " )
    print("[1] : Register" )
    login_register.user_input = int(input("Chose Any One "))
    if login_register.user_input == 1:
        register()
    else:
        login()
        exit = False
        # checking what user has chosen
        while login.login_choice != 2:
            print("[0] : Wallet Address")
            print("[1] : Check Balance")
            print("[2] : Exit")
            print("[3] : All Usernames")
            print("[4] : Send Money")
            
            login.login_choice = int(input("Choose Any Operation "))
            
            if login.login_choice == 1:
                 
                print(f'Your Main Balance is ${register.item_data["amount"]} \n')
            elif login.login_choice == 0:
                print("Your wallet address is  :\n")
                with open (filename,"r") as f :
                    temp = json.load(f)
            # wallet address sent when using for loop used in login function 
                print(login.walletaddress)
            elif login.login_choice == 3:
                print("All the Usernames are : \n")
                with open (filename , "r") as f :
                    temp = json.load(f)
                for item in temp:
                    if item['username'] != "name":
                        print(item['username'])
                        
            elif login.login_choice ==4 :
                reciever_username = input("Enter Username to Send money\n")
                print("Checking if the user Exists\n")
                with open (filename, "r") as f :
                    temp = json.load(f)
                for key in temp :
                    if reciever_username  in key["username"]:
                        print("HURRAY!! We found the user\n")
                        send_amount = int(input("Enter the amount\n"))
                        print(register.item_data["amount"])
                            
                        

                    
                        
                        
                                

      
            
        print("Session Expired \n")
        t = Timer(3,login_register)
        t.start()



def register():
    register.item_data = {}
    with open (filename,"r") as f :
        temp = json.load(f)
    
    register.item_data["username"] = input("enter username : \n")
    
    for item in temp:
        if register.item_data["username"] in item["username"]:
            print("Choose a Unique Username\n")
            register()
    
    if register.item_data["username"] == '':
        print("Dont leave this Empty")
        register()
    password_matched = False 
    
    while password_matched == False:
        
        register.item_data["password"] = getpass_asterisk('Password:')
        if len(register.item_data["password"]) < 6 :
            print("Password should atleast contain 6 Characters")
            password_matched = False
            register.item_data["password"] = getpass_asterisk('Password:')
            
        if register.item_data["password"] =="qwertyu" or register.item_data["password"] == "123456789" or register.item_data["password"]  == "password":
            print("Please Chose a Strong password\n")
            password_matched = False
            # register.item_data["password"] = getpass_asterisk('Password: ')
            
        
            
        else:
            
          
            
            
            
            
            
            # register.item_data["password"] = getpass_asterisk('Password:')
            re_password = getpass_asterisk('Re-enter Password :')
            if register.item_data["password"] == register.item_data["username"]:
                print("Username And Password cannot be Similar")
                password_matched = False
            elif register.item_data["password"] == re_password:
                print("Creating Your wallet address\n")
                password_matched = True
                N= random.randint(27,30)
                wallet = "".join(secrets.choice(string.ascii_lowercase + string.digits)for i in range(N))
            
                register.item_data["walletaddress"] = f"0x{wallet}"
                print(f"Your wallet address is {register.item_data['walletaddress']}\n")
                register.item_data['amount'] = 1000
                
                
                temp.append(register.item_data)
                with open ( filename, "w") as f :
                    json.dump(temp,f,indent=4)
                        
            
                print("Login to Explore \n")
                ti = Timer(3,login_register)
                ti.start()
            else:
                print("Passwords Do Not Match, Try Again ")
                password_matched = False
            
        
        

        

    
    
    # user selected login option 

def login():
    
    
    # if login_register.user_input == 0:
        login.login_username = input("Enter username : \n")
        if login.login_username == '':
            print("You cannot leave that empty")
            login()
        
        with open (filename , "r") as f :
            temp = json.load(f)
            
        
        for item in temp:
            if login.login_username in item["username"]:
                
                login.walletaddress = item["walletaddress"]
                # print(walletadress)
                
                password_entered = False
                
                while password_entered  == False:
                    login.login_password = getpass_asterisk("Password :\n")
                    if login.login_password == "":
                        print("Pleasae Enter Your Password")
                        login.login_password = getpass_asterisk("Password :\n")
                
                    else:
                        for item  in temp:
                            if login.login_password in item["password"]:
                                password_entered = True
                              
                print(f"Welcome {login.login_username }\n")
        
                print("[0] : Wallet Address")
                print("[1] : Check Balance")
                print("[2] : Exit")
                print("[3] : All Usernames ")
                print("[4] : Send Money")
                 
                
                login.login_choice = int(input("Choose Any Operation "))            
                            
                       
                
        # else:
        #     print("User does not Exist \n")
                # print("Please Register\n")
                # t = Timer(3,login_register)
                # t.start()  
def transfer_money():
    
    pass



login_register()

