import random
secret =random.randint(1,20)

guess =0
attemps=0

print("guess the screct number (1 to 20)")
print('')

while guess!=secret:
    guess=int(input(" enter the number :  "))
    attemps += 1

    if guess==secret:
        print("done",attemps)
    elif(guess>secret):
        print('number is too high')
    else:
        print("number is too LoW.")