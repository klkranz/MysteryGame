# import modules
import MurderAtChromaManor

# Introduction
print(f'Welcome!  You have been sent as the Detective Chief Inspector to investigate a crime.')
DCI = input('What name would you like to go by Detective Chief Inspector?\n')
story = MurderAtChromaManor  # Eventually this will be either a menu to pick the story or generated randomly.
print(f'Welcome to {story.title}, Detective Chief Inspector {DCI}.')
print(story.setting)
print(f'What do you have for me today, {story.det_sergeant}?')
print(story.intro)
main_menu = input(f'{story.main_menu}\nType the number or "exit" to leave the game.\n')
if main_menu == 1:
    print(story.menu1_desc)
    option1 = input(f'What would you like to do next? {story.menu1_menu}\n Type the number, 0 to go back to the '
                    f'previous options, or "exit" to leave the game\n')
    if option1 == 1:
        print(story.menu1_opt1_desc)
        opt1_choice1 = input(f'Would you like to examine anything closer at this time? {story.menu1_opt1_menu}\n'
                             f'Type the number, 0 to go back to the previous options, or "exit" to leave the game\n')
    elif option1 == 2:
        print(story.menu1_opt2_desc)
        opt1_choice2 = input(f'Would you like to examine anything closer at this time? {story.menu1_opt2_menu}\n'
                             f'Type the number, 0 to go back to the previous options, or "exit" to leave the game\n')
    elif option1 == 3:
        print(story.menu1_opt3_desc)

elif main_menu == 2:
    print(story.menu2_desc)
    option2 = input(f'What would you like to do next? {story.menu2_menu}\n Type the number, 0 to go back to the '
                    f'previous options, or "exit" to leave the game\n')

elif main_menu == 3:
    print(story.menu3_desc)
    option3 = input(f'What would you like to do next? {story.menu3_menu}\n Type the number, 0 to go back to the '
                    f'previous options, or "exit" to leave the game\n')
