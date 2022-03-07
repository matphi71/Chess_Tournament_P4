""" controller menu """

from models.model_players import player_db
from view.view_menu import ViewMenu


class TournamentMenu:

    def __init__(self):
        self.view = ViewMenu

    def print_welcome_message(self):
        self.view.welcome_message()

    def player_ranking_access(self):
        pass

    def players_to_enter(self):
        pass
        #player_db.update('score', val), where('family_name') == players_list[i]



