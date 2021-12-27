import math

def max_int(a,b):

	if a < b :
		return b
	else :
		return a

def min_int(a,b):

	if a < b:
		return a
	else:
		return b

def mean_list(tab):

	somme = sum(tab)
	taille = len(tab)
	return somme / taille