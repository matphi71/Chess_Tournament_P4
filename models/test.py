
list_first_turn = [3, 4, 6, 7]

def new_score():
    new_results_list = []
    for i in range (len (list_first_turn)):
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
        print("New rank player_1: " + str(last_result_player_1))
        print("New rank player_2: " + str(last_result_player_2))
        new_results_list.append(last_result_player_1)
        new_results_list.append(last_result_player_2)
    new_results_list.sort()
    return new_results_list

'''def list_2nd_turn():
    new_pairs = []
    for i in range (len(list_first_turn)):
        j = 0 + i
        new_pairs.append()(new_score()[j])
        new_pairs.append()(new_score()[j+1])
        j =+ 1
    return new_pairs'''

def list_2nd_turn():
    new_pairs = []
    for i in range(int(len(list_first_turn))/2):
        new_pairs = new_score().pop[i][i + 1]
    return new_pairs


print(new_score())
print(list_2nd_turn())
