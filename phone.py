import sys
import os
from time import sleep
import phonenumbers
from phonenumbers import geocoder, carrier,timezone

os.system("clear")
a = "\033[1;31;1mFind The Location With Phonenumbers \n \n"
print(a.center(60))

print("\033[1;30;1m___________________________\n ")
t = "\033[1;33;1mEnter your number with country code.\n\n\033[1;36;1mEg... For India Format is like this : -\n\tnumber = +91your number\n"

for letter in t:
    sleep(0.08)
    sys.stdout.write(letter)
    sys.stdout.flush()
    
print("\033[1;30;1m___________________________\n")
#writing finished
while True:
    try :
        number = input("\033[1;32;1mEnter your number : -   ")
        phone = phonenumbers.parse(number)
        break
    except Exception as e:
        print(e)
      
country = geocoder.description_for_number(phone, "en")
SIMcard = carrier.name_for_number(phone, "en")
timeZone = timezone.time_zones_for_number(phone)
print("\n\033[1;34;1mThe Country name is : - " , country)
print("\033[1;35;1mThe SIM card is : -  " , SIMcard)
print("\033[1;39;1mThe  TimeZone is  : - " , timeZone)

t = "\n\033[1;33;1mThanks for using this program ^_^. \n " 

for s in t:
    sleep(0.08)
    sys.stdout.write(s)
    sys.stdout.flush()
