import os
from string import ascii_letters

bad_words = tuple('lol kek konopla opa popa minecraft dota2 pizi'.split())


def dir_passage(dir_path):
    """
    :param dir_path: str
    """
    for ii in os.listdir(dir_path):
        new_path = dir_path + '/' + ii
        if os.path.isdir(new_path):
            dir_passage(new_path)
        elif ii.split('.')[-1] == 'py':
            yield new_path


def get_vars(line):
    """
    :param line: str
    :return: tuple
    """
    if '=' in line and '==' not in line and 'def' not in line and 'class' not in line and 'with' not in line and 'if' not in line:
        return tuple(ii.strip().split('.')[-1] for ii in line.split('=')[0].strip().split(',') if '[' not in ii.strip().split('.')[-1])
    return ()


def replace_word(line, word, new_word):
    """
    :param line: str
    :param word: str
    :param new_word: str
    :return: str
    """
    line_parts = line.split(word)
    new_line = ''
    for ii in range(len(line_parts)-1):
        new_line += line_parts[ii]
        if line_parts[ii][-1] not in ascii_letters and line_parts[ii+1][0] not in ascii_letters:
            new_line += new_word
        else:
            new_line += word
    new_line += line_parts[-1]
    return new_line


def vars_replacement(file_path, bad_words_list):
    """
    :param file_path: str
    :param bad_words_list: list
    """
    with open(file_path, encoding='UTF-8') as f:
        data = f.readlines()

    vars_to_change = {}

    for ii in data:
        for j in get_vars(ii):
            vars_to_change[j] = None

    for ii in enumerate(vars_to_change):
        vars_to_change[ii[1]] = bad_words_list[ii[0]]


    with open(file_path, 'w', encoding='UTF-8') as f:
        for ii in data:
            line = ii
            for iii in vars_to_change:
                line = replace_word(line, iii, vars_to_change[iii])
            f.write(line)


if __name__ == '__main__':
    for i in dir_passage('garb'):
        vars_replacement(i, bad_words)
