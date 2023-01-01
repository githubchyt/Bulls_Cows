"""
function_bull_cow.py: Functions for 2nd project in Engeto

author: Lucie Chytilová
email: studyroomchy@gmail.com
discord: Lucie Ch.#8282
"""

from random import sample as rd

def secreat_nbr () -> str:
    """
    Program generates secret four-digit number.
    Number has to be unique and doesn't start zero.
    """

    number = '0'
    
    while number[0] == '0':
        number = "".join(map(str, rd(range(0, 10), k=4)))
    
    return number


def check_number (number: str) -> bool:
    """
    Check if string is number with these conditions:
     - nbr has 4 digits
     - nbr doesn't contain duplicity
     - nbr doesn't start zero
    """
    
    return (len(number) == 4 and len(set(number)) == 4 and 
            number[0] != '0' and number.isdigit())


def eval_bull_cow (nbr1: str, nbr2: str) -> tuple:
    """
    Function compares two string for every position and
    writes out count of bull/bulls or cow/cows.
    
    Bull = value and position are same for both string
    Cow = value is in 2nd string but another position
    
    Example:
    nbr1 = '2598'
    nbr2 = '5092'
    
    Result: ('1 bull', '2 cows')
    bull = 1 (for '9')
    cow = 2 (for '2' and '5')
    
    """

    score = dict(bull = 0, cow = 0)
    
    for i in range(len(nbr1)):
        if nbr1[i] == nbr2[i]:
            score['bull'] += 1
        else:
            if nbr1[i] in nbr2:
                score['cow'] += 1
    
    if score.get('bull') == 1 and score.get('cow') == 1:
        text = ('bull', 'cow')
    elif score.get('bull') == 1 and score.get('cow') > 1:
        text = ('bull', 'cows')
    elif score.get('bull') > 1 and score.get('cow') == 1:
        text = ('bulls', 'cow')
    else:
        text = ('bulls', 'cows')
    
    return f"{score.get('bull')} {text[0]}", f"{score.get('cow')} {text[1]}"


def eval_text (count: int) -> str:
    """
    Functions returns an evaluation based on the number of guesses.
    """

    if count in range(1,4):
        text = 'amazing'
    elif count in range (4,8):
        text = 'average'
    elif count in range (8,12):
        text = 'not so bad'
    else:
        text = 'bad luck. Better luck next time'
    return text

