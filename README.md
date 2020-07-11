# Tsuro Card Counter

This little script count the possible number of cards in the game of Tsuro.
It consider rotational invariance.

 I number the cards like so:

<pre>
|-- 0 - 1 --|
7           2
|           |
6           3
|-- 5 - 4 --|
</pre>

So the following

<pre>
|-- 0 - 1 --|
7-| |---|---2
| |     |   |
6-| |---|---3
|-- 5 - 4 --|
</pre>

corresponds to `[2, 4, 0, 5, 1, 3, 7, 6]`.

## Some Math

Since every card corresponds to a permutation, and obviously not every permutation
makes a valid card, we can ask ourselves what are the restrictions that make
a valid permutation. After some pondering I found the following:

1. f^2(n) = n, for all n in {0, 1, ..., 7}
2. f(n) \\= n, for all n

The first says that since strings only connect two points, if you walk along the
same string twice you should end up where you started. And the second condition
says that no string can connect a number to itself.

### Rotation invariance
Next we want to formalize what a rotation is. First notice that the permutation
`[2, 3, 4, 5, 6, 7, 0, 1]` and its inverse `[6, 7, 0, 1, 2, 3, 4, 5]` correspond
to 90 degree turns to the left and right respectively. The question then becomes:
how do we apply these to our cards? Since permutations are bijective maps we can
simply concatenate them and get another permutation. But it becomes apparent that
this is not the correct operation. Instead we will have to do the following, which
will seem familiar to anyone who has taken group theory before:

`*: Perm x Perm --> Perm ; x,y |--> y^{-1} ° x ° y`

By testing we can see that multiplication is exactly the operation we want. For left
rotation it becomes `x * L = R ° x ° L` and similarly for right rotation. Notice that
this operation is also well defined for all cards, and inparticular, due to restriction 1)
we can simplify to `x * y =  y ° x ° y`.