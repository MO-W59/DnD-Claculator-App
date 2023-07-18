"""This module of the encounter calculator app does all the calculations for the mob side
of the encounter builing process."""

# imports for directory pathing and data
import os
import pandas

# create directories then create data lists
Standard_Directory = os.path.dirname(os.path.realpath(__file__))
Mob_Data_Directory = Standard_Directory + '\\Static\\MOB_DATA.csv'
Mob_Data = pandas.read_csv(Mob_Data_Directory)
Challenge_Rating_Data = Mob_Data['CR']
Xp_Data = Mob_Data['XP']
Multiplier_Data = Mob_Data['MULTIPLIER']


class Mob:
    """This class create instances of mobs that will contain CR information and xp
    calculations."""

    def __init__(self, name, challenge_rating):

        self.name = name
        self.challenge_rating = challenge_rating

        # get xp value from Xp_Data list by matching the input challenge rating index
        xp_index = 0

        for entry in Challenge_Rating_Data:

            if challenge_rating == entry:

                break

            xp_index = xp_index + 1

        # set as the mob's xp value
        self.xp_value = Xp_Data[xp_index]

    def get_xp_value(self):
        """Gets the challenge rating of a mob."""

        return self.xp_value

    def set_challenge_rating(self, challenge_rating):
        """Sets the challenge rating of a mob."""

        self.challenge_rating = challenge_rating

        # when mob challenge rating is updated, update xp value like object creation
        xp_index = 0

        for entry in Challenge_Rating_Data:

            if challenge_rating == entry:

                break

            xp_index = xp_index + 1

        self.xp_value = Xp_Data[xp_index]


def get_challenge_total(mob_list):
    """This function gets the sum of all mobs in the list of mobs sent to it."""

    # set at -1 for proper indexing in the list
    total_mobs = -1
    challenge_total = 0

    for mob in mob_list:

        total_mobs = total_mobs + 1

        challenge_total = challenge_total + mob.get_xp_value()

    # incase user input over 15 mobs use the multiplier located at the 14th index (max)
    if total_mobs > 14:

        challenge_total = challenge_total * Multiplier_Data[14]

        return challenge_total

    # if no mobs were entered ie total mobs is still -1 return 0
    if total_mobs < 0:

        return challenge_total

    challenge_total = challenge_total * Multiplier_Data[total_mobs]

    return challenge_total
