from faker import Faker
import random
import time
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Account generator") #sets the console name


def main():
    ask = input('How many account do you want to gen?: ') #asks for user input
    try:
        ask = int(ask)
    except:
        raise ValueError('Enter a valid integer') #checks for valid user input
    
    

    for i in range(ask):
        domains = ['@gmail.com' , '@yahoo.com' , '@hotmail.com' , '@outlook.com'] #setting a valid list array of domains to grab(you can set it to grab from a certain one, on its own its set to random)

        fake = Faker()
        
        #appending variables 
        name = fake.name() 
        name = name.replace(" ","")
        name = name.lower()
        password = fake.password()

        num = random.randint(0,1000)
        num = str(num)

        mail_pre = name
        mail_pre += num

        mail_check_url = mail_pre + random.choice(domains) + " : " + password + "\n" # this is where the generating is happening, \n is added to avoid collision of lines in the .txt

        print(mail_check_url)
    save = input("Do you want the accounts to save to a .txt? [Y/N]") # saves the accounts if prompted to a new file
    if save == "Y":
        f = open("accounts.txt", "a")
        f.write(mail_check_url)
        f.close()
        print("Generated accounts saved in accounts.txt!")

main()
print("Window will close in 10 seconds...") # added this so the user is aware and can see the account information if they decided not to save it to the .txt file
time.sleep(10)
