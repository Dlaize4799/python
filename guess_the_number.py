import random 
from sys import exit

num1 = random.randint(1,30)

print()
print("I'm thinking of a number between 1 and 30")
print()
print('Can you guess the number? I can give hints.')


for j in range(5):
    num2=input('>')
    num2=int(num2)
    if num1==num2:
        print()
        print("You've succesfully guessed the number in " + str(j+1)+'guess(es)')
        exit()
    elif (num2>30 or num2<1):
        print("it's not even in the range")
        continue
    elif num2>num1:
        print()
        print("You've guessed too high")
        continue
    elif num2<num1:
        print()
        print("You've guessed too low")
        continue
print()   
print("You have used up all your chances.",'GAME OVER!!',sep="\n")   
print('The number was '+ str(num1))
