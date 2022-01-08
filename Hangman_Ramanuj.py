from urllib.request import urlopen
import json
import time
def get_random_word():
    url =("https://random-word-api.herokuapp.com/word?number=1")
    response = urlopen(url)
    random_word = response.read().decode("utf-8")
    return random_word[2:-2]

def ask_to_play_again():
    choice_to_play = input("Want to play Again???\nEnter yes or no: ")
    if choice_to_play.lower() not in ["no","n"]:
        hangman()
    else:
        print("Thankyou for your time!!!")
    
def check_valid_guessed_character(guessed_character,wrong_guesses,already_guessed):
    valid = False
    if len(guessed_character) > 1:
        print("Invalid Input!!! You have entered more than one character")
    elif guessed_character.isupper():
        print("Invalid Input!!! Please enter lowercase character")
    elif guessed_character.isalpha() == False:
        print("Invalid input!!! Please enter characters only")
    elif guessed_character in wrong_guesses:
        print("You have already guessed this wrong character")
    elif guessed_character in already_guessed:
        print("Correct but Already guessed this letter")
    else:
        valid = True
    return valid 

def hangman():
    winning_string = get_random_word()
    char_counter = {}
    currently_guessed = []
    for i in range(len(winning_string)):
        char_counter[winning_string[i]] = char_counter.get(winning_string[i],0) + 1
        currently_guessed.append("_")

    print("Welcome to the hangman game from Ramanuj....")
    time.sleep(2)

    win_flag = False
    remaining_lives = 5

    wrong_guesses = ""
    already_guessed = ""
    wrong_guess_count = 0

    
    while remaining_lives > 0:
        print(f"You have {remaining_lives} lives left....")
        for i in range(len(currently_guessed)):
            if i != len(currently_guessed)-1:
                print(currently_guessed[i], end = " ")
            else:
                print(currently_guessed[i])
    
        print("Enter the character you guessed...")
        guessed_character = input()
        if check_valid_guessed_character(guessed_character,wrong_guesses,already_guessed) == False:
            continue
        if guessed_character in char_counter:
            print("Correct Attempt!!!")
            already_guessed += guessed_character
            for i in range(len(currently_guessed)):
                if winning_string[i] == guessed_character:
                    currently_guessed[i] = guessed_character
        else:
            wrong_guesses += guessed_character
            time.sleep(1)
            print("Sorry !!! Wrong Attempt")
            remaining_lives -= 1
            wrong_guess_count += 1
            if(wrong_guess_count == 1):
                print("   _____ \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif(wrong_guess_count == 2):
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif(wrong_guess_count == 3):
                print("   _____ \n"
                      "  |     |\n"
                      "  |     |\n"
                      "  |     |\n"
                      "  |     O \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif(wrong_guess_count == 4):
                print("   _____ \n"
                      "  |     | \n"
                      "  |     | \n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |      \n"
                      "__|__\n")
            elif(wrong_guess_count == 5):
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "__|__\n")
        if "_" not in currently_guessed:
            win_flag = True
            break

    if win_flag:
        print(winning_string)
        print("Hurray!!! You Win")

    else:
        print("You lose....\nBetter luck next time")
        print(f"The correct word was \"{winning_string}\"")
    time.sleep(2)
    ask_to_play_again()

hangman()