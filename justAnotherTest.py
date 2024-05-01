import random

print("Welcome to wonderland!!\n")

words = ["Hacker", "Land", "House"]
empt_list = []
counter = 0
Checker = True

sword = random.choice(words).lower()
for l in sword:
    empt_list.append("_")
print(f"The word you choosed is a {len(empt_list)} letters word")
print("Happy Guessing")
print(f"{empt_list}\n")

while Checker:
    guess = str(input("Please guess a letter: "))
    print(empt_list)
 #   for i in 
    for letter in sword:
        if guess.lower() == letter.lower():
            print("You just got a bonus point of 10 for guessing a correct letter")
            if sword.index(guess.lower()) != counter:
                print("Well you guessed the right word but at the wrong time fam")
            empt_list[counter] = guess
            if "_" != empt_list[-1] :
                print("Hooray you've completed the puzzle")
        else:
            print("Wrong")
    counter += 1
    print(empt_list)

    if counter == len(empt_list) :
        Checker = False
    
counter = 0





