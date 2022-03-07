from controller import controller_tournament, controller_player, controller_round
from view import view_menu

from models import model_tournament


def main():
    menu = view_menu.ViewMenu()
    menu.welcome_message()
    players = controller_player.ControllerPlayer()
    players.add_players_to_database()
    players.updating_player_score()
    tournament = controller_tournament.TournamentSetUp()
    tournament.go()



if __name__ == "__main__":
    main()








