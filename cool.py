from backend import *


""""
This script calculates the number of unique (up to rotation) cards that could exist in
the board game Tsuro. The insight is that every possible card can be written as a permutation
that fulfils certain requirements.

Once we have all such possible permutations we sort these in to equivalence classes.
"""


#
all_perm = []
k = 0

# If it satisfies the conditions add it to `all_perm`
for perm in itrt.permutations(IDTY):
	if no_self(perm) and double_idty(perm):
		all_perm.append(perm)

print("Number of all legal cards:", end = ' ')
print(len(all_perm))

# Initialize equivalence class list
equv_classes = []

# Sort all permutations into equivalence classes
for perm in all_perm:
	did_find = False
	for cla in equv_classes:
		if is_equiv(perm, cla[0]):
			cla.append(perm)
			did_find = True
			break

	if not did_find:
		equv_classes.append([perm])

# Print number of equivalence classes
print("Number of equivalence classes:", end = ' ')
print(len(equv_classes))


# Print number of elements in all equivalence classes
# This should be equal to number of all permutations
print("Number of ele equivalence classes:", end = ' ')
print(len([x for cla in equv_classes for x in cla]))

# Print all equivalence classes with more than a single element
number_two = 0
number_four = 0
for cla in equv_classes:
	if len(cla) == 2:
		number_two += 1
	elif len(cla) == 4:
		number_four += 1

print("Number of equivalence classes of size 1:", end = ' ')
print(len(equv_classes) - number_two - number_four)

print("Number of equivalence classes of size 2:", end = ' ')
print(number_two)

print("Number of equivalence classes of size 4:", end = ' ')
print(number_four)

all_repr = []
for cla in equv_classes:
	all_repr.append(cla[0])

# ---

l_identities = []
for perm in all_repr:
	if all([is_equiv(x, mult(perm, x)) for x in all_repr]):
		l_identities.append(perm)

print("Number of left identities:", end = ' ')
print(len(l_identities))

# ---

r_identities = []
for perm in all_repr:
	if all([is_equiv(x, mult(x, perm)) for x in all_repr]):
		r_identities.append(perm)

print("Number of right identities:", end = ' ')
print(len(r_identities))

# ---

centralizer = []
for perm in all_repr:
	if all([is_equiv(mult(x, perm), mult(perm, x)) for x in all_repr]):
		centralizer.append(perm)

print("Number of elements in centralizer:", end = ' ')
print(len(centralizer))

# ---
all_l_identities = []
for perm in itrt.permutations(IDTY):
	if all([is_equiv(x, mult(perm, x)) for x in all_repr]):
		all_l_identities.append(perm)

print("Number of right identities in all perm:", end = ' ')
print(len(all_l_identities))

# ---
all_r_identities = []
for perm in itrt.permutations(IDTY):
	if all([is_equiv(x, mult(x, perm)) for x in all_repr]):
		all_r_identities.append(perm)

print("Number of right identities in all perm:", end = ' ')
print(len(all_r_identities))
