female(elizabeth).
female(diana).
female(anne).
female(zara).
female(sarah).
female(beatrice).
female(eugine).
female(sophie).
female(louise).


male(philip).
male(charles).
male(william).
male(mark).
male(peter).
male(andrew).
male(edward).
male(james).
male(harry).


parent(elizabeth, charles).
parent(philip, charles).
parent(elizabeth, anne).
parent(philip, anne).
parent(elizabeth, andrew).
parent(philip, andrew).
parent(elizabeth, edward).
parent(philip, edward).


parent(diana, william).
parent(charles, william).
parent(diana, harry).
parent(charles, harry).


parent(anne, peter).
parent(mark, peter).
parent(anne, zara).
parent(mark, zara).


parent(sarah, beatrice).
parent(andrew, beatrice).
parent(sarah, eugine).
parent(andrew, eugine).


parent(sophie, louise).
parent(edward, louise).
parent(sophie, james).
parent(edward, james).

father(Parent, Child):-
	male(Parent),
	parent(Parent, Child).

mother(Parent, Child):-
	female(Parent),
	parent(Parent, Child).

child(Child, Parent):-
	parent(Parent, Child).

son(Child, Parent):-
	male(Child),
	child(Child, Parent).

daughter(Child, Parent):-
	female(Child),
	child(Child, Parent).

grandparent(GP, GC):-
	parent(GP, X),
	parent(X, GC).

grandmother(GM, GC):-
	female(GM),
	grandparent(GM, GC).

grandfather(GF, GC):-
	male(GF),
	grandparent(GF, GC).

grandson(GS, GP):-
	male(GS),
	grandparent(GP, GS).

granddaughter(GD, GP):-
	female(GD),
	grandparent(GP, GD).

spouse(Person1, Person2):-
	parent(Person1, X),
	parent(Person2, X),
	Person2 \= Person1.

husband(Person, Wife):-
	spouse(Person, Wife).

wife(Person, Husband):-
	spouse(Person, Husband).

sibling(Person1, Person2):-
	parent(X, Person1),
	parent(X, Person2),
	Person2 \= Person1.

brother(Person, Sibling):-
	male(Person),
	sibling(Person, Sibling).

sister(Person, Sibling):-
	female(Person),
	sibling(Person, Sibling).


aunt(Aunt, Person):-
	female(Aunt),
	sibling(Aunt, X),
	parent(X, Person).

aunt(Aunt, Person):-
	female(Aunt),
	wife(Aunt, X),
	sibling(X, Y),
	parent(Y, Person).

uncle(Aunt, Person):-
	male(Aunt),
	sibling(Aunt, X),
	parent(X, Person).

uncle(Uncle, Person):-
	male(Uncle),
	husband(Uncle, X),
	sibling(X, Y),
	parent(Y, Person).


nephew(Nephew, Person):-
	male(Nephew),
	uncle(Person, Nephew);
	aunt(Person, Nephew).

neice(Neice, Person):-
	female(Neice),
	uncle(Person, Neice);
	aunt(Person, Neice).

firstcousin(Person1, Person2):-
	nephew(Person1, X),
	parent(X, Person2).

firstcousin(Person1, Person2):-
	neice(Person1, X),
	parent(X, Person2).
