# List of imports

import time
import random
import functools
import os
import json
import requests

from os import system
from time import sleep




# Changing print function to ensure it doesnt buffer, can disable during print with flush=false argument

print = functools.partial(print, flush=True)


# Creating function for clearing the screen easily, should work on mac and PC but testing required

def clear():
    '''Unpopulated function, checks whether installed operating system is Windows or MacOS'''
    if os.name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Creating function for pulling random jokes from the Holypython official jokes API



# Creating variable for making a small gap between text

gap = "\n"

# Adding the title section for the interface

for x in ("=" * 80):
    print(x, end='')
    sleep(0.005)

print()

for x in (("-" * 35) + ("Welcome to") + ("-" * 35)):
    print(x, end='')
    sleep(0.005)

print()

for x in (("-" * 30) + ("Vault-Tec Companion") + ("-" * 31)):
    print(x, end='')
    sleep(0.005)

print()

for x in (("-" * 37) + ("v1.0.1") + ("-" * 37)):
    print(x, end='')
    sleep(0.005)

print()

for x in ("=" * 80):
    print(x, end='')
    sleep(0.005)

print(gap*2)

sleep(1.5)

# Flavour text

for x in ("New user detected..."):
    print(x, end='')
    sleep(0.1)

print(gap)

sleep(1.5)

for x in ("Loading new user interface"):
    print(x, end='')
    sleep(0.1)

sleep(1)

for x in ("." * 10):
    print(x, end='')
    sleep(0.1)

print(gap*5)

# Gathering users desired username

name = input("Please enter your name: ")

print(gap)

for x in (f"Processing user: {name}..."):
    print(x, end='')
    sleep(0.1)

sleep(1.5)

print(gap)

for x in (f"Saving user: {name}..."):
    print(x, end='')
    sleep(0.1)

sleep(1.5)
    
print(gap)

for x in (f"Hello {name}, welcome to the Vautl-tec personal companion program \nalso known as 'V.T.P.C.P' "):
    print(x, end='')
    sleep(0.05)

sleep(1.5)

print(gap)

for x in ("Loading main menu....."):
    print(x, end='')
    sleep(0.1)

sleep(1.5)

clear()

# Temp name holder for troubleshooting, needs to be commented out

name = "Rick"

# Initiating the main menu

for x in ("=" * 80):
    print(x, end='')
    sleep(0.00001)

print()

for x in (("-" * 36) + ("Main Menu") + ("-" * 35)):
    print(x, end='')
    sleep(0.00001)
    
print()

for x in ("=" * 80):
    print(x, end='')
    sleep(0.00001)
    
print(gap*4)

for x in ("[1] Knock-Knock Joke Generator - Created by Bubblegumcandy"):
    print(x, end='')
    sleep(0.0005)

print(gap*2)

for x in (f"[2] Comedy script review - Under construction, [ACCESS DENIED] "):
    print(x, end='')
    sleep(0.0005)

print(gap*2)

for x in ("[3] Interview script generator - closed beta in progress [ACCESS DENIED] "):
    print(x, end='')
    sleep(0.0005)

print(gap*2)

for x in ("[4] Project Sunshine..... [TOP SECRET].... checking credentials...."):
    print(x, end='')
    sleep(0.0005)
    
sleep(1)
    
for x in (f"{name} has invalid credentials... [ACCESS DENIED]"):
    print(x, end='')
    sleep(0.01)

print(gap*2)


while True:
    selection = int(input("Please make a selection: "))
    if selection > 4:
        for x in ("That is not a valid selection "):
            print(x, end="")
            sleep(0.0005)
    elif selection != 1:
        for x in ("ACCESS DENIED "):
            print(x, end="")
            sleep(0.0005)
    else:
        for x in ("You have selected the Knock-Knock Joke Generator "):
            print(x, end="")
            sleep(0.0005)
        break
sleep(2)
print(gap*2)

for x in ("Loading the Knock-Knock Joke Generator.....Please wait"):
    print(x, end="")
    sleep(0.005)

sleep(2)

clear()

# Defining joke funciton for pulling Jokes from official joke API    
    
def jokes(f):
    
    data = requests.get(f)
    tt = json.loads(data.text)
    return tt

f = r"https://official-joke-api.appspot.com/jokes/knock-knock/random"
a = jokes(f)

# Requesting how many jokes to generate

joke_counter = int(input("How many Knock-Knock jokes would you like to hear?: "))

requested_jokes = 0
# Loop for generating the jokes

while True:

    if requested_jokes != joke_counter:
        f = r"https://official-joke-api.appspot.com/jokes/knock-knock/random"
        a = jokes(f)
        for i in (a):
            print(i["setup"])
            sleep(3)
    
            print(i["punchline"], "\n")
            sleep(2.5)
            
            requested_jokes = (requested_jokes + 1)
            print(f"You have heard {requested_jokes} joke request(s)")
            sleep(1)
            
            print(gap*2)
            
    else:
        print(f"The simpulator has successfully generated {joke_counter} jokes. ")
        break

sleep(3)
            
print(gap*3)
# Flavour to exit the program
            
for x in ("Returning you to the main menu.... Please wait..."):
    print(x, end="")
    sleep(0.005)

sleep(2)
print(gap*2)

for x in ("Warning, security breach detected"):
    print(x, end="")
    sleep(0.05)

sleep(3)
print(gap*2)

for x in (f"For your safety {name}, I am closing the Vault-Tec personal companion program..."):
    print(x, end="")
    sleep(0.03)

sleep(2)

clear()

# Adding life to the program

for x in (f"Goodbye..... {name}"):
    print(x, end="")
    sleep(0.05)

sleep(3)

for x in ("... may we meet "):
    print(x, end="")
    sleep(0.2)
    
sleep(1.5)

for x in ("again..."):
    print(x, end="")
    sleep(0.5)
sleep(2)

clear()

sleep(2)

