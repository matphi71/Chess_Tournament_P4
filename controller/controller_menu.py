""" controller menu """

from controller import controller_tournament, controller_player
from models import model_tournament
from view.view_players import View
from view.view_menu import ViewMenu


class TournamentMenu:

    def __init__(self):
        self.view = View
        self.model = model_tournament

    @staticmethod
    def welcome_message():
        ViewMenu().welcome_message()

    def options_access(self):
        answer = ViewMenu().menu_options()
        while answer != '4':
            if answer == '1':
                ViewMenu().starting_tournament_message()
                controller_tournament.TournamentSetUp().go()
                break
            elif answer == '2':
                controller_player.ControllerPlayer().updating_player_ranking()
                break
            elif answer == '3':
                if ViewMenu().view_report_display_per_category_y_or_n() == 'Y':
                    response = ViewMenu().report_detail_options()
                    while response != '5':
                        if response == '1':
                            ViewMenu().print_report_alphabetical_list()
                            break
                        elif response == '2':
                            ViewMenu().print_report_ranking_list()
                            break
                        elif response == '3':
                            ViewMenu().print_tournament_list()
                            break
                        elif response == '4':
                            ViewMenu().print_match_list()
                            break
                        else:
                            break
                else:
                    ViewMenu().print_report_alphabetical_list()
                    ViewMenu().print_report_ranking_list()
                    ViewMenu().print_tournament_list()
                    ViewMenu().print_match_list()
                    break
        else:
            ViewMenu().ending_message()
            return
        return self.options_access()

    def run(self):
        #controller_player.ControllerPlayer().add_players_to_database()
        self.welcome_message()
        self.options_access()

