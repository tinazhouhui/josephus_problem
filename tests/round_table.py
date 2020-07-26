"""
unit testing cause gotta have tests
"""

import unittest

from app.round_table import identify_seat, create_table


class TestGame(unittest.TestCase):
    """
    Unit test for each part of the round in the game.
    """

    def test_identify_seat(self):
        number_of_people = 20
        output = identify_seat(number_of_people)

        self.assertEqual(9, output)

    def test_create_table(self):
        number_of_people = 4
        output = create_table(number_of_people)

        expected = [1, 2, 3, 4, ]

        self.assertEqual(expected, output)





