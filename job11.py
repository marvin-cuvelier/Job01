"""Écrire un programme qui crée la liste d’entiers L = [7, 11, 42, 39, 2], votre
programme devra pouvoir modifier la liste en augmentant de 1 la valeur de
chaque élément de la liste."""

# Création de la liste L
L = [7, 11, 42, 39, 2]

# Modification de la liste en augmentant chaque élément de 1
for i in range(len(L)):
    L[i] += 1

# Affichage de la liste modifiée
print(L)
