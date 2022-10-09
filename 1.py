import random
a=random.randint(1,10)
print('I am thinking of the number between')
for i in range(1,5):
    x=int(input(" Guess number between:"))
    if x<a:
        print('your guess is to low')
    elif x>a:
        print('your guess is to high')
    else:
        break
if x==a:
    print(f'good job you guess my number in {i} guesses! ')
else:
    print(f'nope.The number i think of was :{a}')  
