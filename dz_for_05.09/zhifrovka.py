import json
import random


def create_key():
    with open('value.json', 'r', encoding='UTF-8') as f:
        length = len(json.load(f))
    key = [i for i in range(length)]
    random.shuffle(key)
    with open('key.json', 'w', encoding='UTF-8') as f:
        f.write(json.dumps(key))


def encode():
    with open('value.json', 'r', encoding='UTF-8') as f:
        value = json.load(f)
    with open('key.json', 'r', encoding='UTF-8') as f:
        key = json.load(f)
    encode_value = []
    for i in key:
        encode_value.append(value[i])
    with open('value.json', 'w', encoding='UTF-8') as f:
        json.dump(encode_value, f)


def decode():
    with open('value.json', 'r', encoding='UTF-8') as f:
        value = json.load(f)
    with open('key.json', 'r', encoding='UTF-8') as f:
        key = json.load(f)
    decode_value = []
    for _ in value:
        decode_value.append(None)
    for i, j in enumerate(key):
        decode_value.pop(j)
        decode_value.insert(j, value[i])
    with open('value.json', 'w', encoding='UTF-8') as f:
        json.dump(decode_value, f)


if __name__ == '__main__':
    create_key()
    encode()
    with open('value.json', 'r', encoding='UTF-8') as f:
        print(json.load(f))
    decode()
    with open('value.json', 'r', encoding='UTF-8') as f:
        print(json.load(f))