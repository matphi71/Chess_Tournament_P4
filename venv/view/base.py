'''view'''

class View:

#dictionnaire {tournament_name...}
    def new_tournament_menu(self):
        '''creation of  new tournament'''
        print("Please enter bellow the infos to create your new tournament")
        tournament_name = input("tournament_name: ")
        #place = input("place: ")
        #date = input("date: ")
        return tournament_name

    def create_new_match(self):
            """Inform of match to play"""
            for round_number in range(NUMBERS_OF_MATCHS):
                print(f"ready for Round n° {round_number}?")
                choice = input("y/n: ")
                if choice == "n":
                    return False
            return True


    def get_players_inputs(self):
        '''players display'''
        print("Please enter a player")
        family_name = input("family name:")
        name = input("name:")
        #birth_date = input("birth_date:")
        #gender = input("gender:")
        #ranking = int(input("ranking:"))
        #if ranking != int and ranking <= 0 or none:
        #    message = (f"Please enter a positive and integer ranking number")
        #    raise Exception(message)
        #else:
        #   return ranking
        return {'family_name': family_name, 'name':name}


    def new_results(self):
        # nouveau classement pour générer une paire pour prochain match
        new_result = input("nouveau classment: ")
        return new_result
