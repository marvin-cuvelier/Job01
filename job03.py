"""Écrire une fonction qui contient une liste nommée « fruits » qui contient les
strings « pomme », « cerise », « orange ». Cette fonction doit à son appel
ajouter à la liste « fruits » un String « Melon » à la fin de cette liste."""

def lesfruit():
    fruit = ["pomme", "cerise ,orange"]
    fruit.append("melon") #append pour ajouter a une liste
    return fruit

print(lesfruit())
