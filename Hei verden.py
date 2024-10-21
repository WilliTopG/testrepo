import random
import string
import time


#%%
def generate_hello_world():
    letters = string.ascii_letters
    target = "HelloWorld"
    result = ""

    for letter in target:
        while True:
            i = random.choice(letters)
            print(result + i)
            if i == letter:
                result += i
                break
            time.sleep(0.05)
    return result


#%%
def generate_hello_world_custom():
    letters = string.ascii_letters + " "
    target = "Oskar kom deg på stein kasting"
    result = ""

    for letter in target:
        while True:
            i = random.choice(letters)
            print(result + i)
            if i == letter:
                result += i
                break
            time.sleep(0.05)
    
    return result

if __name__ == "__main__":
    print("Generating 'HelloWorld':")
    print(generate_hello_world())
    print("\nGenerating custom message:")
    print(generate_hello_world_custom())


