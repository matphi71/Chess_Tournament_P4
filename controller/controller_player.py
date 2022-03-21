""" controller Player """

from tinydb import Query, where
from tinydb.operations import add

from view.view_players import View
from models import model_players
from models import model_round
from models.model_players import PlayersIdentity

query = Query()

NUMBER_OF_PLAYERS_TO_ADD = 8


class ControllerPlayer:
    def __init__(self):
        self.view = View
        self.model = PlayersIdentity

    def collecting_players_info(self):

        """Retrieving players identity"""

        inputs = self.view().get_players_inputs()
        family_name = inputs["family_name"]
        name = inputs["name"]
        birth_date = inputs["birth_date"]
        gender = inputs["gender"]
        ranking = inputs["ranking"]
        return self.model(family_name, name, birth_date, gender, ranking)

    def add_players_to_database(self):

        """inserting players to database"""

        # model_players.player_db.truncate()
        added_players = 0
        while added_players != NUMBER_OF_PLAYERS_TO_ADD:
            self.collecting_players_info().add_player_to_database()
            added_players += 1
        return

    @staticmethod
    def players_index():

        """To present player's name with it's doc_id number"""

        players_id_list = []
        for players_id in model_players.player_db:
            index = players_id.doc_id, players_id["family_name"]
            players_id_list.append(index)
        return players_id_list

    def serialized_players(self):
        return self.collecting_players_info().serialized_player()

    def deserialized_players(self):
        return self.collecting_players_info().deserialized_player()

    def sort_players_by_ranking(self):

        """sorting players to make pairs for first turn, according to the swiss tournament system"""

        players_list = []
        for players in model_players.player_db:
            players_list.append(players)
        sorted_players_list = sorted(
            players_list, key=lambda k: int(k["ranking"]), reverse=True
        )
        self.updating_players_score()
        return sorted_players_list

    def get_pairs_of_players_first_turn(self):

        """to get first turn pairs"""

        half_players_list = int(len(self.sort_players_by_ranking()) / 2)
        split_in_half_lower_rankings = self.sort_players_by_ranking()[
            :half_players_list
        ]
        split_in_half_higher_rankings = self.sort_players_by_ranking()[
            half_players_list:
        ]
        pairs_of_players_first_turn = list(
            zip(split_in_half_lower_rankings, split_in_half_higher_rankings)
        )
        return pairs_of_players_first_turn

    @staticmethod
    def updating_players_score():

        """updating automatically player's score in the players database"""

        new_score_list = []
        old_score_list = []
        players_list = []
        players_tuple = []
        rounds_len = []
        for last_score in model_players.player_db:
            old_score_list.append(last_score["score"])
        for number_of_rounds in model_round.round_db:
            rounds_len.append(number_of_rounds)
        rounds_len_list = len(rounds_len)
        tuples_to_search = model_round.round_db.get(doc_id=rounds_len_list)
        try:
            for tuples_match in tuples_to_search["pairs_to_play"]:
                for tuples in tuples_match:
                    players_tuple.append(tuples)
        except TypeError:
            pass
        players_tuple.sort()
        for players in players_tuple:
            new_score_list.append(float(players[1]))
            players_list.append(players[0])
        for i, val in enumerate(new_score_list):
            model_players.player_db.update(
                add("score", val), where("family_name") == players_list[i]
            )
        return model_players.player_db

    @staticmethod
    def updating_player_ranking():

        """option to update on demand, the rank of a player"""

        family_name = View().player_family_name_ranking_change()
        ranking = View().ranking_change()
        model_players.player_db.update(
            {"ranking": ranking}, where("family_name") == family_name
        )

    def sort_players_by_score(self):

        """sorting players to make pairs other but first turn, according to the swiss tournament system.
        If scores are the same, selection is then by ranking and if a player have already face the other,
        he will face the next to come on the list"""

        players_list = []
        for players in self.updating_players_score():
            players_list.append(players)
        sort_by_rank = sorted(
            players_list, key=lambda k: int(k["ranking"]), reverse=True
        )
        sort_by_points = sorted(sort_by_rank, key=lambda k: k["score"], reverse=True)
        # rank is preserved by default option
        return sort_by_points

    def get_pairs_other_turns(self):

        """to get other but first turn pairs"""

        new_pairs_list = []
        last_pairs_list = []
        sorted_players = self.sort_players_by_score()
        if model_round.round_db:
            for tuples_match in model_round.round_db:
                for pairs in tuples_match["pairs_to_play"]:
                    pairs = [pairs[0][0], pairs[1][0]]
                    pairs = tuple(pairs)
                    last_pairs_list.append(pairs)
        else:
            return None
        while len(new_pairs_list) <= len(last_pairs_list) and len(sorted_players) > 0:
            player_1 = sorted_players[0]["family_name"]
            player_2 = sorted_players[1]["family_name"]
            players_pair = (player_1, player_2)
            players_pair_reversed = players_pair[::-1]
            if (
                players_pair not in last_pairs_list
                and players_pair_reversed not in last_pairs_list
            ):
                player_1 = sorted_players.pop(0)
                player_2 = sorted_players.pop(0)
                players_pair = (player_1, player_2)
                new_pairs_list.append(players_pair)
                if len(sorted_players) == 2:
                    player_1 = sorted_players.pop(0)
                    player_2 = sorted_players.pop()
                    players_pair = (player_1, player_2)
                    new_pairs_list.append(players_pair)
                    return new_pairs_list
            else:
                i = 1
                while (
                    players_pair in last_pairs_list
                    and players_pair_reversed in last_pairs_list
                ):
                    i += 1
                    player_1 = sorted_players[0]
                    player_2 = sorted_players[i]
                    players_pair = (player_1, player_2)
                    players_pair_reversed = players_pair[::1]
                player_1 = sorted_players.pop(0)
                try:
                    player_2 = sorted_players.pop(i)
                except IndexError:
                    player_2 = sorted_players.pop(-1)
                players_pair = (player_1, player_2)
                new_pairs_list.append(players_pair)
        return new_pairs_list
