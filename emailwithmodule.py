# # a-z
# # 0-9
# # . _ 1 time
# # . 2,3
# import re
# email_condition= "^[a-z]+[/._]?[a-z 0-9]+[@]/w+[.]/w{2,3}$"
# user_email=input("enter your email : ")

# if re.search(email_condition,user_email):
# 	print("right email ")
# else:
# 	print("wrong email ")
	

import re

email_condition = r"^[a-z]+[._]?[a-z0-9]+@[a-z0-9]+\.[a-z]{2,3}$"

user_email = input("Enter your email: ")

if re.search(email_condition, user_email):
    print("Valid email.")
else:
    print("Invalid email.")
