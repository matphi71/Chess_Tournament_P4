from models.players import PlayersIdentity
from models.tournament import Tournament
from models.match import Match

from view import base
from models import players
from controller import base


def main():

    run = base.Controller_player()
    run.go()


if __name__ == "__main__":
    main()








