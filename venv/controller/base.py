'''controller'''


from tinydb import TinyDB, Query

from view.base import View
from models.players import PlayersIdentity
from models.tournament import Tournament
#from models.round import RoundView

query = Query()

NUMBER_OF_PLAYERS_TO_ADD = 1
NUMBERS_OF_TURNS = 4


class Controller_player: 
    
    def __init__(self):
        self.view = View
        self.model = PlayersIdentity

        
    def collecting_players_infos(self):
        '''retrieveing players ID'''
        player = PlayersIdentity()
        inputs = self.view().get_players_inputs()
        player.family_name = inputs['family_name']
        player.name = inputs['name']


        #player.family_name = inputs.get('family_name')
        #player.name = inputs.get('name')
        #print(player.family_name)'''
        #P = PlayersIdentity(fn, n)
        #print (P.family_name)
        #inputs = View().get_players_inputs()
        #print(inputs.get('name'))
        #player = players.PlayersIdentity()
        print(getattr(player, 'name'))
        #family_name = PlayersIdentity(family_name=inputs(familyname))
        #d = PlayersIdentity('jean', 'bon')
        #print(d)
        #print(hasattr(player,'family_name'))
        '''PlayersIdentity.print(PlayersIdentity(family_name = inputs['family_name']))
        PlayersIdentity.print(PlayersIdentity(name=inputs['name']))'''
        '''family_name = PlayersIdentity
        fn = family_name(family_name)
        fn = inputs.get('family_name')
        name = PlayersIdentity
        n = name(name)
        n = inputs.get('name')
        print(fn, n)'''
        return

    def add_player_to_database(self):
        new_players = PlayersIdentity().serialized_players()
        players_model.player_db.truncate()
        added_players = 0
        while added_players != NUMBER_OF_PLAYERS_TO_ADD:
            PlayersIdentity().add_player_to_database()
            #players_model.player_db.insert(new_players)
            added_players += 1

    '''def serialized_player(self):
        inputs = self.collecting_players_infos()
        serialized_players = {'family_name':inputs[0], 'age':inputs[1]}
        print(serialized_players)
        return serialized_player

    def deserialized_players(self):
        serialized_players = players_model.player_db.all()
        player_1 = serialized_players[0]
        rint(player_1)'''


    '''def get_first_pairs_of_players(self):
        pass

        def adjust_points_number(self):
            new_points = self.views.new_results
            return new_points
            #winner = self.players[0]


        def get_rest__pairs_of_players(self):
            # repeat until end of tournement
            pass'''

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

    def new_tournament(self):
        ''' receiving datas from the view'''
        tournament_model.tournaments_db.truncate()
        new_tournament_menu = View().new_tournament_menu()
        return new_tournament_menu

        #self.adjust_points_number()
        #self.get_first_pairs_of_players()
        #running = True
        #while running:

            #self.views.create_new_matchs()
            #self.get_rest__pairs_of_players()
            #self.adjust_points_number()
            #self.views(self.adjust_points_number())

    def setting_up_new_tournament(self):
        '''storing datas'''
        tournament.Tournament().new_tournament_infos()

    def turns(self):
        pass
        #with open (players) as players_database:
        #print(players_database[])#players.player_db.all())
        #players_database = players.player_db.all()
        #print(players.player_db.all())
            
        

    def go(self):
        #self.add_player_to_database()
        #print(players.player_db, tournament.tournaments_db)
        #self.setting_up_new_tournament()
        #self.adding_players()
        #self.players_sorting()
        #self.turns()
        cont = Controller_player()
        cont.collecting_players_infos()
        #self.add_player_to_database()
        #self.deserialized_players()
        #self.serialized_players()
        #players_model.PlayersIdentity
        #players_model.PlayersIdentity().serialized_players()
        pl = PlayersIdentity()
        print(getattr(pl, 'family_name'))


        #PlayersIdentity().print()
        #View().get_players_inputs()




        

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

'''from views.players import PlayersView
from models.players import PlayersIdentity

#récupération des données depuis la vue pour les envoyer à la db 
class Controller_players:
    def __init__(self):
        #views
        self.view = view
                
        #models
        self.players = self.get_list_players()
        self.tournament = tournament
        self.rounds = rounds
        self.match = match
        self.datas = datas

    def get_list_players(self):
        players_list = []
        players_list.append(PlayersView.get_players_identity())
        return players_list

    def run(self):
        self.get_list_players()'''



            
    
















