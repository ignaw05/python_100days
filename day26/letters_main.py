#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

database = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index,row) in database.iterrows()}

def ask_word():
    word_in = input("Enter the word: ")
    try:
        list_words = [dict[letter.upper()] for letter in word_in]
    except KeyError as letter:
        print(f"{letter} is not a letter!")
        ask_word()
    else:
        print(list_words)

ask_word()