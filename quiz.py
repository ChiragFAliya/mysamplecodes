print("welcome to my quiz game!")

while True:
    playing = input("do you want to play? (yes/no) ").lower()
    if playing == "no":
        quit()
    elif playing == "yes":
        print("okay! let's play :)")
        break
    else:
        print("invalid input, please enter 'yes' or 'no'")

score = 0
answer = input("do you know the national animal of India? ").lower()
if answer == "tiger":
    print("correct")
    score += 1
else:
    print("your answer is wrong!") 
    
  
answer = input("do you know the national flag of India? ").lower()
if answer == "tricolor":
    print("correct")
    score += 1
else:
    print("your answer is wrong!") 
    
 
answer = input("do you know the national bird of India? ").lower()
if answer == "peacock":
    print("correct")
    score += 1
else:
    print("your answer is wrong!") 
    

print("you got " + str(score) + " answers correct! ")
print("you got " + str((score/3)*100) + " % ")
