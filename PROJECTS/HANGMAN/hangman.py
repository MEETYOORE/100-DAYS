import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)

chosen_word = random.choice(word_list)
blanks = []
count = 6

for i in range(0,len(chosen_word)):
    blanks.append("_")

print(chosen_word)
print(blanks)

GAME_NOT_OVER = True

while GAME_NOT_OVER:
    if not '_' in blanks:
        clear()
        print(stages[-1])
        print(blanks)
        print("YOU WIN 🥳🥳")
        break

    guess = input("\nGuess a letter: ").lower()
    clear()

    if guess in blanks:
        print(f"\nYou already guessed letter {guess} 😬")
        print(stages[count])
        print(blanks)

    elif guess in chosen_word and '_' in blanks:
        for i in range(0,len(chosen_word)):
            if chosen_word[i] == guess:
                blanks[i] = guess
        
        print(stages[count])
        print(blanks)

    else:
        count -= 1
        if count > 0:
            print(stages[count])
            print(f"You guessed the letter {guess} which is wrong 🥲 {count} lives left")
        else:
            print(stages[count])
            print(f"You are hanged 💀💀💀")
            GAME_NOT_OVER = False
