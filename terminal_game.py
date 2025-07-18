# Welcome to the Terminal Game!
# This is a simple text-based game where you can explore different paths and make choices.

import random

health = 10
alive = True

print("Welcome to the Looping Adventure!")
print("You wake up in a mysterious forest with paths leading in different directions.")
print(f'Your Health: {health} HP')

while alive:
    print("Choose a direction to explore:")
    print("1. Go north")
    print("2. Go south")   
    print("3. Go east")
    print("4. Go west")
    print("5. Exit the game")

    choice = input(">> ")

    if choice == '5':
        print("Thanks for playing! Goodbye!")
        break

    health -= 1

    outcome = random.choice([
        'You found a healing herb!',
        'You encountered a wild beast!',
        'You discovered a hidden treasure!',
        'You fell into a trap!'
    ])

    if outcome == 'You found a healing herb!':
        gain = random.randint(1, 5)
        health += gain
        print(outcome)
        print(f'{outcome} restored {gain} HP!')

    elif outcome == 'You encountered a wild beast!':
        dmg = random.randint(1, 5)
        health -= dmg
        print(outcome)
        print(f'You lost {dmg} HP in the encounter!')

    elif outcome == 'You discovered a hidden treasure!':
        gain = random.randint(1, 5)
        health += gain
        print(outcome)
        print(f'You gained {gain} from the treasure!')

    elif outcome == 'You fell into a trap!':
        dmg = random.randint(1, 5)
        health -= dmg
        print(outcome)
        print(f'You lost {dmg} HP in the trap!')

    print(f'Current Health: {health} HP')

    if health <= 0:
        print("You have succumbed to your injuries. Game Over!")
        alive = False
