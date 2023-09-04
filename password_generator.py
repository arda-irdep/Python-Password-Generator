# Python Password Generator

import string
import random
import pyperclip

lower_case_letters = string.ascii_lowercase
upper_case_letters = string.ascii_uppercase
numbers = string.digits
punctuation = string.punctuation

want_lower = input("Do you want lower case letters (y/n)?: ").lower()
want_upper = input("Do you want upper case letters (y/n)?: ").lower()
want_digits = input("Do you want numbers (y/n)?: ").lower()
want_puncts = input("Do you want punctuation (y/n)?: ").lower()

length_of_password = int(input("Please enter length of password: "))

passwd = ""

if want_lower == "y":
	passwd += lower_case_letters
elif want_lower == "n":
	pass
else:
	print("Please write (y) or (n)")

if want_upper == "y":
	passwd += upper_case_letters
elif want_upper == "n":
	pass
else:
	print("Please write (y) or (n)")

if want_digits == "y":
	passwd += numbers
elif want_digits == "n":
	pass
else:
	print("Please write (y) or (n)")

if want_puncts == "y":
	passwd += punctuation
elif want_puncts == "n":
	pass
else:
	print("Please write (y) or (n)")

random_pass = ''.join(random.sample(passwd, len(passwd)))

pyperclip.copy(random_pass[:length_of_password])
print("Password copied")