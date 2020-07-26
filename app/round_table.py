"""
Pet project, wondering about the round table seat - Josephus problem

Given a group of n men seated at a round table under the edict that every second man will be
executed going around the circle until only one remains, find the seat in which you should sit
in order to be the last survivor (Ball and Coxeter 1987)
"""

def create_table(number_of_people: int) -> list:
    """
    Creates a list of seats based on the initial number of people.
    """
    sit_around_table = []

    for person in range(number_of_people):
        sit_around_table.append(person + 1)

    return sit_around_table

def identify_seat(people: int) -> int:
    """
    Identifies the seat to sit on in order to avoid death.
    """
    seated_people = create_table(people)

    while len(seated_people) > 1:
        del seated_people[1::2]  # always take out the second person

        if len(seated_people) == 1:  # this is for the last round, when we are left with last one
            return seated_people[0]
        if len(seated_people) % 2 != 0:  # takes out the first one if odd number left
            del seated_people[1::2]
            seated_people.pop(0)

    return seated_people[0]

# Improvement: what about every third man?