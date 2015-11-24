import random

trial=0
trial_num=3

#Oct 13-made this program to work
#Next?: Find out how to catch error
def guess():
    return eval(raw_input("What is your guess?"))== (random.randint(0,10))


def sec_guess(ans):
    return eval(raw_input("What is your guess?"))== ans


def checkguess():
    global trial
    while (trial < trial_num):
        if not(guess()):
            print "The number is incorrect. Try again"
            trial += 1
        else:
            print "Congrats you have guessed the right answer"
            quit()
    
def loopguess():
    global trial 
    while not(guess()):
        print "The number is incorrect. Try again"
    print "Congrats you have guessed the right answer"
    quit()


def main():
    global trial
    print "Hello there! What is your name?"
    name=raw_input()
    print "Hello, "+name+"! ____Some Super Fancy Phrase_______. GOOD LUCK!"
    global trial_num
    secondoption=(random.randint(0,10))
    sec_ans=random.randint(0,10)
    checkguess()
    second_try=raw_input( "Have you realized something abnormal yet?")
    if(second_try=="Yes"):
        print "Good you have spot the trap, Do you still wanna play then?"
        if (raw_input()=='No'):
            print "Sorry to waste your time, but I still hope that you enjoyed this little program lol"
            quit()
        else:
            loopguess()
    else:               #Second_try is "NO"
        loopguess()
main()
 
