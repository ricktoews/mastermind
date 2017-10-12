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
        return True
    else:
        return False    
        

def check_inexact(inexact, perm, pattern):
    perm = list(perm)
    orig_pattern = pattern
    pattern = list(pattern)
    pattern_len = len(pattern)
    for i in range(pattern_len):
        if pattern[i] == perm[i]:
            perm[i] = '_'
            pattern[i] = '_'
    count = 0
    for i in range(pattern_len):
        if pattern[i] != '_':
            if pattern[i] != perm[i] and pattern[i] in perm:
                count += 1
    if count == inexact:
        return True
    else:
        return False


def is_match(exact, inexact, perm, pattern):
    exact_match = check_exact(exact, perm, pattern)
    if exact_match:
        inexact_match = check_inexact(inexact, perm, pattern)

    return exact_match and inexact_match


def filter_perms(exact, inexact, pattern):
    filtered = []
    for p in perms:
        if is_match(exact, inexact, p, pattern):
            filtered.append(p)

    return filtered
