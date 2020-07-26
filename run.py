"""
Identify the seat to sit at in the Josephus problem
"""
from app.round_table import identify_seat

number_of_people = int(input('Enter number of people: '))

seat = identify_seat(number_of_people)

print('You want to sit at seat number {}!'.format(seat))

