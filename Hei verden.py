# Mitt testrepo
#%%

import random
import string
import time


def generate_hello_world():
    letters = string.ascii_letters
    target = "HelloWorld"
    result = ""

    for letter in target:
        while True:
            I = random.choice(letters)
            print(result + I)
            if I == letter:
                result += I
                break
            time.sleep(0.05)


    def generate_hello_world():
    letters = string.ascii_letters
    target = "Oskar kom deg på stein kasting"
    result = ""

    for letter in target:
        while True:
            I = random.choice(letters)
            print(result + I)
            if I == letter:
                result += I
                break
            time.sleep(0.05)
    
    return result

# Usage
hello_world_result = generate_hello_world()
        
        
        /fill  1 1 1  10 10 10  minecraft:stone

