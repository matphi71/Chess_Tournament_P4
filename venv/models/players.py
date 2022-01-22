'''model players'''

from tinydb import TinyDB, Query

db = TinyDB('db.json')
User = Query()
player_db = db.table('players')


class PlayersIdentity:

    def __init__(self,family_name = None, name = None):
        self.family_name = family_name
        self.name = name
    
    def __str__():
        return f"{self.family_name}, {self.name}"

    def __repr__():
        pass

    def serialized_players(self):
        serialized_players = {}
        serialized_players ['family_name'] = self.family_name
        serialized_players ['name'] = self.name
        return serialized_players

    def deserialized_players(self):
        family_name = serialized_players ['family_name']
        name = serialized_players ['name']
        deserialized_players = PlayersIdentity(family_name=family_name, name=name)
        return  deserialized_players

    def add_player_to_database(self):
        player_db.truncate()
        player_db.insert(self.deserialized_players())
        return
    
    '''def add_player_to_database(self):
        new_players = players_model.PlayersIdentity().serialized_players()
        players_model.player_db.truncate()
        added_players = 0
        while added_players != NUMBER_OF_PLAYERS_TO_ADD:
            players_model.PlayersIdentity().add_player_to_database()
            #players_model.player_db.insert(new_players)
            added_players += 1'''






