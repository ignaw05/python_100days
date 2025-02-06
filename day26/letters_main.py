#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

database = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index,row) in database.iterrows()}

word_in = input("Enter the word: ")

list_words = [dict[letter.upper()] for letter in word_in]

print(list_words)