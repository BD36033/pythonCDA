# cours.py
# prenom = input("Veuillez saisir votre prénom : ")
# nom = input("Veuillez saisir votre nom : ")
# annee_naissance = int(input("Veuillez saisir votre année de naissance : "))

# age = 2024 - annee_naissance

# print(f"Bonjour {prenom} {nom}, vous êtes né en {annee_naissance}.")

# Exercice 7

# Fonction pour afficher le prénom dans une boîte
def afficher_prenom_dans_boite(prenom):
    # Caractères pour la boîte
    haut_gauche = "┌"
    haut_droite = "┐"
    bas_gauche = "└"
    bas_droite = "┘"
    horizontal = "─"
    vertical = "│"

    # Calculer la longueur de la boîte
    longueur = len(prenom) + 2  # +2 pour les espaces de chaque côté

    # Afficher la boîte
    print(f"{haut_gauche}{horizontal * longueur}{haut_droite}")
    print(f"{vertical} {prenom} {vertical}")
    print(f"{bas_gauche}{horizontal * longueur}{bas_droite}")

# Demander à l'utilisateur de saisir son prénom
prenom = input("Veuillez saisir votre prénom : ")

# ANSI escape codes pour le texte vert sur fond bleu
ANSI_GREEN = "\033[32m"
ANSI_BLUE_BACKGROUND = "\033[44m"
ANSI_RESET = "\033[0m"  # Réinitialiser les couleurs

# Afficher le prénom dans la boîte avec les couleurs
print(f"{ANSI_BLUE_BACKGROUND}{ANSI_GREEN}", end="")
afficher_prenom_dans_boite(prenom)
print(ANSI_RESET)  # Réinitialiser les couleurs après l'affichage