#This script performs some simple tests on the UserAccount class.
from UserAccount import UserAccount

#Three things are missing from the line below - fill them in
username='lyne18-meet'
password= 'I love icecream'
secret= ' I am affraid of closed places'
my_user=UserAccount(username,password,secret)


#Call the print_secret method (function) - it takes one input - a guess for the password.
my_user.print_secret('i hate hotdogs')
#Use the wrong password as input here


#Use the right password here
my_user.print_secret(password)
