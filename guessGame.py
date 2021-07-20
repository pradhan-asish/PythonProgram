import random
def guessNumGame():
    x = random.randint(1,20)
    print(str(x))
    print('You will be given 6 chance for guessing a number between 1 and 20')
    for i in range(1,6):
        print('Guess a number')
        try:
            y = int(input())
        except ValueError:
            print('invalid number')
        if x != y:
            print('Your guess is wrong!! Please choose once again')
        else:
            print('Your guess is right and number is '+ str(y) + ' number of attempt taken by you is ' + str(i))
            break;
    if (x != y):    
        print('Your guess is wrong and number is '+ str(x) )
    return ;

guessNumGame()                        
    
