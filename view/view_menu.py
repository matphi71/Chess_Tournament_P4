""" view menu """

import pyfiglet
from termcolor import colored

from models.model_players import player_db
from models.model_round import round_db
from models.model_tournament import tournaments_db
from controller.controller_tournament import NUMBERS_OF_ROUNDS


class ViewMenu:

    @staticmethod
    def welcome_message():
        f = pyfiglet.Figlet(font='small', justify='center', width=140)
        print('\n\n' + colored(f.renderText('WELCOME  TO  YOUR  TOURNAMENT SYSTEM     MANAGER'), 'yellow'))

    @staticmethod
    def starting_tournament_message():
        print('\n'+" "*60 + colored('NEW TOURNAMENT', 'yellow')+'\n')

    @staticmethod
    def ending_message():
        f = pyfiglet.Figlet(font='small', justify='center', width=140)
        print('\n\n'+colored(f.renderText('GOODBYE'), 'yellow'))

    @staticmethod
    def menu_options():
        print('\n'+" "*50 + colored("*** CHESS TOURNAMENT MANAGER MENU ***", 'blue') + '\n')
        answer = input(("Please choose an option:\n\n* START A NEW TOURNAMENT = 1   * CHANGE PLAYER'S RANK = 2   "
                        "* REPORT DISPLAY = 3   * ENDING TOURNAMENT = 4\n").center(100))
        while answer not in "1234" or answer in "":
            print(colored("\nEnter a number between 1 and ", 'red')+'\n')
            answer = input(("Please choose an option:\n\n* START A NEW TOURNAMENT = 1   * CHANGE PLAYER'S RANK = 2   "
                            "* REPORT DISPLAY = 3   * ENDING TOURNAMENT = 4\n").center(100))
        return answer

    @staticmethod
    def report_detail_options():
        answer = input(("Please choose an option:\n\n* ALPHABETICAL PARTICIPANTS PLAYERS LIST = 1 "
                        "* RANKING PARTICIPANTS PLAYERS LIST = 2   * TOURNAMENT LIST = 3   * MATCH LIST = 4"
                        "  * STOP VIEWING TOURNAMENT DETAILS = 5\n").center(100))
        while answer not in "12345" or answer in "":
            print(colored("\nEnter a number between 1 and 5", 'red') + '\n')
            answer = input(("Please choose an option:\n\n* ALPHABETICAL PARTICIPANTS PLAYERS LIST = 1 "
                            "* RANKING PARTICIPANTS PLAYERS LIST = 2   * TOURNAMENT LIST = 3   * MATCH LIST = 4"
                            "  * STOP VIEWING TOURNAMENT DETAILS = 5\n").center(100))
        return answer

    @staticmethod
    def view_report_display_per_category_y_or_n():
        answer = input("\nWould you like to obtain a tournament report per category? (Yes print Y, No print N): ")
        while answer not in "yYnN" or answer in "":
            print('\n' + colored("I didn't understand you answer: ", 'red'))
            answer = input("would you like to obtain a tournament report per category? (Yes print Y, No print N): ")
        return answer.upper()

    @staticmethod
    def print_report_alphabetical_list():
        alphabetical_participants_players_list = []
        for information in player_db:
            alphabetical_participants_players_list.append(information)
        alphabetical_participants_players_list = sorted(alphabetical_participants_players_list, key=lambda
            k: k['family_name'])
        print('\n' + colored('ALPHABETICAL PARTICIPANTS PLAYERS LIST:', 'yellow') + '\n')
        for participants in alphabetical_participants_players_list:
            print(participants['family_name'], participants['name'] + ' - birth date:', participants['birth_date']
                  + ' - ranking:', participants['ranking'])
        return

    @staticmethod
    def print_report_ranking_list():
        ranking_participant_players_list = []
        for information in player_db:
            ranking_participant_players_list.append(information)
        ranking_participant_players_list = sorted(ranking_participant_players_list, key=lambda k: int(k['ranking']))
        print('\n' + colored('RANKING PARTICIPANTS PLAYERS LIST:', 'yellow') + '\n')
        for participants in ranking_participant_players_list:
            print(participants['family_name'], participants['name'] + ' - birth date:', participants['birth_date']
                  + ' - ranking:', participants['ranking'])
        return

    @staticmethod
    def print_tournament_list():
        rounds_list = []
        print('\n' + colored('TOURNAMENT LIST:', 'yellow') + '\n')
        for tournament in tournaments_db:
            for key, value in tournament.items():
                key = key.upper()
                if key == 'PLAYERS_INDEX':
                    print(colored('PLAYERS INDEX ', 'green'), end=' ')
                    i = 0
                    while i <= len(value):
                        try:
                            item = f" {value[i][1]}: id n° {value[i][0]}"
                            i += 1
                            print(item, end="  ")
                        except IndexError:
                            break
                elif key == 'ROUNDS_LIST':
                    print(f"\n{colored(key, 'green')}:")
                    for i in range(NUMBERS_OF_ROUNDS):
                        rounds_list.append(value[0][i])
                    for detail in rounds_list:
                        pair_list = [detail['pairs_to_play']]
                        for pairs in pair_list:
                            print("Pairs to play: ", end='')
                            for pair in pairs:
                                print(tuple(pair), end='')
                            print(f"\nBeginning time: {detail['beginning_time']}")
                            print(f"Ending time: {detail['ending_time']}\n")
                else:
                    print(f"{colored(key, 'green')} : {value}")
        return

    @staticmethod
    def print_match_list():
        print('\n' + colored('MATCH LIST:', 'yellow') + '\n')
        i = 0
        for tuples_match in round_db:
            for pairs in tuples_match['pairs_to_play']:
                pairs = f"{pairs[0][0]} against {pairs[1][0]}"
                i += 1
                print(f"Match n°{i}: {pairs}")
        return
