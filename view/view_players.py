""" view """


class View:

    def get_players_inputs(self):

        """players identity display"""

        print("Please enter a player")
        family_name = input("FAMILY NAME:")
        name = input("NAME:")
        # birth_date = input("BIRTH-DATE:")
        # gender = input("GENDER:")
        ranking = int(input("RANKING: "))
        if ranking != int and ranking <= 0: #or none:
            message = f"Please enter a positive and integer ranking number"
            raise Exception(message)
        else:
            ranking
        return {'family_name': family_name, 'name': name, 'ranking': ranking}
        #, 'birth_date':birth_date, 'gender':gender,

    def get_tournament_inputs(self):

        """creation of  new tournament"""

        T = 4
        print("Please enter the following informations to create your new tournament: ")
        tournament_name = input("TOURNAMENT NAME: ")
        place = input("PLACE: ")
        #date = input("date: ")
        #turn_numbers = ("T")
        #rounds = liste instances rondes
        #players = liste des indices correspondant instances joueurs stockées en mémoire
        #time control = input(" chosse one of the following time controlleur: bullet - blitz - fast stroke: ")
        #description = input("please enter you general comments if needed: ")
        return {'tournament_name': tournament_name, 'place': place }#, 'date':date, 'turn_numbers':turn_numbers}

    '''def new_match_inputs(self):
            """Inform of match to play"""
            for round_number in range(NUMBERS_OF_MATCHS):
                print(f"ready for Round n° {round_number}?")
                choice = input("y/n: ")
                if choice == "n":
                    return False
            return True'''
    def round_inputs(self):
        pass

    def new_results_match_inputs_player_1(self):

        """ points attribution to player 1 """

        new_result_player_1 = int(input("enter result of player n°1: "))
        return new_result_player_1

    def new_results_match_inputs_player_2(self):

        """ points attribution to player 2 """

        new_result_player_2 = int(input("enter result of player n°2: "))
        return new_result_player_2
