'''model'''

'''import time
from models.match import new_score


class turn_set_up:

    def __init__(self, turn_name): #, beginning_time, ending_time):
        self.turn_name = turn_name
        #self.beginning_time = beginning_time
        #self.ending_time = ending_time
        
    def time_start(self):
        beginning_time = time.ctime()
        print (beginning_time)

    def end_notification(self):
        #demander en vue heure démarage et heure fin
        pass
        
    def time_end(self):
        ending_time = time.ctime()
        print(ending_time)

    def selecting_first_turn(self):
        #selecting by order
        pairs = []
        list_first_turn = [5, 7, 15, 1, 20, 36, 8, 2]
        list_first_turn.sort()
        # génération des premières paires
        number_of_players = len(list_first_turn)
        half = number_of_players / 2
        for i in range(int(number_of_players / 2)):
            pairs = (list_first_turn[i], list_first_turn[i + (int(number_of_players / 2))])
            return pairs

    def list_2nd_turn(self):
        #sort by points number
        new_pairs = []
        new_pairs.append(new_score.last_result_player_1)
        new_pairs.append(new_score.last_result_player_2)'''
        

    



        