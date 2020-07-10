from bvla import *


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

print("Number of all legal cards:")
print(len(all_perm))

equv_classes = []

for perm in all_perm:
	did_find = False
	for cla in equv_classes:
		if is_equiv(perm, cla[0]):
			cla.append(perm)
			did_find = True
			break

	if not did_find:
		equv_classes.append([perm])

print("Number of equivalence classes:")
print(len(equv_classes))


print("Number of ele equivalence classes:")
print(len([x for cla in equv_classes for x in cla]))


for cla in equv_classes:
	if len(cla) > 1:
		print(cla)


