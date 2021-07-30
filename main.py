import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear
name= input("please enter your name to proceed \n")
print("Welcome to")
print(logo)
end_of_game = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"Sorry {name}, you have lost the game and the correct word is {chosen_word}")
    
    if not "_" in display:
        end_of_game = True
        print("You win")
        

    print(stages[lives])