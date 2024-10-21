"""Écrire une fonction qui contient une liste nommée « fruits » qui contient les
strings pomme, cerise, orange, melon. Cette fonction doit à son appel ajouter
à la liste « fruits » un string « mangue » à l’index 2."""

def thefruits():
    fruits = ["pomme", "cerise", "orange", "melon"]
    #utiliser insert pour rajouter a une liste et choisir l'emplacement dans la liste 
    fruits.insert(2,"mangue")
    print (fruits)

thefruits()    