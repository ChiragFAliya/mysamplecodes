import random

user_wins = 0
comouter_wins = 0 


options = ["rock" , "papper" , "scissors"]


whie True:
	user_input = input("type rock/papper/scissors or q to quit:").lower()
	if user_input == "q":
		break

	if user_input not in options:
		continue

	random_number = random.randint(0,2)
	# rock:0 , papper:1 , scissors:2 

	computer_pick = options(random_number)
	print("computer_picked", computer_pick +".")

	if user_input == "rock" and computer_pick == "scissors":
		print("you won")
		user_wins += 1

	if user_input == "papper" and computer_pick == "rock":
		print("you won")
		user_wins += 1

    if user_input == "scissors" and computer_pick == "papper":
		print("you won")
		user_wins += 1

	else:
		print("you lost")
		comouter_wins += 1



	print("you won", user_wins,"times")
	print("the computer won",comouter_wins,"times")
	print("good bye!")