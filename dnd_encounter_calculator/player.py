"""This module of the encounter calculator app does all the calculations for the player side
of the encounter builing process."""

# imports for directory and file reading, and add function
import os
import operator
import pandas


# setup directory and data lists from PLAYER_DATA.csv
Standard_Directory = os.path.dirname(os.path.realpath(__file__))
Player_Data_Directory = Standard_Directory + '\\Static\\PLAYER_DATA.csv'
Player_Data = pandas.read_csv(Player_Data_Directory)
Easy_Data = Player_Data['EASY']
Med_Data = Player_Data['MEDIUM']
Hard_Data = Player_Data['HARD']
Deadly_Data = Player_Data['DEADLY']
Daily_Data = Player_Data['DAILY']


class Player:
    """This is a class for player objects which have xp values based on their level."""

    def __init__(self, name, level):

        self.name = name
        self.level = level

        # -1 to the level for proper list indexing
        xp_index = level - 1

        self.easy_xp = Easy_Data[xp_index]
        self.med_xp = Med_Data[xp_index]
        self.hard_xp = Hard_Data[xp_index]
        self.deadly_xp = Deadly_Data[xp_index]
        self.daily_xp = Daily_Data[xp_index]


    def set_player_level(self, level):
        """This function updates a players level and xp values to match the update."""

        self.level = level

        # -1 to the level for proper list indexing
        xp_index = level - 1

        self.easy_xp = Easy_Data[xp_index]
        self.med_xp = Med_Data[xp_index]
        self.hard_xp = Hard_Data[xp_index]
        self.deadly_xp = Deadly_Data[xp_index]
        self.daily_xp = Daily_Data[xp_index]


    def get_player_xp_levels(self):
        """This function returns all the xp levels for a player, such as easy, hard, daily
        in a list."""

        xp_levels = [self.easy_xp, self.med_xp, self.hard_xp, self.deadly_xp, self.daily_xp]

        return xp_levels


def get_party_xp_totals(player_list):
    """This function adds all the player exp levels together."""

    xp_totals = [0, 0, 0, 0, 0]

    for player in player_list:

        # add the list together with map and add
        xp_totals = list(map(operator.add, xp_totals, player.get_player_xp_levels()))

    return xp_totals
