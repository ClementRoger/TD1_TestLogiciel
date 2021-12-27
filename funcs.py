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

def median_list(tab):

	tab = sorted(tab)
	taille = len(tab)
	center_left_index = int( ( (taille - 1) / 2 ) )
	center_right_index = int( ( (taille + 1) / 2 ) )

	if taille < 1:
		return None
	elif taille % 2 == 0:
		return ( tab[ center_left_index ] + tab[ center_right_index ] ) / 2.0 #tableau de taille paire on renvoie la moyenne des deux éléments centraux
	return tab[ center_left_index ]	