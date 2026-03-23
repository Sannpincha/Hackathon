# Name: Toby
# Period: 7th
# Assignment: Hackathon
# Time Spent: 3 hours maybe? I haven't been keeping track.
# Note: I think the time.sleep() is too short for all of these, so, uh sorry.

# Imports everything I use for this project
import datetime
import random
import json
import time

# Imports the English Dictionary which is a json file.
with open("words_dictionary.json", "r") as file:
    words_dict = json.load(file)

# The number of eyes the man has is how many words you need to type for the first part.
manEyes = random.randint(2, 8)

# Wipes the screen
print("\033[H\033[2J", end="")

# First prompt
print(f"A crowd shows up to hear what you have to say. A man with {manEyes} eyes walk into frame, alongside a person with {random.randint(2, 8)} feathers in their hat and another person walks in with {random.randint(1, 5)} pupils.")

# All the time.sleep()'s is for making you wait. I don't want to comment on all of them.
time.sleep(2)
# Insert words
oneAns = input("What will you say to the crowd?\n")

# Tracks how many words you said
AnsWrds1 = len(oneAns.split())

# Selects all the words that are 5 letters or less in the dictionary
guessWrd = [word for word in words_dict.keys() if len(word) <= 5]

# Picks a random word
randomWrd = random.choice(guessWrd)

# Takes the length of that randomWrd to tell the user how long the word is.
randomWrdlen = len(randomWrd)

# Tracks the correct letters you've guessed
correctGs = []
time.sleep(1.5)
# IF you say the right amount of words
if AnsWrds1 == manEyes:

    print("The crowd loved what you had to say! They are planning to throw you a party! \nYou need to write the speech you will be performing for tomorrow. \nThere's a certain word you want to use, but you can't quite figure it out.")

    # Lets you guess forever! I didn't want to make some sort of lives system.
    while True:
        # Prints the correct guesses you've said
        print(correctGs)

        # Asks for a letter
        twoAns = input(f"\nWhat is a letter in that word? The word is {randomWrdlen} characters long: ").lower()

        # If you actually provide A letter or not
        if len(twoAns) == 1 and twoAns.isalpha():
            # Tells you the letter is in the word and adds it to the correct guesses list.
            if twoAns in randomWrd:
                print(f"{twoAns} is in the word.")
                count = randomWrd.count(twoAns)
                for x in range(count):
                    correctGs.append(twoAns)
                print(f"It appears {count} time(s).")
            else:
            # If the letter is not there.    
                print(f"{twoAns} is not in the word. Try again.")
        else:
            print("Please enter only one letter.")
        # If the word is guessed    
        if all(letter in correctGs for letter in randomWrd):
            print(f"\nOh, the word was '{randomWrd}'. How could you forget?")
            break
else:
    print("The crowd is displeased! You lose!")
    quit()

# Gets the current time
lastTime = datetime.datetime.now()
# Gets the time in Hours, Minutes, and whether it's AM or PM
lastTime12 = lastTime.strftime("%I:%M %p")
# You need to type as many words as what hour it is. If it's 12:00, then 12 words.
hourTime = int(lastTime.strftime("%I"))

# Story
print(f"\nYou deliever your speech with the included wise word: {randomWrd}. The party goes wild, they love you!")
time.sleep(1)
print(f"\n(Not that you could get it wrong, you had unlimited tries to guess that word.)")
time.sleep(5)
print("\033[H\033[2J", end="")
print(f"\nYears pass by, you have to leave the town you reside in because you've grown bored of it.")
time.sleep(1)
print(f"\nYet again, a crowd shows up to hear your final goodbyes. The time is currently {lastTime12}.")
time.sleep(1.5)
# Your final words. Requests your input.
finalWrd = input("\nWhat are/is your final word(s)? ")

# However many words in your final words.
finalWrdlen = len(finalWrd.split())

# If the right amount of words, great! Otherwise, you lose.
if finalWrdlen == hourTime:
    print("...")
    time.sleep(3)
    print(f"\nEveryone sobs to see such a bright indivudal leave. What a shame!")
    time.sleep(2)
    print(f"\nAt least you have left with a great reputation. They will forever remember the words you've said, such as: {oneAns}, {randomWrd}, and, most importantly; {finalWrd}.")

else:
    print("...")
    time.sleep(3)
    print("Everyone stares at you. Why would you say such a thing? At this hour? You leave town in shame, no one will remember your name.")