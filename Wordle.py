'''
Wordle
Toaster
5/1/23
'''

import os, colorama, random

file_name = "wordle_words.txt"

def play_round():
    '''
    Plays a round of wordle
    '''
    selected_word = select_word()
    i = 0
    while i < 6:
        print(colorama.Fore.RESET, end="")
        guess = input("\nEnter a guess >> ").lower()
        if valid_word(guess):
            i += 1
            split_guess = list(guess)
            if check_letters(split_guess, selected_word):
                break

        else:
            print("Invalid word!")
            continue

    rejoined_word = "".join(selected_word)
    print(colorama.Fore.RESET, "\n The word was", rejoined_word)

def check_letters(guess, selected_word):
    '''
    Checks the letters and prints them out with the colors
    '''
    colors_list = []
    for i in range(0, len(selected_word)):
        if guess[i] == selected_word[i]:
            colors_list.append(colorama.Fore.GREEN)
        elif guess[i] in selected_word:
            colors_list.append(colorama.Fore.YELLOW)
        elif guess[i] not in selected_word:
            colors_list.append(colorama.Fore.LIGHTWHITE_EX)

    for i in range(0, len(selected_word)):
        print(colors_list[i], guess[i], end = "")
    print(colorama.Fore.RESET, end="")
    total_check = 0
    for i in range(0, len(colors_list)):
        if colors_list[i] == colorama.Fore.GREEN:
            total_check += 1
        else:
            continue

    if total_check == 5:
        return True

def valid_word(word):
    '''
    Checks if the users guess is in the wordle_words file.
    '''
    file = open(file_name, "r")
    words = file.readlines()
    file.close()

    for i in range(0, len(words)):
        words[i] = words[i].strip()

    if word in words:
        return True

def select_word():
    '''
    Selects a word from wordle_words.
    '''
    file = open(file_name, "r")
    words = file.readlines()
    file.close()

    for i in range(0, len(words)):
        words[i]

    selected_word = words[random.randint(0, len(words) - 1)]
    split_word = list(selected_word)
    split_word.remove("\n")
    return split_word

def clear_screen():
    '''
    Clears the screen
    '''
    if os.name == 'nt':
        os.system("cls") #For windows use.
    else:
        os.system("clear") #For linux and other OS.

loop = "y"
while loop == "y":
    play_round()
    loop = input(colorama.Fore.RESET + "\n Would you like to play another round? (y/n) >> ").lower()
    clear_screen()
