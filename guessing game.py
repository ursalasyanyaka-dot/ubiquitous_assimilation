
print("Hello this is a number guessing game, are you ready!")
#random is used to import random characters
import random
#calling and putting a limit to the range
num_list = random.randint(0,21)


#the loop will help in running it until the condition is satisfied
i = 1
for i in range(5):
    
    num = int(input("Enter guess the number: "))
    if num < num_list:
        print("Higher: ")
    elif num > num_list:
        print("lower")
    else:
        print("You got it!!!!!")
        break
else:
    print("sorry You didn't get it, maybe next time")
