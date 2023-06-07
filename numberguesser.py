import random

top_of_range = input("type a number: ")
if top_of_range.isdigit():
	top_of_range = int(top_of_range)
	

	if top_of_range <= 0:
		print("please type a number bigger than 0")
		quit()
else:
	print("type a number next time, mah boy!")
	quit()


random_number = random.randrange(0,top_of_range)
guesses =0
while True:
	guesses += 1
	user_guess1 = input("type a number: ")
	if user_guess1.isdigit():
		user_guess1 = int(user_guess1)
	else:
		print("print type a number nest time.")

	if user_guess1 == random_number:
		print("you go it!")
		break
	elif user_guess1 > random_number:
		print("you are above the number!")
	else:
		print("you are below the number!")

print("you got the right number in" ,(guesses),"guesses.")