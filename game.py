import random
import math
print("Enter a number:")
y = math.floor(random.random()*30)
won = False
for i in range(1, 10):
    Num1 = input()
    x = int(Num1)
    if x < y:
        print("the number is smaller than the reqiured number")
        print("Number of guesses left :", 9 - i)
        if i < 9:
            print("Enter the number again :")
    elif x > y and i <= 8:
        print("the number is greater than the required number")
        print("Number of guesses left :", 9 - i)
        if i < 9:
            print("Enter the number again :")
    elif x == y:
        print("congrats you won the game")
        won = True
        break
if won is False:
    print("GAME OVER!")
