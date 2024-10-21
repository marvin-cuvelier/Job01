"""Écrire un programme qui calcule le produit de toutes les valeurs de la liste
comprises dans l’intervalle [25, 90].

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]"""

# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialisation du produit
produit = 1

# Parcourir chaque élément de la liste
for valeur in L:
    # Vérifier si la valeur est dans l'intervalle [25, 90]
    if 25 <= valeur <= 90:
        produit *= valeur  # Multiplier la valeur au produit

# Affichage du produit
print("Le produit des valeurs dans l'intervalle [25, 90] est:", produit)
