import itertools as itrt

# Some useful permutations
IDTY = [0, 1, 2, 3, 4, 5, 6, 7]
ROTL = [2, 3, 4, 5, 6, 7, 0, 1]
ROTR = [6, 7, 0, 1, 2, 3, 4, 5]


# Rotate a card left
def rot_card_L(perm):
    return apply(ROTR, apply(perm, ROTL))


# Rotate a card right
def rot_card_R(perm):
    return apply(ROTL, apply(perm, ROTR))


# Test if card A is rotationally equivalent to card B
def is_equiv(perm1, perm2):
    if compare_all(perm1, perm2):
        return True

    if compare_all(perm1, rot_card_L(perm2)):
        return True

    if compare_all(rot_card_L(perm1), perm2):
        return True

    if compare_all(rot_card_L(perm1), rot_card_R(perm2)):
        return True

    return False


# Apply permutation to vector `vect`
def apply(perm, vect):
    return [perm[x] for x in vect]


# Condition that no string can lead to itself
def no_self(perm):
    if compare_any(IDTY, perm):
        return False
    return True


# Condition that evert string only has a single end
def double_idty(perm):
    if compare_all(IDTY, apply(perm, perm)):
        return True
    return False


# AND
def compare_all(listA, listB):
    if len(listA) != len(listB):
        raise Exception("List lengths differ.")
    for k in range(len(listA)):
        if listA[k] != listB[k]:
            return False
    return True


# OR
def compare_any(listA, listB):
    if len(listA) != len(listB):
        raise Exception("List lengths differ.")
    for k in range(len(listA)):
        if listA[k] == listB[k]:
            return True
    return False
