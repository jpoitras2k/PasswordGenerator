''' Developer: Jason Poitras
Generate a random password of a chosen length.'''

from random import *
import string

# string.ascii_letters is upper and lower letters from import string
#string.digits is '0-9'
characters =string.ascii_letters + string.digits

pw_length = int(input("How many characters would you like for your password? "))

#joins characters for the number of characters in password entered from random import
password = "".join(choice(characters) for x in range(pw_length))

#prints password
print (password)