""" view """

from models.model_players import player_db
from models.model_round import round_db
from models.model_tournament import tournaments_db


class View:

    def get_players_inputs(self):

        """players identity display"""

        print("Please enter a new player")
        family_name = input("FAMILY NAME:")
        name = input("NAME:")
        birth_date = input("BIRTH-DATE:")
        gender = input("GENDER:")
        ranking = int(input("RANKING: "))
        if ranking != int and ranking <= 0:
            message = f"Please enter a positive and integer ranking number"
            raise Exception(message)
        else:
            ranking
        return {'family_name': family_name, 'name': name, 'birth_date': birth_date, 'gender': gender,
                'ranking': ranking}

    @staticmethod
    def ranking_change_option():
        option = input("To change player rank print Y: ")
        while option not in "Yy" and option in "":
            option = input("To change player rank print Y: ")
            continue
        return option

    @staticmethod
    def get_tournament_inputs():

        """creation of  new tournament"""

        print("Please enter the following informations to create your new tournament: ")
        tournament_name = input("TOURNAMENT NAME: ")
        place = input("PLACE: ")
        date = input("DATE: ")
        time_control = input("Enter time control: bullet, blitz or rapid?\n")
        manager_notes = input("Enter comments if needed:\n")
        return {'tournament_name': tournament_name, 'place': place, 'date': date, 'time_control': time_control,
                'manager_notes': manager_notes}

    def new_results_match_inputs_player_1(self):

        """ points attribution to player 1 """

        new_result_player_1 = int(input("enter result of player n°1: "))
        return new_result_player_1

    def new_results_match_inputs_player_2(self):

        """ points attribution to player 2 """

        new_result_player_2 = int(input("enter result of player n°2: "))
        return new_result_player_2

    @staticmethod
    def see_tournament_results_y_or_n():
        answer = input("would you like to obtain a report of all tournaments? (Yes print Y, No print N): ")
        while answer not in "yYnN" or answer in "":
            answer = input("would you like to obtain a report of all tournaments? (Yes print Y, No print N): ")
            continue
        return answer

    @staticmethod
    def print_tournament_results():
        print("\nTOURNAMENT FINAL RESULTS:\n")
        for players in player_db:
            print(f"{players['family_name']} gets, {players['score']} points")

    def print_report_display(self):
        alphabetical_participants_players_list = []
        ranking_participant_players_list = []
        tournament_list = []
        rounds_list = []
        for information in player_db:
            alphabetical_participants_players_list.append(information)
            ranking_participant_players_list.append(information)
        alphabetical_participants_players_list = sorted(alphabetical_participants_players_list, key=lambda
            k: k['family_name'])
        ranking_participant_players_list = sorted(ranking_participant_players_list, key=lambda k: k['ranking'])
        print("\nALPHABETICAL PARTICIPANTS PLAYERS LIST:\n ")
        for participants in alphabetical_participants_players_list:
            print(participants['family_name'], participants['name'] + ' - birth date:', participants['birth_date']
                    + ' - ranking:', participants['ranking'])
        print("\nRANKING PARTICIPANTS PLAYERS LIST:\n")
        for participants in ranking_participant_players_list:
            print(participants['family_name'], participants['name'] + ' - birth date:', participants['birth_date']
                    + ' - ranking:', participants['ranking'])
        # print('\n'.join(map(str, ranking_participant_players_list)))
        print("\nTOURNAMENT LIST:\n")
        for tournament in tournaments_db:
            print(f"Tournament name: {tournament['tournament_name']}\n Place:  {tournament['place']}\n Date:  "
                  f"{tournament['date']}\n Number of rounds: {tournament['number_of_rounds']}\n Time control:  "
                  f"{tournament['time_control']}\n  Manager notes: {tournament['manager_notes']}\n Players index: "
                  f"{tournament['players_index']}\n Tournament rounds list: {tournament['rounds_list']}")
        # tournament = tournament_db.all()
        # tournament_list.append(tournament)
        # print('\n'.join(map(str, tournament_list)))
        print("\nMATCH LIST:\n")
        for tuples_match in round_db:
            match_list = []
            i = 0
            for pairs in tuples_match['pairs_to_play']:
                pairs = pairs[0][0], pairs[1][0]
                pairs = tuple(pairs)
                match_list.append(pairs)
            i += 1
            print(f"Match n°{i}: {match_list[1:-1]}")





