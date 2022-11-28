import sys
import os
from time import sleep

def tmux():
      print("\033[1;30;1mTermux is a Android tool of linux environment")
      
t = "\033[1;32;1mDark Tools \n"
print(t.center(82))
while True:
    name = input("\033[1;33;1mWhat is your name ?  :   ")
    if name == "":
        print("Name cannot be blank")
    else:
        break
os.system("clear")
c = "\033[1;30;1mWelcome to Termux \n"
print(c.center(82))
print("\033[1;31;1m[1]\033[1;32;1m About")
print("\033[1;31;1m[2]\033[1;32;1m Exit \n \n")

choice = int(input("\033[1;33;1m[*] \033[1;34;1mChoose   :   "))
if choice == "":
    print("It cannot be blank")
elif choice == 2:
    exit()
    
#funtion defined in python

text = f"\n\033[1;36;1mHello   {name} ...\nWelcome to DarkTools !\n\n\033[1;37;1mAuthor  \033[1;32;1m: \033[1;33;1mSarthak Singh \n\033[1;37;1mWebsite \033[1;32;1m: \033[1;33;1msarthaksinghcoder.unaux.com \n\033[1;37;1mVersion \033[1;32;1m: \033[1;37;1m3.9.7\nTotal   \033[1;32;1m: \033[1;33;1m0 tool & no update\n\n\033[1;34;1mThanks for using this program ^_^ . \nPlease visit my website and explore there.\n\n"

text2 = "\033[1;31;1m___________________________________________ \n \n"
for letter in text:
    sleep(0.08)
    sys.stdout.write(letter)
    sys.stdout.flush()
    
for letter in text2:
    sleep(0.08)
    sys.stdout.write(letter)
    sys.stdout.flush()
