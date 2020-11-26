import random
import time
import sys
# Introduction to user:
print("\nWelcome to Hangman game\n")
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)


# Execute the game:
def main():
    global count
    global display
    global word
    global guessed_letter
    global length
    global play_game
    global displaying
    words_to_guess = ['abruptly', 'bandwagon', 'caliph', 'dizzying', 'equip', 'faking', 'galaxy', 'haiku', 'icebox', 'jackpot', 'kayak', 'larynx', 'matrix', 'nightclub', 'onyx', 'pajama', 'quartz', 'rhythm', 'scratch', 'thumbscrew', 'unknown', 'vaporize', 'walkway', 'xylophone', 'yachtsman', 'zigzag']
    word = random.choice(words_to_guess)
    displaying = word
    length = len(word)
    count = 0
    display = '_' * length
    guessed_letter = []
    play_game = ""

# Restart the game when finished:

def game_restarted():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing!!")
        sys.exit(0)

# Conditions required for the game:
def game():
    global count
    global display
    global word
    global guessed_letter
    global displaying
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        game()


    elif guess in word:
        guessed_letter.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in guessed_letter:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",displaying)
            game_restarted()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        game_restarted()

    elif count != limit:
        game()


main()


game()