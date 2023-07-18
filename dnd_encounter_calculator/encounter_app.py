"""This program will create a GUI window that users can use to calculate their encounter
difficulties for their DnD games. Utilizes the accompaning modules mob and player .py
along with the CSV files in the Static folder."""

import sys
import os
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import mob
import player


# disable linter message due to using C extention
# pylint: disable=c-extension-no-member
Big_Font = qtg.QFont('Times', 13)
Regular_Font = qtg.QFont('Times', 11)
Background_Color = qtg.QColor(30, 30, 30)
Window_Icon = os.path.dirname(os.path.realpath(__file__)) + '\\Static\\Mortis.png'


# disable linter message due to using C extention and too many attributes
# pylint: disable=c-extension-no-member
# pylint: disable=too-many-instance-attributes
class EncounterGui(qtw.QMainWindow):
    """This class creates an instance of the encounter app gui."""
    # statements required in class to get user input
    # pylint: disable=too-many-statements

    def __init__(self):
        super().__init__()

        # Setup variables used to contain changable values
        self.easy_xp = 0
        self.med_xp = 0
        self.hard_xp = 0
        self.deadly_xp = 0
        self.daily_xp = 0
        self.encounter_difficulty = 'N\\A'
        self.encounter_xp = 0
        # lists to hold the text objects to iterate through during encounter calculation
        self.player_levels = []
        self.player_numbers = []
        self.mob_crs = []
        self.mob_numbers = []

        # Setup main window
        self.setGeometry(800, 500, 800, 600)
        self.setWindowTitle("Gerg(Atron)'s DnD Xp Calculator")
        self.setStyleSheet('background-color: rgb(30, 30, 30);'
                           'color: white')
        self.setWindowIcon(qtg.QIcon(Window_Icon))

        # Setup player set labels
        self.player_set_labels = qtw.QLabel(self)
        self.player_set_labels.setText('Player Set 1:\n'
                                       '\nPlayer Set 2:\n'
                                       '\nPlayer Set 3:\n'
                                       '\nPlayer Set 4:\n'
                                       '\nPlayer Set 5:')
        self.player_set_labels.setFont(Regular_Font)
        self.player_set_labels.setGeometry(20, 70, 100, 180)

        # Setup X labels
        self.player_set_x_labels = qtw.QLabel(self)
        self.player_set_x_labels.setText('X\n'
                                         '\nX\n'
                                         '\nX\n'
                                         '\nX\n'
                                         '\nX')
        self.player_set_x_labels.setFont(Regular_Font)
        self.player_set_x_labels.setGeometry(157, 70, 20, 180)

        # Setup set 1 text boxes
        self.player_level_set1_text = qtw.QTextEdit(self)
        self.player_level_set1_text.setGeometry(120, 75, 25, 25)
        self.player_level_set1_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_level_set1_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_number_set1_text = qtw.QTextEdit(self)
        self.player_number_set1_text.setGeometry(180, 75, 25, 25)
        self.player_number_set1_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_number_set1_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_levels.append(self.player_level_set1_text)
        self.player_numbers.append(self.player_number_set1_text)

        # Setup set 2 text boxes
        self.player_level_set2_text = qtw.QTextEdit(self)
        self.player_level_set2_text.setGeometry(120, 111, 25, 25)
        self.player_level_set2_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_level_set2_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_number_set2_text = qtw.QTextEdit(self)
        self.player_number_set2_text.setGeometry(180, 111, 25, 25)
        self.player_number_set2_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_number_set2_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_levels.append(self.player_level_set2_text)
        self.player_numbers.append(self.player_number_set2_text)

        # Setup set 3 text boxes
        self.player_level_set3_text = qtw.QTextEdit(self)
        self.player_level_set3_text.setGeometry(120, 147, 25, 25)
        self.player_level_set3_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_level_set3_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_number_set3_text = qtw.QTextEdit(self)
        self.player_number_set3_text.setGeometry(180, 147, 25, 25)
        self.player_number_set3_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_number_set3_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_levels.append(self.player_level_set3_text)
        self.player_numbers.append(self.player_number_set3_text)

        # Setup set 4 text boxes
        self.player_level_set4_text = qtw.QTextEdit(self)
        self.player_level_set4_text.setGeometry(120, 183, 25, 25)
        self.player_level_set4_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_level_set4_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_number_set4_text = qtw.QTextEdit(self)
        self.player_number_set4_text.setGeometry(180, 183, 25, 25)
        self.player_number_set4_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_number_set4_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_levels.append(self.player_level_set4_text)
        self.player_numbers.append(self.player_number_set4_text)

        # Setup set 5 text boxes
        self.player_level_set5_text = qtw.QTextEdit(self)
        self.player_level_set5_text.setGeometry(120, 219, 25, 25)
        self.player_level_set5_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_level_set5_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_number_set5_text = qtw.QTextEdit(self)
        self.player_number_set5_text.setGeometry(180, 219, 25, 25)
        self.player_number_set5_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_number_set5_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.player_levels.append(self.player_level_set5_text)
        self.player_numbers.append(self.player_number_set5_text)

        # setup mob labels
        self.mob_set_labels = qtw.QLabel(self)
        self.mob_set_labels.setText('Mob Set 1:\n'
                                    '\nMob Set 2:\n'
                                    '\nMob Set 3:\n'
                                    '\nMob Set 4:\n'
                                    '\nMob Set 5:\n'
                                    '\nMob Set 6:\n'
                                    '\nMob Set 7:\n'
                                    '\nMob Set 8:\n'
                                    '\nMob Set 9:\n'
                                    '\nMob Set 10:')
        self.mob_set_labels.setFont(Regular_Font)
        self.mob_set_labels.setGeometry(580, 75, 100, 350)

        # Setup X labels
        self.mob_set_x_labels = qtw.QLabel(self)
        self.mob_set_x_labels.setText('X\n'
                                      '\nX\n'
                                      '\nX\n'
                                      '\nX\n'
                                      '\nX\n'
                                      '\nX\n'
                                      '\nX\n'
                                      '\nX\n'
                                      '\nX\n'
                                      '\nX')
        self.mob_set_x_labels.setFont(Regular_Font)
        self.mob_set_x_labels.setGeometry(708, 75, 20, 350)

        # Setup set 1 text boxes
        self.mob_cr_set1_text = qtw.QTextEdit(self)
        self.mob_cr_set1_text.setGeometry(670, 75, 28, 25)
        self.mob_cr_set1_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_cr_set1_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set1_text = qtw.QTextEdit(self)
        self.mob_number_set1_text.setGeometry(730, 75, 25, 25)
        self.mob_number_set1_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set1_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_crs.append(self.mob_cr_set1_text)
        self.mob_numbers.append(self.mob_number_set1_text)

        # Setup set 2 text boxes
        self.mob_cr_set2_text = qtw.QTextEdit(self)
        self.mob_cr_set2_text.setGeometry(670, 111, 28, 25)
        self.mob_cr_set2_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_cr_set2_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set2_text = qtw.QTextEdit(self)
        self.mob_number_set2_text.setGeometry(730, 111, 25, 25)
        self.mob_number_set2_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set2_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_crs.append(self.mob_cr_set2_text)
        self.mob_numbers.append(self.mob_number_set2_text)

        # Setup set 3 text boxes
        self.mob_cr_set3_text = qtw.QTextEdit(self)
        self.mob_cr_set3_text.setGeometry(670, 147, 28, 25)
        self.mob_cr_set3_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_cr_set3_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set3_text = qtw.QTextEdit(self)
        self.mob_number_set3_text.setGeometry(730, 147, 25, 25)
        self.mob_number_set3_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set3_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_crs.append(self.mob_cr_set3_text)
        self.mob_numbers.append(self.mob_number_set3_text)

        # Setup set 4 text boxes
        self.mob_cr_set4_text = qtw.QTextEdit(self)
        self.mob_cr_set4_text.setGeometry(670, 183, 28, 25)
        self.mob_cr_set4_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_cr_set4_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set4_text = qtw.QTextEdit(self)
        self.mob_number_set4_text.setGeometry(730, 183, 25, 25)
        self.mob_number_set4_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set4_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_crs.append(self.mob_cr_set4_text)
        self.mob_numbers.append(self.mob_number_set4_text)

        # Setup set 5 text boxes
        self.mob_cr_set5_text = qtw.QTextEdit(self)
        self.mob_cr_set5_text.setGeometry(670, 219, 28, 25)
        self.mob_cr_set5_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_cr_set5_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set5_text = qtw.QTextEdit(self)
        self.mob_number_set5_text.setGeometry(730, 219, 25, 25)
        self.mob_number_set5_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set5_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_crs.append(self.mob_cr_set5_text)
        self.mob_numbers.append(self.mob_number_set5_text)

        # Setup set 6 text boxes
        self.mob_cr_set6_text = qtw.QTextEdit(self)
        self.mob_cr_set6_text.setGeometry(670, 255, 28, 25)
        self.mob_cr_set6_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_cr_set6_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set6_text = qtw.QTextEdit(self)
        self.mob_number_set6_text.setGeometry(730, 255, 25, 25)
        self.mob_number_set6_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set6_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_crs.append(self.mob_cr_set6_text)
        self.mob_numbers.append(self.mob_number_set6_text)

        # Setup set 7 text boxes
        self.mob_cr_set7_text = qtw.QTextEdit(self)
        self.mob_cr_set7_text.setGeometry(670, 291, 28, 25)
        self.mob_cr_set7_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_cr_set7_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set7_text = qtw.QTextEdit(self)
        self.mob_number_set7_text.setGeometry(730, 291, 25, 25)
        self.mob_number_set7_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set7_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_crs.append(self.mob_cr_set7_text)
        self.mob_numbers.append(self.mob_number_set7_text)

        # Setup set 8 text boxes
        self.mob_cr_set8_text = qtw.QTextEdit(self)
        self.mob_cr_set8_text.setGeometry(670, 327, 28, 25)
        self.mob_cr_set8_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_cr_set8_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set8_text = qtw.QTextEdit(self)
        self.mob_number_set8_text.setGeometry(730, 327, 25, 25)
        self.mob_number_set8_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set8_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_crs.append(self.mob_cr_set8_text)
        self.mob_numbers.append(self.mob_number_set8_text)

        # Setup set 9 text boxes
        self.mob_cr_set9_text = qtw.QTextEdit(self)
        self.mob_cr_set9_text.setGeometry(670, 363, 28, 25)
        self.mob_cr_set9_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_cr_set9_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set9_text = qtw.QTextEdit(self)
        self.mob_number_set9_text.setGeometry(730, 363, 25, 25)
        self.mob_number_set9_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set9_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_crs.append(self.mob_cr_set9_text)
        self.mob_numbers.append(self.mob_number_set9_text)

        # Setup set 10 text boxes
        self.mob_cr_set10_text = qtw.QTextEdit(self)
        self.mob_cr_set10_text.setGeometry(670, 399, 28, 25)
        self.mob_cr_set10_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_cr_set10_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set10_text = qtw.QTextEdit(self)
        self.mob_number_set10_text.setGeometry(730, 399, 25, 25)
        self.mob_number_set10_text.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_number_set10_text.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.mob_crs.append(self.mob_cr_set10_text)
        self.mob_numbers.append(self.mob_number_set10_text)

        # Setup the other parts of the window and the calculate button
        draw_top_labels(self)
        draw_player_output_labels(self)
        draw_player_xp(self)
        draw_encouter_output_labels(self)
        draw_encounter_diff(self)
        draw_encounter_xp(self)
        self.calculate_button = draw_calculate_button(self)

    def calculate_clicked(self):
        """This function handles the events resulting from the user clicking the
        calculate button."""

        player_xp_list = self.get_party_values()
        passed_encounter_xp = self.get_mob_values()
        self.set_xp_values(player_xp_list, passed_encounter_xp)

    def show_error(self, error):
        """This function will display the passed error message to the user in a
        separate window."""

        error_window = qtw.QMessageBox()
        error_window.setIcon(qtw.QMessageBox.Critical)
        error_window.setText(error)
        error_window.setWindowTitle('ERROR!')
        error_window.exec_()

    def get_party_values(self):
        """This function will retrive the party values entered into party information
        boxes."""

        # counts the total number of players, used for naming new player objects
        player_counter = 1
        # sets the index of the player_numbers list
        number_set_index = 0
        # prepare empty player list
        player_list = []

        for player_set in self.player_levels:

            player_level = player_set.toPlainText()

            if player_level is None or player_level == '':

                number_set_index = number_set_index + 1

                continue

            try:

                player_level = int(player_level)

            except ValueError:

                error = ('ERROR: Invalid entry in party information.\n'
                         'Please ensure you have only entered numeric values.')

                self.show_error(error)

                continue

            if player_level < 1 or player_level > 20:

                error = 'ERROR: Player levels must be between 1 and 20.'

                self.show_error(error)

                continue

            number_players_in_set = self.player_numbers[number_set_index].toPlainText()

            if number_players_in_set is None or number_players_in_set == '':

                number_set_index = number_set_index + 1

                continue

            try:

                number_players_in_set = int(number_players_in_set)

            except ValueError:

                number_set_index = number_set_index + 1

                error = ('ERROR: Invalid entry in party information.\n'
                         'Please ensure you have only entered numeric values.')

                self.show_error(error)

                continue

            added_players = 0

            while number_players_in_set > added_players:

                player_name = 'player_' + str(player_counter)

                player_list.append(player.Player(player_name, player_level))

                added_players = added_players + 1

                player_counter = player_counter + 1

            number_set_index = number_set_index + 1

        player_xp_list = player.get_party_xp_totals(player_list)

        return player_xp_list

    def get_mob_values(self):
        """This function will retrive the mob values entered into the mob information
        boxes."""

        # counts the total amount of mobs, used for naming new mob objects
        mob_counter = 1
        # set the index of the mob_numbers list
        number_set_index = 0
        # prepare empty mob list
        mob_list = []
        # list of valid inputs for the cr feilds
        valid_crs = ['0', '1/8', '1/4', '1/2', '1', '2', '3', '4', '5', '6', '7', '8',
                     '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                     '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']

        for mob_set in self.mob_crs:

            mob_cr = mob_set.toPlainText()

            if mob_cr is None or mob_cr == '':

                number_set_index = number_set_index + 1

                continue

            if mob_set.toPlainText() not in valid_crs:

                error = "ERROR: Monster CR ratings must be between 0 and 30."

                self.show_error(error)

                continue

            number_mobs_in_set = self.mob_numbers[number_set_index].toPlainText()

            if number_mobs_in_set is None or number_mobs_in_set == '':

                number_set_index = number_set_index + 1

                continue

            try:

                number_mobs_in_set = int(number_mobs_in_set)

            except ValueError:

                number_set_index = number_set_index + 1

                error = ('ERROR: Invalid entry in monster information.\n'
                         'Please ensure you have only entered numeric values.')

                self.show_error(error)

                continue

            added_mobs = 0

            while number_mobs_in_set > added_mobs:

                mob_name = 'mob_' + str(mob_counter)

                mob_list.append(mob.Mob(mob_name, mob_cr))

                added_mobs = added_mobs + 1

                mob_counter = mob_counter + 1

            number_set_index = number_set_index + 1

        passed_encounter_xp = mob.get_challenge_total(mob_list)

        return passed_encounter_xp

    def set_xp_values(self, player_xp_list, passed_encounter_xp):
        """This function will update the app party xp values."""

        self.easy_xp = player_xp_list[0]
        self.med_xp = player_xp_list[1]
        self.hard_xp = player_xp_list[2]
        self.deadly_xp = player_xp_list[3]
        self.daily_xp = player_xp_list[4]

        self.party_xp_output.setText(f'{self.easy_xp}\n'
                                     f'\n{self.med_xp}\n'
                                     f'\n{self.hard_xp}\n'
                                     f'\n{self.deadly_xp}\n'
                                     f'\n{self.daily_xp}')

        self.encounter_xp = passed_encounter_xp

        self.encounter_xp_output.setText(f'{self.encounter_xp}')

        self.set_encounter_diff(player_xp_list, passed_encounter_xp)

    def set_encounter_diff(self, player_xp_list, passed_encounter_xp):
        """This function will update the encounter difficulty text for the app."""

        player_xp_list.reverse()

        # remove 'Daily' value from passed list.
        del player_xp_list[0]

        difficulty_list = ['Deadly', 'Hard', 'Medium', 'Easy']

        index = 0

        for value in player_xp_list:

            if passed_encounter_xp >= value:

                self.encounter_difficulty = difficulty_list[index]

                self.encounter_diff_label.setText(
                    f'Difficulty = {self.encounter_difficulty}')

                return

            index = index + 1


def draw_top_labels(self):
    """This function creates the labels for the top of the gui."""

    # Setup instructions
    self.instructions_label = qtw.QLabel(self)
    self.instructions_label.setText('Enter the the encouter information '
                                    'then press the calculate button.')
    self.instructions_label.setFont(Big_Font)
    self.instructions_label.setGeometry(150, 10, 600, 25)

    # Setup top labels
    self.player_level_label = qtw.QLabel(self)
    self.player_level_label.setText('Level  X  Number')
    self.player_level_label.setFont(Regular_Font)
    self.player_level_label.setGeometry(115, 50, 150, 15)

    self.mob_cr_label = qtw.QLabel(self)
    self.mob_cr_label.setText('CR  X  Number')
    self.mob_cr_label.setFont(Regular_Font)
    self.mob_cr_label.setGeometry(680, 50, 150, 15)


def draw_calculate_button(self):
    """This function creates the calculate button for the gui and links it to the calculate
    clicked function above."""

    calculate_button = qtw.QPushButton(self)
    calculate_button.setText('Calculate')
    calculate_button.setFont(Big_Font)
    calculate_button.setStyleSheet('background-color: rgb(90, 0, 0);')
    calculate_button.setGeometry(330, 180, 100, 50)
    calculate_button.clicked.connect(self.calculate_clicked)

    return calculate_button


def draw_player_output_labels(self):
    """This function draws the labels and outputs of the player party xp."""

    self.player_output_labels = qtw.QLabel(self)
    self.player_output_labels.setText('Difficulty --> XP Values\n'
                                      '\nEasy:\n'
                                      '\nMedium:\n'
                                      '\nHard:\n'
                                      '\nDeadly:\n'
                                      '\nDaily:\n')
    self.player_output_labels.setFont(Regular_Font)
    self.player_output_labels.setGeometry(20, 320, 200, 250)


def draw_player_xp(self):
    """This function will draw the player exp values on the gui."""

    self.party_xp_output = qtw.QLabel(self)
    self.party_xp_output.setText(f'{self.easy_xp}\n'
                                 f'\n{self.med_xp}\n'
                                 f'\n{self.hard_xp}\n'
                                 f'\n{self.deadly_xp}\n'
                                 f'\n{self.daily_xp}')
    self.party_xp_output.setFont(Regular_Font)
    self.party_xp_output.setGeometry(100, 365, 200, 180)


def draw_encouter_output_labels(self):
    """This function will draw the encounter output labels to the gui."""

    self.encounter_output_label = qtw.QLabel(self)
    self.encounter_output_label.setText('v Encounter XP v')
    self.encounter_output_label.setFont(Regular_Font)
    self.encounter_output_label.setGeometry(580, 450, 120, 20)


def draw_encounter_xp(self):
    """This function will draw the encounter xp to the gui."""

    self.encounter_xp_output = qtw.QLabel(self)
    self.encounter_xp_output.setText(f'{self.encounter_xp}')
    self.encounter_xp_output.setFont(Regular_Font)
    self.encounter_xp_output.setGeometry(550, 480, 200, 20)


def draw_encounter_diff(self):
    """This function will draw the determined difficulty of the encounter on the gui."""

    self.encounter_diff_label = qtw.QLabel(self)
    self.encounter_diff_label.setText(
        f'Difficulty = {self.encounter_difficulty}')
    self.encounter_diff_label.setFont(Big_Font)
    self.encounter_diff_label.setGeometry(300, 350, 200, 30)


def main():
    """Main function of the program, which will load all the data from the other modules
    and display the GUI to the user."""

    q_app = qtw.QApplication(sys.argv)
    encounter_app = EncounterGui()
    encounter_app.show()
    sys.exit(q_app.exec_())  # sets up window exit button


main()
