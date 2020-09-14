import random

abc = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ.,:;!?/-+*%@#"()&$ "\'0123456789аАбБвВгГдДеЕёЁжЖзЗиИйЙкКлЛмМнНоОпПрРсСтТуУфФхХцЦчЧшШщЩъЪыЫьЬэЭюЮяЯ'


def encode(str1):
    num = random.randint(0,50)
    new = ''
    for i in str1:
        new += abc[(abc.index(i) + num) % len(abc)]
    return new, num


def decode(str1, num):
    new = ''
    for i in str1:
        new += abc[(abc.index(i) - num) % len(abc)]
    return new


if __name__ == '__main__':
    a = input()
    b = encode(a)
    print(b)
    c = decode(b[0], b[1])
    print(c)