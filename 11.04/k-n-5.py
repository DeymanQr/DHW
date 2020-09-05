import copy, random, time

area = [
    ['_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_'],
]


def area_ptint(field):
    for i in field:
        print('|'.join(i))


def move(field, move, player):
    if not move.isdigit():
        raise TypeError("Move must be integer !")
    move = int(move)
    field_copy = copy.deepcopy(field)
    move -= 1
    if -1 < move < 25 and field_copy[move // 5][move % 5] == '_':
        field_copy[move // 5][move % 5] = player
        return field_copy
    raise IndexError("Incorrect input index !")


def player_move(mas, player):
    while True:
        a = input('\nEnter coordinate:\n\n')
        try:
            masiv = move(mas, a, player)
            return masiv
        except (IndexError, TypeError):
            print('Wrong index !')


def enemy_move(mas, player):
    while True:
        try:
            masiv = move(mas, str(random.randint(1, 25)), player)
            return masiv
        except IndexError:
            continue


def winner_detect(pole):
    if pole[0][0] == pole[0][1] == pole[0][2] == pole[0][3] == pole[0][4] and pole[0][0] != '_':
        return [True, pole[0][0]]
    if pole[1][0] == pole[1][1] == pole[1][2] == pole[1][3] == pole[1][4] and pole[1][0] != '_':
        return [True, pole[1][0]]
    if pole[2][0] == pole[2][1] == pole[2][2] == pole[2][3] == pole[2][4] and pole[2][0] != '_':
        return [True, pole[2][0]]
    if pole[3][0] == pole[3][1] == pole[3][2] == pole[3][3] == pole[3][4] and pole[3][0] != '_':
        return [True, pole[3][0]]
    if pole[4][0] == pole[4][1] == pole[4][2] == pole[4][3] == pole[4][4] and pole[4][0] != '_':
        return [True, pole[4][0]]
    if pole[0][0] == pole[1][0] == pole[2][0] == pole[3][0] == pole[4][0] and pole[0][0] != '_':
        return [True, pole[0][0]]
    if pole[0][1] == pole[1][1] == pole[2][1] == pole[3][1] == pole[4][1] and pole[0][1] != '_':
        return [True, pole[0][1]]
    if pole[0][2] == pole[1][2] == pole[2][2] == pole[3][2] == pole[4][2] and pole[0][2] != '_':
        return [True, pole[0][2]]
    if pole[0][3] == pole[1][3] == pole[2][3] == pole[3][3] == pole[4][3] and pole[0][3] != '_':
        return [True, pole[0][3]]
    if pole[0][4] == pole[1][4] == pole[2][4] == pole[3][4] == pole[4][4] and pole[0][4] != '_':
        return [True, pole[0][4]]
    if pole[0][0] == pole[1][1] == pole[2][2] == pole[3][3] == pole[4][4] and pole[0][0] != '_':
        return [True, pole[0][0]]
    if pole[0][4] == pole[1][3] == pole[2][2] == pole[3][1] == pole[4][0] and pole[0][4] != '_':
        return [True, pole[0][4]]
    else:
        return [False, None]

while True:
    type_plr = input("Choose your player (x or 0):\t")
    if type_plr not in ["x", "0"]:
        continue
    ch = ["x", "0"].index(type_plr)
    break


while True:
    if ch == 0:
        area = player_move(area, "x")
        area_ptint(area)
        res = winner_detect(area)
        if res[0]:
            print(f"Winner: {res[1]}")
            break
        print("\nEnemy move:\n")
        area = enemy_move(area, "0")
        time.sleep(1)
        area_ptint(area)
        res = winner_detect(area)
        if res[0]:
            print(f"Winner: {res[1]}")
    else:
        print("\nEnemy move:\n")
        area = enemy_move(area, "x")
        time.sleep(1)
        area_ptint(area)
        res = winner_detect(area)
        if res[0]:
            print(f"Winner: {res[1]}")
        area = player_move(area, "0")
        area_ptint(area)
        res = winner_detect(area)
        if res[0]:
            print(f"Winner: {res[1]}")
            break