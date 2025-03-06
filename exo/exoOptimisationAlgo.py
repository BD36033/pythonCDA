import random
import string
import time

liste_nombres = random.choices(range(50), k=50)
liste_lettres = random.choices(string.ascii_uppercase, k=20)

def supprimer_doublons_avec_set(liste):
    return list(set(liste))

def supprimer_doublons_avec_boucle(liste):
    resultat = []
    for element in liste:
        if element not in resultat:
            resultat.append(element)
    return resultat

print("Liste nombres :", liste_nombres)
print("Sans doublons (set) :", supprimer_doublons_avec_set(liste_nombres))
print("Sans doublons (boucle) :", supprimer_doublons_avec_boucle(liste_nombres))

print("\nListe lettres :", liste_lettres)
print("Sans doublons (set) :", supprimer_doublons_avec_set(liste_lettres))
print("Sans doublons (boucle) :", supprimer_doublons_avec_boucle(liste_lettres))

taille_test = random.choices(range(100), k=100)

debut = time.time()
supprimer_doublons_avec_set(taille_test)
print("\nTemps (set) :", time.time() - debut, "secondes")

debut = time.time()
supprimer_doublons_avec_boucle(taille_test)
print("Temps (boucle) :", time.time() - debut, "secondes")
