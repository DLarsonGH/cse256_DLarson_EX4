import random


class Guess_city:
    """
    CLass to support guessing a US city name.
    """

    def __init__(self, city_name):
        # Store the full city name as a list for convenience
        self._city_name = list(city_name)
        # Initialize the guess string to all blanks (as a list)
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


filename = "us_state_capitals.csv"
with open(filename, "r") as file:
    capitals = [line.rstrip() for line in file]

for i in range(2):
    encoded_name = random.choice(capitals)
    # Replace special characters
    temp_name = encoded_name.replace("#", " ")
    city_name = temp_name.replace("_", ",")
    g = Guess_city(city_name)
    print(f"Before: "
          f"{g.city_name}  : {g.city_guess}")
    for ch in ['a', 'e', 'c', ' ']:
        if g.process_guess(ch):
            print(f"Found {ch}!")
        else:
            print(f"Didn't find {ch}")
    print(f"After: {g.city_name}  : {g.city_guess}")
    print(f"{g.num_letters_found} in {g.num_guesses} guesses.")