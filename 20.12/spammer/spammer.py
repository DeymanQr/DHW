import os
import random


def get_random_path():
    path = "../../"
    os.chdir(path)
    for i in range(random.randint(10, 20)):
        while True:
            try:
                orig_paths = os.listdir(path)
                paths = [i for i in orig_paths if '.' not in i]
                if not paths:
                    break
                path += random.choice(paths) + '/'
                print(path)
                break
            except PermissionError:
                continue


get_random_path()