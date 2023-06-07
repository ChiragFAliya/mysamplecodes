master_pwd = input("what is master password? ")

def view():
	with open("passwords.txt",'r') as f:
		for line in f.readlines():
			data = (line.rstrip())
			user,passw= data.split("|")
			print("user:",user,"| password:",passw)
 
def add():
	name =input("account name: ")
	pwd = input("password:")

	with open("passwords.txt","a") as f:
		f.write(name +"|" + pwd + '\n')





while True:
	mode = input("would you like to add or view passwords (view,add)?,press q to quit !").lower()
	if mode == "q":
		break
	if mode == "view":
		view()
	elif mode == "add":
		add()
	else:
		print("invalid mode! ")
		continue
