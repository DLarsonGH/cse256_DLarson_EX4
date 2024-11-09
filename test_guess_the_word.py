# Donald Larson
# CIS256 Fall 2024
# EX 4 (EX 4)
"""
This file contains PyScript unit tests for the GuessCity and CityNames classes
in the guess_the_word.py file.  The tests cover all methods and properties of
the classes, including all logic paths.
"""

from guess_the_word import GuessCity, CityNames
import pytest

"""
City name for unit test.  Chosen because it includes a blank and 2 instances
of repeated characters.
"""
test_city = "Santa Fe,NM"
g = GuessCity(test_city)

"""
Script for unit test.  Each element represents a letter guess and the expected
results:
Item 0: Guess character
Item 1: Boolean, is the character in the city name?
Item 2: formatted guess word
Item 3: number of guesses
Item 4: number of letters found
Item 5: Boolean, is the game over?
"""
guess_list = [
    ['a', True, '_ a _ _ a _ _ _ , _ _', 1, 2, False],
    ['b', False, '_ a _ _ a _ _ _ , _ _', 2, 2, False],
    ['n', True, '_ a n _ a _ _ _ , N _', 3, 4, False],
    [' ', True, '_ a n _ a   _ _ , N _', 4, 5, False],
    ['c', False, '_ a n _ a   _ _ , N _', 5, 5, False],
    ['f', True, '_ a n _ a   F _ , N _', 6, 6, False],
    ['s', True, 'S a n _ a   F _ , N _', 7, 7, False],
    ['e', True, 'S a n _ a   F e , N _', 8, 8, False],
    ['m', True, 'S a n _ a   F e , N M', 9, 9, False],
    ['t', True, 'S a n t a   F e , N M', 10, 10, True]
]


def test_city_name():
    """
    Unit test for the GuessCity city_name property.  The test verifies that
    the city_name property is correctly set to the input parameter of the
    class instantiation.
    """
    assert g.city_name == test_city


def test_guess_city():
    """
    Unit test for the GuessCity methods and properties:
        process_guess()
        formatted_guess()
        game_over()
        num_guesses
        num_letters_found
    The test iterates through the guess_list array which simulates a sequence
    of 10 letter guesses.  The cases include correct and incorrect letters as
    well as the blank character.  Also included are cases where a letter
    appears more than once in the city name. The sequence also demonstrates
    correctly detecting when all the letters in the city name have been guessed.
    """
    for step in guess_list:
        result = g.process_guess(step[0])
        assert result == step[1]
        assert g.formatted_guess() == step[2]
        assert g.num_guesses == step[3]
        assert g.num_letters_found == step[4]
        assert g.game_over() == step[5]


def test_city_names_file_error():
    """
    Verify that the CityNames constructor raises a FileNotFoundError if
    the input file does not exist.
    """
    with pytest.raises(FileNotFoundError):
        bad_file_name = "xxxx.txt"
        cities = CityNames(bad_file_name)


# List of city names in the file "test_cities.txt"
valid_cities = [
    "Boise,ID", "Springfield,IL", "Indianapolis,IN", "Des Moines,IA",
    "Topeka,KS", "Frankfort,KY", "Baton Rouge,LA", "Augusta,ME",
    "Annapolis,MD", "Boston,MA", "Lansing,MI", "Saint Paul,MN"
]


def test_city_names_select_city():
    """
    Verify that the CityNames constructor correctly reads a valid city names
    file and that the select_city() method returns a properly formatted
    city name from the cities in the file.
    """
    test_file_name = "test_cities.txt"
    cities = CityNames(test_file_name)
    for i in range(5):
        city = cities.select_city()
        assert city in valid_cities
