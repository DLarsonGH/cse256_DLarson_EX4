# Donald Larson
# CIS256 Fall 2024
# EX 4 (EX 4)
"""
Create a word-guessing game where the user must guess a word letter by letter.

Write a Python script named guess_the_word.py that implements the following:
1. The program selects a random word from a predefined list.
2. The user guesses one letter at a time.
3. If the guessed letter is in the word, it is revealed; otherwise, the program
   indicates the guess is incorrect.
4. The game continues until the user correctly guesses the entire word or runs
   out of attempts.
5. Display a congratulatory message when the word is guessed.

This implementation is designed to help students learn the U.S. state capitals
and state abbreviations.  Because some city names consist of two or more words
(e.g. "Santa Fe,NM") the guess characters may include a blank as well as
a letter.
"""
import random


class Guess_city:
    """
    The class supports guessing a US city name by selecting one letter at a
    time.  An object of the class is instantiated by calling the constructor
    with a string of the form "Xxxxxxxxx,YY" where Xxxxxxxxx is the city name
    and YY is the associated state abbreviation.  On instantiation, a guess_word
    is created of equal length as the selected city name but with the letters
    replaced by underscores ("_" ).  When a letter which appears in the selected
    city name is guessed, the corresponding position(s) in the guess word are
    changed from "_" to the correct character.  The guess character can also
    be a blank as some city names are two or more words in length.  Initialize
    counters for the number guesses and a runnng count of the number of letters
    correctly guessed.
    """

    def __init__(self, city_name):
        """
        Instantiate a Guess_city object.  Store the full city name and create
        a guess word of with the characters (except "'") replaced by "_".
        :param city_name:
        """
        # Store the full city name as a list for convenience
        self._city_name = list(city_name)
        # Initialize the guess string to all underscores (as a list)
        temp_guess = "_" * len(city_name)
        temp_list = list(temp_guess)
        # Place the comma separator between city and state names
        temp_list[-3] = ','
        self._city_guess = temp_list
        self._num_guesses = 0
        self._num_letters_found = 0

    def process_guess(self, guess_ch):
        """
        Process a guessed character guess_ch.  See if the guessed character is
        in the target name and, if so, update the corresponding positions in the
        guess string and increment the number of letters found.  Increment the
        number of guesses count.
        :param guess_ch: a lower-case letter [a-z] or a blank (" ")
        :return: True if one or more matches were found
        """
        match_found = False
        self._num_guesses += 1
        for i, ch in enumerate(self._city_name):
            # Compare each character in the target word with the guess_ch
            if ch.lower() == guess_ch:
                match_found = True
                self._city_guess[i] = self._city_name[i]
                self._num_letters_found += 1
        return match_found

    @property
    def city_name(self):
        """
        City name is stored internally as a list.  Return as string.
        """
        return "".join(self._city_name)

    @property
    def city_guess(self):
        """
        Guess word is stored internally as a list.  Return as string.
        """
        return "".join(self._city_guess)

    @property
    def num_guesses(self):
        return self._num_guesses

    @property
    def num_letters_found(self):
        return self._num_letters_found

    def formatted_guess(self):
        """
        Format guess word for better readability.
        :return: string
        """
        wide_word = []
        for i, ch in enumerate(self._city_guess):
            wide_word.append(ch)
            if i < (len(self._city_guess)-1):
                wide_word.append(" ")
        return "".join(wide_word)



filename = "us_state_capitals.csv"
with open(filename, "r") as file:
    capitals = [line.rstrip() for line in file]

for i in range(2):
    encoded_name = random.choice(capitals)
    # Replace special characters
    temp_name = encoded_name.replace("#", " ")
    city_name = temp_name.replace("_", ",")
    g = Guess_city(city_name)
    print(f"Chose {g.city_name}")
    for ch in ['a', 'e', 'c', ' ']:
        if g.process_guess(ch):
            print(f"Found {ch}!")
        else:
            print(f"Didn't find {ch}")
    print(f"After {g.num_guesses} guesses, {g.num_letters_found} letters found.")
    print(f"Guess the capital and state: {g.formatted_guess()}.")