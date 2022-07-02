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
action = input(f'What would you like to do first? {story.primary_menu}:\n')
