import helper
import time

print("Welcome to Dice-Off!")
print("--------------------")
rules = '''
    This game consists of multiple numbered rounds.
    In round n, your opponent Dr. Discombobulate rolls a n*6 sided die and you are shown the result.
    You will then have to predict if your collection of n 6-sided dice will give a higher or lower number than that result.
    If your correct (or the numbers are the same), you progress to the next round.
    How far can you make it??
'''
print(rules)


failed = False
round_num  = 1

# Game continues until you lose.
while not failed:
    print("--------------------")
    print(f"Round {round_num}:")
    # Dr Ds dice gets 6 more sides per round.
    dr_d_roll = helper.custom_dice_roll(round_num * 6)
    print(f'Dr. Discombobulate rolled a {dr_d_roll}')

    # User guesses a or b depending on prediction
    choice = input(f"""
You have {round_num} six-sided dice, do you think your roll will be:

    a) Higher
    b) Lower

    """)
    
    player_roll = 0
    rolls = 0

    # Repeats rolling dice multiple times based on round number.
    while rolls < round_num:
        player_roll += helper.dice_roll()
        rolls += 1
    
    print(f"You rolled a {player_roll}")

    # TODO: If you guessed correctly, go to next round
    # TODO: If you guessed incorrectly, end the game

    time.sleep(1)

print(f"You survived {round_num} rounds!")