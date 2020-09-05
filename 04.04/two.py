dictt = {"a": 1, "b": 2, "c": 3, "de": [4, 5]}


def add_el_1(dictt={}, key="", item=""):
    if key in dictt.keys():
        if isinstance(dictt[key], list):
            dictt[key].append(item)
        else:
            item_2 = dictt[key]
            dictt[key] = [item_2, item]
    else:
        dictt[key] = item
    return None


def add_el_2(dictt={}, key="", item=""):
    if key in dictt.keys():
        dictt[f"{key}_copy"] = item
    else:
        dictt[key] = item
    return None
