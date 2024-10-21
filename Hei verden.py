#%%

import random
import string
import time



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