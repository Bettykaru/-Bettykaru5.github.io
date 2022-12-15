# Kibo FPWP Final Project
# Put your final project code in this file for submission
# Add the names of the authors, a brief description, and link to your video in the file called 'readme.md'
# Then, you can remove these instruction comments
# Then, you can remove these instruction comments 
import random
import string
import termcolor
import time
previous_passwords = []
#passcode function
def passcode(length): 
  lower = string.ascii_lowercase
  upper = string.ascii_uppercase
  num = string.digits
  symbols = string.punctuation
  combination = lower + upper + num + symbols
  password = "".join(random.sample(combination,length))
  previous_passwords.append(password)
  print()
  print("Generating password..............")
  time.sleep(3)
  print()
  print("Here's your password coloured blue: ")
  print()
  termcolor.cprint(password,'blue')
  
#Actual programme

termcolor.cprint("     Welcome to   SQUAD - 6 ",'cyan')
print()
termcolor.cprint("      Password    generator    app",'cyan')
print()
time.sleep(1)
termcolor.cprint("Hello ,Let's sign you in to create a strong and secure password",'yellow')
print()
time.sleep(3)
termcolor.cprint("       Sign   in   with   a    Username",'magenta')
print()

prompt = input("   USERNAME :  ")
print()
print("Nice to meet you"  ,  prompt  ,  "in just a few steps ,we shall help you generate an unbreakable  password ,with extra features to allow our user to build or customize according to their preferences ")
print()
time.sleep(2)
print()
print("So  much easier,",prompt)
termcolor.cprint(" I'll help you generate a password of any length greater than 5 characters",'blue') 
length = 0
while True:
 length = input("\nEnter the number of characters your password should have : ")
 
 if not length.isdecimal(): 
  print("\nYou have to enter a number") 
  continue
 length = int(length)
 if length <= 4:
  print()
  print("Sorry ,input 5+ characters  or  'quit' to exit")
  continue
 if length > 39: 
  length = input("A password can't be that long\nEnter a number less than 39.")
  continue
 if length == 6:
  print()
  print()
  termcolor.cprint("Password character strength is fair",'cyan') 

 if length == 5:
  print()
  print()
  termcolor.cprint("Password character strength is fair",'cyan')

 if length == 7  :
  print()
  print()
  termcolor.cprint("Password character strength is fair",'cyan')
  
 if length >= 8 and length < 21:
  print()
  termcolor.cprint("Password character strength is good",'green')
  print()
 if length >= 21 and length <= 39:
  print()
  termcolor.cprint("Great,Password  character Strength is  strong ",'green')
  print()
  print()
  if length == 'quit' or 'Quit':
    termcolor.cprint("Exitting App ",'red')
    termcolor.cprint("Thank you for using this app",'yellow')
    break
#preparing combinations   
 if length > 4 and length < 39 : 
  passcode(length)
  print()
  termcolor.cprint("Hi,Would you like another password? ")
  print()
  termcolor.cprint("1. Yes",'yellow')
  termcolor.cprint("2. No ",'yellow')
  print()
  num = input("Please choose an option: ")
  if num == '1':
   termcolor.cprint(" Kindly, Enter",'green')
   print("        1 . Generate another password")
   termcolor.cprint("        2 . Exit ",'magenta')
   print("        3 . Customize your password")
   print()
   termcolor.cprint("Hello",'blue')
   termcolor.cprint(prompt,'blue')
   menu =int(input("Kindly input selection here: "))
   print()
   print()
  if num == '2':
   termcolor.cprint("Exitting app",'red')
   print()
   termcolor.cprint("Thank you for using this app")
   break


  if menu == 1 :
   termcolor.cprint("Fantastic,Generate another one-time password  ",'cyan')
   print()
 elif length == " ":
  continue
  if menu == 3:
   print("Welcome back",prompt,"set your preferred password")
   print()
   user = input("New Password: ")
   print()

   print("Heres's your New customised password:")
   termcolor.cprint(user,'blue')
   print()
   print()  
   if len(user) <= 4  :
    termcolor.cprint("oops,Password can not be created",'red')
    print()
    user = input("create another password between 5 - 39( Try mixing symbol,letters ,number or other characters): ")
    print()
   if len(user) >= 6 :
    print()
    termcolor.cprint("Password strength strong enough",'green')
    print()
    termcolor.cprint("Congratulations you have succesfully create your password : "+user,'blue')
    print()
    termcolor.cprint("Thank you for using this app",'yellow')
   elif len(user) < 39 :
    print()
    termcolor.cprint("Password strength strong enough",'green')
    print()
    termcolor.cprint("Congratulations you have succesfully create your password : "+user,'blue')
    print()
    termcolor.cprint("Thank you for using this app",'yellow')
    break
 
  
   if menu == 2:
    time.sleep(2)
    termcolor.cprint("You have successfully exit app: ",'green')
    print()
    termcolor.cprint("Thanks for Using this app",'yellow')
    break
  else: 
   termcolor.cprint("Sorry,wrong input to continue please Enter",'red')
   print()
   termcolor.cprint("1. To generate password",'yellow')
   print()
   menu = int(input("Please input selection here: "))