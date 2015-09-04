#!/usr/bin/python

import sys
import time
import random
import re

hack_on = """
    __  __           __      ____        __
   / / / /___ ______/ /__   / __ \____  / /
  / /_/ / __ `/ ___/ //_/  / / / / __ \/ /
 / __  / /_/ / /__/ ,<    / /_/ / / / /_/
/_/ /_/\__,_/\___/_/|_|   \____/_/ /_(_)
"""

def write_character(c):
    sys.stdout.write( '%s' % c )
    sys.stdout.flush()

def write_words(words, speed_min=400, speed_max=650, speed_space=0.08):
    for character in words:
        if character == ' ':
            time.sleep(speed_space)
        write_character(character)
        sleeptime = random.randrange(speed_min, speed_max)
        time.sleep(float(sleeptime)/10000.0)

write_words("Welcome, USC Hacker. You are invited to come to our Hacker Orientation on 9/10.\n")

write_words("\nT-Shirts.")
time.sleep(0.6)
write_words(" Waffles.")
time.sleep(0.6)
write_words(" Hackers.\n")
time.sleep(0.6)

write_words("\nYou down?")
time.sleep(0.6)
write_words(" Enter your full name: ")

name = raw_input('')
name = name.strip()

while len(name) < 2 or len(name) > 80:
    write_words("Whoops! Please make sure your name is more than a character and less than 80 characters.\n")
    write_words("Enter your full name: ")
    name = raw_input('')
    name = name.strip()

write_words("And your usc email: ")

email_regex = re.compile('^[a-z+\.]+\@usc\.edu$')

email = raw_input('')
email = email.strip()

while email_regex.match(email) is None:
    write_words("Whoops! Please make sure your email is a valid @usc.edu email.\n")
    write_words("Enter your usc email: ")
    email = raw_input('')
    email = email.strip()


with open('output.txt', 'a') as f:
    f.write(name.replace(',', '')+','+email.replace(',', '')+','+str(time.time())+',false'+'\n')

write_words("\nWe'll see you at 6:30 on 9/10 in the Annenberg West Lobby!")

write_words(hack_on, speed_min=10, speed_max=15, speed_space=0.001)

time.sleep(1.5)

write_words('\n;)')

time.sleep(20)

write_words(' You\'re still here? Might want to view the page source...\n')

time.sleep(1.5)

write_words('???: ')

md5 = raw_input('')
md5.strip()

while md5 != '000242dc7a5257e1f265578cdcc6c3fd':
    write_words('???: ')
    md5 = raw_input('')
    md5.strip()

write_words('You were added to the list "TOP SECRET". We\'ll be in touch soon. Hack On.')

with open('output.txt', 'a') as f:
    f.write(name.replace(',', '')+','+email.replace(',', '')+','+str(time.time())+',true'+'\n')

sys.exit(0)
