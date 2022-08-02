import random
import math
print("Enter a number:")
y = math.floor(random.random()*30)
won = False
for i in range(1,10):
    Num1 = input()
    x = int(Num1)
    if x < y :
        if i < 9:
            print("the number is smaller than the required number")
            print("Number of guesses left :", 9 - i)
            print("Enter the number again :")
        elif i == 9:
            print("the number is smaller than the required number")
            print("Number of guesses left :", 9 - i)

    elif x > y and i <= 8:
        if i < 9:
            print("the number is greater than the reqiured number")
            print("Number of guesses left :", 9 - i)
            print("Enter the number again :")
        elif i == 9:
            print("the number is greater than the reqiured number")
            print("Number of guesses left :", 9 - i)
    elif x == y:
        print("congrats you won the game")
        won = True
        break
if (won == False):
    print("GAME OVER!")

# while x <= 9:
#     print(x)
#     x = x + 1
# else:
#     print("no")
#     x = 9
#
#     while x and i in Num1:
#     print("the Number is less than the required number")
#     if x < 9 and int(i) < 18:
#         break
#     else:
#         print("the number is greater than the required number")
#     x = x + 1
#     i = i
# else:
#     print("Congrats you won the game")
