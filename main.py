from tinydb import TinyDB, Query
import json

from controller import controlleur_players, controlleur_tournament
from models import model_round
from models import model_match

db = TinyDB('db.json')
User = Query


def main():

    controlleur_players.ControllerPlayer().add_players_to_database()
    controlleur_tournament.TournamentSetUp().add_round_to_database()
    controlleur_players.ControllerPlayer().sort_players_by_score()


if __name__ == "__main__":
    main()








