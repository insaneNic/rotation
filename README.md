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

`*: A x Perm --> A ; x,y |--> y^{-1} ° x ° y`

LEM: This operation is well defined. 

Proof: Let `f` in `A`. Let `R` be in `Perm`. Since we know `f ° R (n) \= R(n)` we can be
sure that `R^{-1} ° f ° R (n) \= n`.

Next 
<pre>
(R^{-1} ° f ° R)^2 (n)
= R^{-1} ° f ° R ° R^{-1} ° f ° R (n)
= R^{-1} ° f ° f ° R (n)
= R^{-1} ° R (n)
= n
</pre>

And so both conditions are satisfied. [ ]

### Some more properties

By testing we can see that multiplication is exactly the operation we want. For left
rotation it becomes `x * L = R ° x ° L` and similarly for right rotation. Notice that
this operation is also well defined for all cards, and inparticular, due to restriction 1)
we can simplify to `x * y =  y ° x ° y`.

Now we can use the multiplication to define an equivalence relation ~ by saying any
card that is in the orbit of `L` is equivalent. It is left as an exercise to the
reader to prove that this is actually an equivalence relation.

There are then many questions we can ask. Let me start with my original question:

- How many possible cards are there?

If we do not consider rotation there are 105 cards. Applying the equivalence class we 
end up with 35. If we order them by class size we get the following:

| Class size | Number of Classes |
|------------|-------------------|
| 1          | 5                 |
| 2          | 10                |
| 4          | 20                |

Cards in class size 1 have full rotational symmetry. Cards in class size 2 have 180° rotational
symmetry. And finally classes of size 4 means no rotational symmetry. There can not be a
class of size three.

- Is our multiplication abelian?

No: in particular the Centralizer is empty. This means that there isn't even a single
element that can commute with every other.

- Is there an identity element in the set of cards with respect to our multiplication?

Kind of. There is only a right-identity element. That mean only if you multiply this
element from the right does it act as an identity. This element is: (4, 5, 6, 7, 0, 1, 2, 3)
which is one of the five elements which is completely rotation invariant, i.e. it is
in its own equivalence class.


 