import random
import time

player = cpu = 0

print('Three points = win the game!')

answers = ['Rock', 'Paper', 'Scissors']
wins = [('Rock', 'Scissors'), ('Scissors', 'Paper'), ('Paper', 'Rock')]

while cpu < 3 > player:
    cpu_pick = random.choice(answers)
    player_pick = input('\nRock, paper or scissors: ').title()
    if player_pick in answers:
        time.sleep(0.5)
        match = (player_pick, cpu_pick)

        print(f"Player: {player_pick}!")
        print(f"CPU: {cpu_pick}!")

        if match in wins:
            player += 1
            print('Player won and gets a point!')
        elif player_pick == cpu_pick:
            print('Tie! No points!')
        else:
            cpu += 1
            print('Player lost! CPU gets a point.')
        print(f'CPU: {cpu}. Player: {player}!')
    else:
        print('Invalid pick! New round.')

print('Player wins the game!' if player > cpu else 'CPU wins the game!')
