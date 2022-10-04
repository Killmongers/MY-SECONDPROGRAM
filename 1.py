import random
a=random.randint(1,10)
print('I am thinking of the number between')
for i in range(1,5):
    x=int(input("take a guess:"))
    if x<a:
        print('your guess is to low')
    elif x>a:
        print('your guess is to high')
    else:
        break
if x==a:
    print('good job you guess my number in ' +str(i)+' guesses! ')
else:
    print('nope.The number i think of was '+str(a))  