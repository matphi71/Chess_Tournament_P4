""" controller players """


from tinydb import Query

from view.view_players import View
from models import model_players
from models.model_players import PlayersIdentity
from models import model_tournament

query = Query()

NUMBER_OF_PLAYERS_TO_ADD = 3


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
        return self.collecting_players_infos().serialized_players()

    def deserialized(self):
        print(self.collecting_players_infos().deserialized_players())
        return

    def sort_players_by_ranking(self):
        deserialized_players = []
        for players in model_players.player_db:
            deserialized_players.append(players)
        print(deserialized_players)


    '''def players_sorting(self):
            players_list = []
            players_list_elements = players.player_db.all()
            #players_list_elements.sort()
            #sorted(players_list_elements[2])
            #players.db.search ('ranking' == all)#(query.players.player_db('ranking' == any)) #(query.type == 'name'))
            for row in players_list_elements:
            #print(row)
            players_list.append(row)
        ranking_list = []
        index = 2
        for i in range(NUMBER_OF_PLAYERS_TO_ADD):
            ranking_list.append(players_list[index])
            index += 3
        print(ranking_list)
        return'''

        #self.adjust_points_number()
        #self.get_first_pairs_of_players()
        #running = True
        #while running:

            #self.views.create_new_matchs()
            #self.get_rest__pairs_of_players()
            #self.adjust_points_number()
            #self.views(self.adjust_points_number())

    def go(self):
        #Controller_player().collecting_players_infos()
        ControllerPlayer().add_players_to_database()
        ControllerPlayer().sort_players_by_ranking()


"new round 4 max"
'''def generate_a_round(self):
            players_identity = PlayersIdentity
            players_view = Players_View
            players_identity.familly_name = players_view.familly_name

            self.generate_a_round().append(list)
            return list
    def players_list(self):
        self.players_list = []
        
        players_dentity = PlayersIdentity
        enter_identity = PlayersView.enter_identity()
        players_list.append(familly_name)
        print(players_list)


        #players_list = players_list.append(players_identity())
        #while len(players_list)<NUMBER_OF_PLAYERS:'''



            
    
















