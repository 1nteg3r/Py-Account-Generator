from faker import Faker
import random
import time
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Account generator")


def main():
    ask = input('How many account do you want to gen?: ')
    try:
        ask = int(ask)
    except:
        raise ValueError('Enter an integer')
    
    

    for i in range(ask):
        domains = ['@gmail.com' , '@yahoo.com' , '@hotmail.com' , '@outlook.com']

        fake = Faker()

        name = fake.name()
        name = name.replace(" ","")
        name = name.lower()
        password = fake.password()

        num = random.randint(0,1000)
        num = str(num)

        mail_pre = name
        mail_pre += num

        mail_check_url = mail_pre + random.choice(domains) + " : " + password + "\n"

        print(mail_check_url)
    save = input("Do you want the accounts to save to a .txt? [Y/N]")
    if save == "Y":
        f = open("accounts.txt", "a")
        f.write(mail_check_url)
        f.close()
        print("Generated accounts saved in accounts.txt!")

main()
print("Window will close in 10 seconds...")
time.sleep(10)
