import copy, time

area = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


players = {}
players_list = []

def init():
    global players_list, players
    while True:
        hu_player = input("\nChoose your player (x or 0):\n")
        if hu_player == "x":
            players = {"x": "player", "0": "enemy"}
            players_list = ["x", "0"]
        elif hu_player == "0":
            players = {"x": "enemy", "0": "player"}
            players_list = ["0", "x"]
        else:
            print("\nIncorrect input!")
            continue
        break


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


empty_indices = lambda mas: [i for i in range(len(mas)) if mas[i] == "_"]


def minimax(mas, player, player_list):
    if isinstance(mas[0], list):
        mas_copy = []
        for i in mas:
            for j in i:
                mas_copy.append(j)
    else:
        mas_copy = copy.deepcopy(mas)
    avail_spots = empty_indices(mas_copy)
    print(mas)
    if winner_detect(mas)[0]:
        if winner_detect(mas)[1] == "0":
            return {"score": 10}
        return {"score": -10}
    elif len(avail_spots) == 0:
        return {"score": 0}
    moves = []
    for i in avail_spots:
        x = (i-1) % 3
        y = (i-1) // 3
        move = {}
        move["index"] = i
        mas[y][x] = player
        if player == player_list[1]:
            result = minimax(mas=mas, player=player_list[0], player_list=player_list)
            move["score"] = result
        else:
            result = minimax(mas=mas, player=player_list[1], player_list=player_list)
            move["score"] = result
        mas[y][x] = "_"
        moves.append(move)
    if player == player_list[1]:
        best_score = -10000
        for i in range(len(moves)):
            if moves[i]["score"] > best_score:
                best_score = moves[i]["score"]
                best_move = i
    else:
        best_score = 10000
        for i in range(len(moves)):
            if moves[i]["score"] < best_score:
                best_score = moves[i]["score"]
                best_move = i
    print(moves[best_move])
    return moves[best_move]


def enemy_move(area, player):
    area_copy = copy.deepcopy(area)
    print(minimax(area_copy, player, players_list))
    return area_copy



ch = 0
init()
area_ptint(area)
while True:
    if players[["x", "0"][ch % 2]] == "player":
        while True:
            try:
                index = input("\nChose place:\n")
                area = move(area, index, players_list[0])
                break
            except (IndexError, TypeError):
                print("Incorrect index !")
    else:
        time.sleep(1)
        area = enemy_move(area, players_list[1])
    area_ptint(area)
    if winner_detect(area)[0]:
        print(f"Winner is:{winner_detect(area)[1]}")
        break
    ch += 1