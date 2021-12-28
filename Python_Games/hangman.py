import random
import string

from list_hangan_game import words

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word
def hangman():
    word = get_valid_word(words)
    word_letter = set(word) # letter in word
    alphabet = set(string.ascii_uppercase) # Tạo ra một set bảng chữ cái alphabet
    used_letters = set() #what the user has guess
    #getting user input
    while len(word_letter)>0:
        print("You have used these letter:" + ", ".join(used_letters))
        word_list = ["_" if letter in word else letter for letter in word]
        print("Current word: "+ " ".join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
        elif user_letter in used_letters:
            print("You have already used that character. Please try again!")
        else:
            print("Invalid character!")

hangman()
