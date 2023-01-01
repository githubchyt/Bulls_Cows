"""
project_2_lchy.py: 2nd project in Engeto Online Python Academy

author: Lucie Chytilová
email: studyroomchy@gmail.com
discord: Lucie Ch.#8282
"""

import time
import function_bull_cow as fbc

SEP = "------------------------------------------------------------------"

game = 'Y'
stats = dict()
count_play = 0

print(f"Hi there!")

while game.upper() == 'Y':
    count_play += 1
    
    # create secreate number
    secreat_number = fbc.secreat_nbr()
    
    # you can show generated secrate number
    # print("Secret number is: ", secreat_number)
    
    print(SEP)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(SEP) 
    print("Enter a number (max 4 digits, not start 0, all digits unique):")
    print("If you want to quit enter 'Q' instead of the number.")
    print(SEP)
        
    start = time.time()
    count_guess = 0
    guess_number = ''  
    
    while guess_number != secreat_number and guess_number.upper() != 'Q':
        guess_number = input(">>> ")
        
        if guess_number.upper() != 'Q':
            
            # check if guess number has correct format
            if fbc.check_number(guess_number):    
                count_guess +=1
                
                # compare guess number and generated secrate number
                result = fbc.eval_bull_cow(guess_number, secreat_number)
                
                # payer guesses secrate number
                if result[0].split()[0] == '4': 
                    endt = time.time()
                    
                    stats[count_play]=[count_guess, time.strftime("%H:%M:%S", 
                    time.gmtime(endt-start)), fbc.eval_text(count_guess)]
       
                    print(f"Correct, you've guessed the right number in "
                        f"{count_guess} guesses!")
                    
                    print(f"That's {fbc.eval_text(count_guess)}!")
                    print(SEP)
                    
                    game = input("If you want to play new next game,"
                        "press 'Y': ")

                # payer doesn't guess secrate number                  
                else:
                    print(', '.join(result))
                    print(SEP)
                    
            else:
                print(f"Your number {guess_number} has wrong format.")
                print(SEP)
        else:    
            print(f"Secret number is: {secreat_number}")
            print(f"You lose your {count_play}. game!")
            game = 'N'
   
# writes out game statistics
if len(stats) != 0:     
    print(f"\n{'-'*90}\n|{'YOUR SCORE':^88}|\n{'-'*90}")
    
    print(f"|{'Game Nbr.':^15}|{'Nbr. of Guesess':^15}|{'Game Time':^15}|"
        f"{'Evaluation':^40}|\n{'-'*90}")
   
    for key, values in stats.items():
        count_guess, time, evaluation = values
        
        print(f"|{key:^15}|{count_guess:^15}|{time:^15}|"
            f"{'''That's '''+ evaluation:^40}|")

    print('-'*90)
       
     
