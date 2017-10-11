#! /usr/bin/python

import itertools

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def build_digits(count):
    list = ''
    for i in range(count):
        list += letters[i:i+1]
    return list


def build(symbols, places):
    _perms = []
    digits = build_digits(symbols)
    for num in itertools.product(digits, repeat=places):
        perm = ''.join(num)
        _perms.append(perm)

    return _perms

