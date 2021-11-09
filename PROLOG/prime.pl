non_divisible_from(N, D):-
	N =<D.

non_divisible_from(N, D):-
	N>D,
	N mod D =\= 0,
	D1  is D+1	,
	non_divisible_from(N, D1).


isPrime(N):-
	N>1,
	non_divisible_from(N, 2).
