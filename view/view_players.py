""" view """


class View:

    def get_players_inputs(self):

        """players identity display"""

        print("Please enter a player")
        family_name = input("family name:")
        name = input("name:")
        # birth_date = input("birth_date:")
        # gender = input("gender:")
        ranking = int(input("ranking: "))
        if ranking != int and ranking <= 0: #or none:
            message = f"Please enter a positive and integer ranking number"
            raise Exception(message)
        else:
            ranking
        return {'family_name':family_name, 'name':name, 'ranking':ranking }
        #, 'birth_date':birth_date, 'gender':gender,

    def get_tournament_inputs(self):

        """creation of  new tournament"""

        T = 4
        print("Please enter the following informations to create your new tournament: ")
        tournament_name = input("tournament_name: ")
        place = input("place: ")
        #date = input("date: ")
        #turn_numbers = ("T")
        #rounds = liste instances rondes
        #players = liste des indices correspondant instances joueurs stockées en mémoire
        #time control = input(" chosse one of the following time controlleur: bullet - blitz - fast stroke: ")
        #description = input("please enter you general comments if needed: ")
        return {'tournament_name':tournament_name, 'place':place }#, 'date':date, 'turn_numbers':turn_numbers}

    '''def new_match_inputs(self):
            """Inform of match to play"""
            for round_number in range(NUMBERS_OF_MATCHS):
                print(f"ready for Round n° {round_number}?")
                choice = input("y/n: ")
                if choice == "n":
                    return False
            return True'''

    def new_results(self):
        # nouveau classement pour générer une paire pour prochain match
        new_result = input("new ranking: ")
        return new_result
