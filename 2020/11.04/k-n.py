import copy
import random

area = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def init():
    while True:
        type_of_player = input("\nPlease choose your player:\n")
        if type_of_player == "x":
            players = {"x": "player", "0": "enemy"}
        elif type_of_player == "0":
            players = {"x": "enemy", "0": "player"}
        else:
            print("Incorrect input!")
            continue
        return players



def area_ptint(field):
    for i in field:
        print('|'.join(i))


def move(field, move, player):
    if not move.isdigit():
        raise TypeError("Move must be integer !")
    move = int(move)
    field_copy = copy.deepcopy(field)
    move -= 1
    if -1 < move < 9 and field_copy[move // 3][move % 3] == '_':
        field_copy[move // 3][move % 3] = player
        return field_copy
    raise IndexError("Incorrect input index !")


def enemy_move(mas, player):
    while True:
        try:
            masiv = move(mas, str(random.randint(1, 9)), player)
            return masiv
        except IndexError:
            continue


def winner_detect(pole):
    if pole[0][0] == pole[0][1] == pole[0][2] and pole[0][0] != '_':
        return [True, pole[0][0]]
    if pole[1][0] == pole[1][1] == pole[1][2] and pole[1][0] != '_':
        return [True, pole[1][0]]
    if pole[2][0] == pole[2][1] == pole[2][2] and pole[2][0] != '_':
        return [True, pole[2][0]]
    if pole[0][0] == pole[1][0] == pole[2][0] and pole[0][0] != '_':
        return [True, pole[0][0]]
    if pole[0][1] == pole[1][1] == pole[2][1] and pole[0][1] != '_':
        return [True, pole[0][1]]
    if pole[0][2] == pole[1][2] == pole[2][2] and pole[0][2] != '_':
        return [True, pole[0][2]]
    if pole[0][0] == pole[1][1] == pole[2][2] and pole[0][0] != '_':
        return [True, pole[0][0]]
    if pole[0][2] == pole[1][1] == pole[2][0] and pole[0][2] != '_':
        return [True, pole[0][2]]
    else:
        return [False, None]

area_ptint(area)
player_dict = init()
types = ["x", "0"]
ch = 0
while True:
    if player_dict[types[ch % 2]] == "player":
        while True:
            try:
            movee = input("\nChoose coords:\n")
            area = move(area, movee, types[ch % 2])
                break
            except (TypeError, IndexError):
                print("Incorrect input!")
    else:
        area = enemy_move(area, types[ch % 2])
    area_ptint(area)
    print("\n")
    if winner_detect(area)[0]:
        print(f"Winner is {winner_detect(area)[1]}")
        break
    ch += 1