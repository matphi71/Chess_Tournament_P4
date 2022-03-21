""" view """

from termcolor import colored
import datetime


class View:
    @staticmethod
    def get_players_inputs():

        """players identity display"""

        print("\nPlease enter a new player:\n")
        family_name = input("FAMILY NAME:  ")
        while family_name.isalpha() is False and family_name.isspace() is False:
            print("\n" + colored("Enter a valid family name", "red"))
            family_name = input("FAMILY NAME:  ")
        family_name = family_name.upper()
        name = input("NAME:  ")
        while name.isalpha() is False and name.isspace() is False:
            print("\n" + colored("Enter a valid name", "red"))
            name = input("NAME:  ")
        name = name.capitalize()
        birth_date = input("BIRTH-DATE (D.M.Y):  ")
        try:
            datetime.datetime.strptime(birth_date, "%d.%m.%Y")
        except ValueError:
            print("\n" + colored("Enter a valid date", "red"))
            birth_date = input("BIRTH-DATE (D.M.Y):  ")
        gender = input("GENDER (M or F):  ")
        while gender not in "MmFf":
            print("\n" + colored("I didn't understand your answer", "red"))
            gender = input("GENDER (M or F):  ")
        ranking = int(input("RANKING: "))
        while ranking != int and ranking <= 0:
            print(
                "\n"
                + colored("Please enter a positive and integer ranking number", "red")
            )
            ranking = int(input("RANKING: "))
        return {
            "family_name": family_name,
            "name": name,
            "birth_date": birth_date,
            "gender": gender,
            "ranking": ranking,
        }

    @staticmethod
    def player_family_name_ranking_change():
        player_family_name = input("Players family name's ranking to change: ")
        while not player_family_name.isalpha() or player_family_name in "":
            print("Enter a valid family name")
            player_family_name = input("FAMILY NAME:  ")
        return player_family_name

    @staticmethod
    def ranking_change():
        new_ranking = input("New ranking: ")
        while not new_ranking.isnumeric() or new_ranking in "":
            print("I didn't understand you answer")
            new_ranking = input("New ranking: ")
        return new_ranking
