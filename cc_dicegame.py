import random

high_score = 0

def dice_game():
    global high_score
    print("Current High Score is", high_score)
    print("1)Roll Dice")
    print("2)Leave Game")
    answer=input("Enter Your Choice:")
    while True:
        if answer=="1":
            first_roll=random.randint(1,6)
            second_roll=random.randint(1,6)        
            total=int(first_roll)+int(second_roll)
            print("Okay")
            print("You roll a. . .", first_roll)
            print("You roll a. . .", second_roll)
            print("You have rolled total of", total)            
            if total>high_score and answer=="1":
                high_score=total
                print("New High Score")
                dice_game()
            elif answer=="1":
                dice_game()
            else:
                break
        else:
            break

        


dice_game()


# import random

# high_score = 0


# def dice_game():
#     global high_score
#     print('Current High Score:', high_score)
#     print('1) Roll Dice')
#     print('2) Leave Game')
#     menu_selection = input('Enter your choice: ')
#     if menu_selection == '1':
#         die_1 = random.randint(1, 6)
#         die_2 = random.randint(1, 6)
#         total = die_1 + die_2
#         print('You roll a...', die_1)
#         print('You roll a...', die_2)
#         print()
#         print('You rolled a total of:', total)
#         if total > high_score:
#             high_score = total
#             print()
#             print('New high score!')
#             print()
#             dice_game()
#     elif menu_selection == '2':
#         quit()
#     else:
#         print('Option invalid')

# dice_game()
