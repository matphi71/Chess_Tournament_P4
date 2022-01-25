""" controller Tournament"""

from view.view_players import View
from models import model_tournament
from models.model_tournament import Tournament

NUMBERS_OF_TURNS = 4


class TournamentSetUp:
    
    def __init__(self):
        self.model = Tournament
        self.view = View

    def collecting_tournament_infos(self):
        inputs = self.view().get_tournament_inputs()
        tournament_name = inputs['tournament_name']
        place = inputs['place']
        return self.model(tournament_name, place)
    
    def add_tournament_to_database(self):
        model_tournament.tournaments_db.truncate()
        return self.collecting_tournament_infos().add_tournament_to_database()

    def go(self):
        TournamentSetUp().add_tournament_to_database()
