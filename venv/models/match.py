'''model'''

from round import turn_set_up

class Match:

    def __init__ (self, player_1, player_2, result_player_1, result_player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.result_player_1 = result_player_1
        self.result_player_2 = result_player_2
      
    def new_score(self):
        print("player_1 results:")
        result_player_1 = int(input())
        print("player_2 results:")
        result_player_2 = int(input())
        print("Please enter player_1 new score:")
        player_1_new_score = int(input())
        print("Please enter player_2 new score:")
        player_2_new_score = int(input())
        last_result_player_1 = int(result_player_1 + player_1_new_score)
        last_result_player_2 = int(result_player_2 + player_2_new_score)
        print ("New order player_1:" + str (last_result_player_1))
        print ("New order player_2:" + str (last_result_player_2))







        
        