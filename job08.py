"""Écrire un programme qui calcule la somme de toutes les valeurs paires de la
liste : L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]."""


def sommepaires(liste):
    somme = 0
    for i in liste:
        if i % 2 == 0:  # Vérifie si la valeur est paire
            somme += i
    return somme

# Exemple d'utilisation
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat = sommepaires(L)
print("La somme des valeurs paires est :", resultat)
