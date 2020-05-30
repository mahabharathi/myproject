import random

def run_guess_game(guess,answer):
    if 0 < guess < 11:
        if guess ==answer:
            print('You are a genius!!!')
            return True
    else:
        print('heybozo, I said 1~10')

if __name__=='__main__':
    answer =random.randint(1,10)
    while(True):
        try:
            guess=int(input('guess a number 1~10: '))
            if (run_guess_game(guess)):
                break
        except ValueError:
            print('Please enter a number')
            continue