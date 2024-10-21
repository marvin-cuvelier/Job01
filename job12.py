"""Écrire un programme qui trie dans l’ordre croissant une liste passée en
paramètre.

SANS UTILISER DE FONCTION SYSTÈME (len, sort, round.....)"""


def tri_liste(liste):
    # On utilise l'algorithme de tri par sélection
    n = len(liste)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            # Comparaison des éléments pour trouver le minimum
            if liste[j] < liste[min_index]:
                min_index = j
        # Échange de l'élément actuel avec le minimum trouvé
        liste[i], liste[min_index] = liste[min_index], liste[i]
    
    return liste

# Exemple d'utilisation :
ma_liste = [64, 25, 12, 22, 11]
print("Liste avant tri :", ma_liste)
print("Liste triée :", tri_liste(ma_liste))
