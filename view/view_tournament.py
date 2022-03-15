""" view tournament """

from termcolor import colored
import datetime

from models.model_players import player_db


class ViewTournament:

    @staticmethod
    def get_tournament_inputs():

        """creation of  new tournament"""

        print("\nPlease enter the following informations to create your new tournament:\n")
        tournament_name = input("TOURNAMENT NAME: ")
        tournament_name = tournament_name.title()
        place = input("PLACE: ")
        while not place.isalpha() and place.isspace() is False:
            print('\n' + colored('Please enter a valid name', 'red'))
            place = input("PLACE: ")
        date = input("TOURNAMENT DATE (D.M.Y): ")
        try:
            datetime.datetime.strptime(date, '%d.%m.%Y')
        except ValueError:
            print('\n' + colored('Please enter a valid date', 'red'))
            date = input("TOURNAMENT DATE (D.M.Y): ")
        time_control = input("\nEnter time control: Bullet, Blitz or Rapid?\n")
        time_control = time_control.capitalize()
        while time_control:
            if time_control == 'Bullet':
                print(time_control)
                break
            elif time_control == 'Blitz':
                print(time_control)
                break
            elif time_control == 'Rapid':
                print(time_control)
                break
            else:
                print('\n' + colored('Please enter a valid time control', 'red'))
                time_control = input("\nEnter time control: Bullet, Blitz or Rapid?\n")
                time_control = time_control.capitalize()
        manager_notes = input("\nEnter comments if needed:\n")
        return {'tournament_name': tournament_name, 'place': place, 'date': date, 'time_control': time_control,
                'manager_notes': manager_notes}

    @staticmethod
    def new_results_match_inputs_player_1():

        """ points attribution to player 1 """

        new_result_player_1 = int(input("enter result of player n°1: "))
        return new_result_player_1

    @staticmethod
    def new_results_match_inputs_player_2():

        """ points attribution to player 2 """

        new_result_player_2 = int(input("enter result of player n°2: "))
        return new_result_player_2

    @staticmethod
    def see_tournament_report_y_or_n():
        answer = input("Would you like to obtain a report of all tournaments? (Yes print Y, No print N): ")
        while answer not in "yYnN" or answer in "":
            print('\n' + colored("I didn't understand you answer: ", 'red'))
            answer = input("Would you like to obtain a report of all tournaments? (Yes print Y, No print N): ")
        return answer

    @staticmethod
    def print_tournament_results():
        print("\nTOURNAMENT FINAL RESULTS:\n")
        for players in player_db:
            print(f"{players['family_name']} has {players['score']} points")
