#from models.tournament import Tournament
#from models.match import Match

from controller import controlleur_players, controlleur_tournament


def main():

    run_players = controlleur_players.ControllerPlayer()
    run_players.go()
    run_tournament = controlleur_tournament.TournamentSetUp()
    run_tournament.go()


if __name__ == "__main__":
    main()








