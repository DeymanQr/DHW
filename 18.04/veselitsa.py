import random
import requests

alphabet = 'abcdefghijklmnopqrstuvwxyz'
used_letters = []


def pprint(level):
    levels = [
        '',
        '/|\\',
        ' | \n | \n | \n/|\\',
        '  ___ \n | \n | \n | \n/|\\',
        '  ___\n |   |\n |  \n |  \n | \n/|\\',
        '  ___\n |   |\n |   0\n |  \n | \n/|\\',
        '  ___\n |   |\n |   0\n |  /\n | \n/|\\',
        '  ___\n |   |\n |   0\n |  /|\n | \n/|\\',
        '  ___\n |   |\n |   0\n |  /|\\\n | \n/|\\',
        '  ___\n |   |\n |   0\n |  /|\\\n |  / \n/|\\',
        '  ___\n |   |\n |   0\n |  /|\\\n |  / \\\n/|\\',
    ]
    if 0 <= level < 11:
        print(levels[level])
        return None
    raise TypeError("Incorrect level !")


def print_field(field):
    print('Word: ', ' '.join(field))


def hint(field, word):
    not_find_lets = []
    for i in range(len(field)):
        if field[i] == "_":
            not_find_lets.append(word[i])
    return random.choice(not_find_lets)


def rand_word():
    while True:
        resp = requests.get("http://api.wordnik.com/v4/words.json/randomWords?minCorpusCount=0&limit=1&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5")
        yield resp.json()[0]['word']


def create_word_field(word):
    field = []
    for _ in word:
        field.append('_')
    return field


def make_move(field, used, word):
    while True:
        new_letter = input('Enter a letter that has not yet been:')
        new_letter = new_letter.lower()
        if len(new_letter) == 1 and new_letter in alphabet and new_letter not in used:
            if new_letter in word:
                for i in range(len(word)):
                    if word[i] == new_letter:
                        field[i] = new_letter
                used.append(new_letter)
                return [field, used, word, True]
            used_letters.append(new_letter)
            return [field, used, word, False]
        elif new_letter == "all":
            for i in range(len(word)):
                field[i] = word[i]
                used.append(word[i])
            print_field(field)
            print('Used letters: ', ' '.join(used))
            return [field, used, word, True]
        elif new_letter == "hint":
            print('The word has letter ', hint(field, word))
        else:
            print('You have entered incorrect letter! Enter again!')


def winning_or_loosing(field, game_number):
    if "_" not in field:
        return True
    elif game_number >= 10:
        return False


words = rand_word()
word = next(words)
field_word = create_word_field(word)
game_number = 0
print('We made a word for you: \n')

while True:
    print_field(field_word)
    pprint(game_number)
    print('Used letters: ', ' '.join(used_letters))
    field_word, used_letters, word, in_word = make_move(field_word, used_letters, word)

    if not in_word:
        game_number += 1

    is_win = winning_or_loosing(field_word, game_number)
    if is_win:
        print('You win!')
        print(word)
        break

    if is_win == False:
        print('You lose!')
        pprint(game_number)
        print(word)
        break