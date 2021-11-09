
/*Practice assignment*/

woman(jija).
man(john).
healthy(john).
healthy(jia).
wealthy(john).


traveller(X):-
	healthy(X),
	wealthy(X).

canTravel(X):-
	traveller(X).
