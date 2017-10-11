#! /usr/bin/python

import permutations
perms = permutations.build(6, 4)

def check_exact(exact, perm, pattern):
    perm = list(perm)
    pattern = list(pattern)
    pattern_len = len(pattern)
    count = 0
    for i in range(pattern_len):
        if pattern[i] == perm[i]:
            pattern[i] = '_'
            count += 1
    if count == exact:
        return ''.join(pattern)
    else:
        return False    
        

def check_inexact(inexact, perm, pattern):
    perm = list(perm)
    pattern = list(pattern)
    pattern_len = len(pattern)
    count = 0
    for i in range(pattern_len):
        if pattern[i] != '_':
            if pattern[i] != perm[i] and pattern[i] in perm:
                count += 1
    if count == inexact:
        return ''.join(pattern)
    else:
        return False


def final_check(perm, pattern):
    result = True
    perm = list(perm)
    pattern = list(pattern)
    pattern_len = len(pattern)
    for i in range(pattern_len):
        if pattern[i] != '_':
            if pattern[i] in perm:
                result = False
    return result


def is_match(exact, inexact, perm, pattern):
    pattern = check_exact(exact, perm, pattern)
    if bool(pattern):
        pattern = check_innexact(inexact, perm, pattern)
    if bool(pattern):
        pattern = final_check(perm, pattern)

    return bool(pattern)


def filter_perms(exact, inexact, pattern):
    filtered = []
    for p in perms:
        if is_match(exact, inexact, p, pattern):
            filtered.append(p)

    return filtered
