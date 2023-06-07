import random


MAX_LINES = 5
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {"A":2,"b":4,"c":6,"d":8}

symbol_value = {"A":2,"b":4,"c":3,"d":2}



def check_winnings(columns,lines,bet,values):
	winnings = 0
	winning_lines = []
	for line in range(lines):
		symbol = columns[0][line]
		for column in columns:
			symbol_to_check = column[line]
			if symbol != symbol_to_check:
				break

		else:
			winnings += values[symbol] * bet
			winning_lines.append(line+1)

	return winnings, winning_lines





def get_slot_machine_spin(rows,cols,symbols):
	all_symbols = []
	for symbol,symbol_count in symbols.items():
		for _ in range(symbol_count):
			all_symbols.append(symbol)

	columns = []
	for _ in range(cols):
		columns = []
		current_symbols = all_symbols[:]
		for _ in range(rows):
			value = random.choice(current_symbols)
			current_symbols.remove(value)
			column.append(value)
		columns.append(column)

	return columns

def print_slot_machine(columns):
	for row in range(len(columns[0])):
		for i,column in enumerate(columns):
			if i != len(columns) -1:
				print(column[row],end=" | ")
			else:
				print(column[row],end="")


		print()


def deposit():
	while True:
		amount = input("how much do you want to deposit? ")
		if amount.isdigit():
			amount = int(amount)
			if amount > 0:
				return amount
			else:
				print("please enter greater than 0")
		else:
			print("please enter a number")

def get_bet():
	while True:
		amount = input("what would you lioke to bet on each line ? ")
		if amount.isdigit():
			amount = int(amount)
			if MIN_BET <= amount <= MAX_BET:
				break
			else:
				print(f"amount must be between {MIN_BET} - {MAX_BET}.")
		else:
			print("please enter a number")
	return amount


def get_number_of_lines():
	while True:
		lines = input("enter the number of lines to bet on (1-"+ str(MAX_LINES) + ")? ")
		if lines.isdigit():
			amount = int(lines)
			if 1 <= lines <= MAX_LINES:
				return amount
			else:
				print("enter the valid number of lines ! ")
		else:
			print("please enter a number")

def spin(balance):
	lines = get_number_of_lines()
	while True:
		bet = get_bet()
		total_bet = bet * lines

		if total_bet > balance:
			print(f"you do not have enought balance to bet, your current balance is {balance}")
		else:

	print(f"you are betting {bet} on {lines} lines.total bet is equal to: {total_bet}")
	print(balance,lines)


slots = get_slot_machine_spin(ROWS.COLS,symbol_count)
print_slot_machine(slots)
winnings, winning_lines  = check_winnings(slots,lines,bet,symbol_value)
print(f"you won {winnings}).")
print(f"you won on lines:",*winning_lines)
return winnings - total_bet


def main():
	balance = deposit()
	while True:
		print(f"xurrent balance is {balance}")
		answer = input("press enter to play (q to quit).")
		if spin == "q":
			break
		balance += spin(balance)

	print(f"you left with {balance}")



main()