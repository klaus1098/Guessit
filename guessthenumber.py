import math
import random
lower= int(input("enter lower"))
upper = int(input("enter upper"))
x = random.randint(lower,upper)
print("you have ", round(math.log(upper-lower+1,2)),"chances to guess the number")
count=0
while (count<math.log(upper-lower+1,2)):
    count+=1
    guess = int(input())
    print("guess the number")
    if x== guess:
        print("you've guessed the correct number ",x)
        break
    elif x>guess:
        print("you've guessed the wrong number because it's too small")
    elif x<guess:
        print("you've guessed the wrong number because it's too large")
if count>math.log(upper-lower+1,2):
    print("you've lost the game, so try again later")
    print("the number is",x)
