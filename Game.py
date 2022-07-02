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
action1 = input(f'What would you like to do first? {story.primary_menu} type the number or exit to leave the game.\n')
if action1 == 1:
    print(story.scene_desc)
    action2 == input(f'What would you like to do next? {story.scene_menu}\n'
                     f'type the number, 0 to go back to the previous options, or exit to leave the game')
    if action2 == 1:
        print(story.)

elif action1 == 2:
