    
/* Too check if the given element exists in the list */
member([],_):-!, fail.
member([H|_], X) :-
  X = H,                    
  !.
member([_|T], X):-member(T, X).   

/* To calculate the length of the list */
enumerate([], R):- R is 0.
enumerate([_|T], R):-
    enumerate(T, X),
    R is X + 1.


/* Finding first element*/
first([H|_], F):-
	F is H.


/* Finding last element*/
last([H], L):- L is H.
last([_|T], L):-
	last(T, L).



/* Finding smallest element in list*/
min([Min],Min).                
min([H,K|T],M) :-
    H =< K,                             
    min([H|T],M).               
min([H,K|T],M) :-
    H > K,                              
    min([K|T],M).      



/* Finding largest element in list*/
max([Max],Max).                
max([H,K|T],M) :-
    H =< K,                             
    max([K|T],M).               

max([H,K|T],M) :-
    H > K,                              
    max([H|T],M).


/* Finding sum of the elements of the list*/
sum([H], Sum):- Sum is H.
sum([H|T], Sum):-
	sum(T, S),
	Sum is H+S.


/* Finding the number of elements in the list */
count([], C):- C is 0.
count([_|T], C):-
    count(T, X),
    C is X + 1.


/* Finding the arithematic mean of elements in the list */

mean([H|T], X):-
	sum([H|T], S),
	count([H|T], C),
	C>0,
	X is S/C.
