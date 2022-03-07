""" view menu """

import pyfiglet
from termcolor import cprint, colored

from models.model_players import player_db
from models.model_round import round_db
from models.model_tournament import tournaments_db


class ViewMenu:

    @staticmethod
    def welcome_message():
        f = pyfiglet.Figlet(font='small', justify='center', width=140)
        print(colored(f.renderText('WELCOME  TO  YOUR  TOURNAMENT SYSTEM     MANAGER'), 'yellow'))
        # print('\n\n\n' + colored('                                           WELCOME TO YOUR SYSTEM MANAGER', 'blue')
        # +'\n\n\n')

    @staticmethod
    def player_ranking_access(self):
        answer = input("Change player's ranking (Y/N)?: ")
        while answer not in "YyNn" or answer in "":
            answer = input("Change player's ranking (Y/N)?: ")
            continue
        return answer



