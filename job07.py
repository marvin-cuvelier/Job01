"""Écrire un programme qui compte le nombre de multiples de 3 présents dans
la liste : L = [8, 24,48,2,16]."""

L = [8,24,48,2,16]
x = 0
liste = []
for i in range(len(L)):
    if i % 3 == 0:
        x += 1
        liste.append(L[i])



print(x)
print(liste)
       


    


       


        



 



