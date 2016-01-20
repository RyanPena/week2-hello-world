# replace the contents of this comment with your full name

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!

import sys
print('Hello you!')
print('I can speak 3 languages!Well at least greet you in 3!')
print('Test me! Press 1 for Spanish, 2 for German, 3 for Italian.') # standard intro up to this point
lang = int(input()) # used 'lang' to represent language choosen
if lang == 1:
    print('Hola usted!')
    sys.exit()
if lang == 2:
    print('Hallo sie!')
    sys.exit()
if lang == 3:
    print('Ciao voi!')
    sys.exit()
