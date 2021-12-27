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

def std_list(tab):

	taille = len(tab)
	if(taille < 1):
		return None

	moyenne = mean_list(tab)
	std = 0

	for element in tab:
		std += (element - moyenne) ** 2

	return math.sqrt( std  / taille )

def is_geometric(tab):

	taille = len(tab)
	if taille < 1 :
		return None
	elif taille < 2:
		return True

	if tab[0] == 0:
		q = 0
	else:		
		q = tab[1] / tab[0]

	for i in range(taille - 1):
		if( tab[i + 1] != q * tab[i] ):
			return False

	return True

def is_arithmetic(tab):

	taille = len(tab)
	if taille < 1 :
		return None
	elif taille < 2:
		return True
	
	r = tab[1] - tab[0]

	for i in range(taille - 1):
		if( tab[i + 1] != r + tab[i] ):
			return False

	return True

def return_next_geometric_progression(tab , n):

	if not is_geometric(tab):
		return False

	if tab[0] == 0:
		q = 0
	else:		
		q = tab[1] / tab[0]

	prev = tab[-1]
	next_list = []

	for i in range(n):
		new = prev * q
		next_list.append(new)
		prev = new

	return True , next_list