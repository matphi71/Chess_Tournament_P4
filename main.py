from controller import controller_player, controller_tournament, controller_round
from models import model_tournament


def main():

    model_tournament.tournaments_db.truncate()
    tournament = controller_tournament.TournamentSetUp()
    tournament.go()



if __name__ == "__main__":
    main()








