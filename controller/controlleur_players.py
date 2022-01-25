""" controller players """


from tinydb import Query

from view.view_players import View
from models import model_players
from models.model_players import PlayersIdentity
from models import model_tournament

query = Query()

NUMBER_OF_PLAYERS_TO_ADD = 4


class ControllerPlayer:

    def __init__(self):
        self.view = View
        self.model = PlayersIdentity

    def collecting_players_infos(self):

        """ retrieveing players Identity """

        inputs = self.view().get_players_inputs()
        family_name = inputs['family_name']
        name = inputs['name']
        ranking = inputs['ranking']
        return self.model(family_name, name, ranking)

    def add_players_to_database(self):

        """ inserting players to database """
        
        model_players.player_db.truncate()
        added_players = 0
        while added_players != NUMBER_OF_PLAYERS_TO_ADD:
            self.collecting_players_infos().add_player_to_database()
            added_players += 1
        return

    def serialized(self):
        print(self.collecting_players_infos().serialized_players())
        return

    def deserialized(self):
        return print(self.collecting_players_infos().deserialized_players())

    def sort_players_by_ranking(self):

        """ sorting players to make pairs according to the swiss tournament system """

        players_list = []
        for players in model_players.player_db:
            players_list.append(players)
        sorted_players_list = sorted(players_list, key=lambda k: k['ranking'])
        return sorted_players_list

    def get_pairs_of_players_first_tour(self):
        half_players_list = int(len(self.sort_players_by_ranking())/2)
        print(half_players_list)
        split_in_half_lower_rankings = self.sort_players_by_ranking()[:half_players_list]
        split_in_half_higher_rankings = self.sort_players_by_ranking()[half_players_list:]
        print(list(zip(split_in_half_lower_rankings, split_in_half_higher_rankings)))

    def adjust_points(self):
        pass

    def go(self):
        #Controller_player().collecting_players_infos()
        ControllerPlayer().add_players_to_database()
        #ControllerPlayer().serialized()
        #ControllerPlayer().deserialized()
        #ControllerPlayer().sort_players_by_ranking()
        ControllerPlayer().get_pairs_of_players_first_tour()



            
    
















