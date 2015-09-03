#!/usr/bin/python

import sys
import time
import random

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

write_words("Welcome USC Hacker. You are invited to come to our Hacker Orientation on 9/10.")

write_words("\n\nT-Shirts.")
time.sleep(0.6)
write_words(" Waffles.")
time.sleep(0.6)
write_words(" Hackers.\n")
time.sleep(0.6)

write_words("You down?")
time.sleep(0.6)
write_words(" Enter your full name: ")

name = raw_input('')

write_words("And your usc email: ")

email = raw_input('')

write_words(hack_on, speed_min=10, speed_max=15, speed_space=0.001)

with open('output.txt', 'a') as f:
    f.write(name+','+email+'\n')

time.sleep(9999999)

sys.exit(0)