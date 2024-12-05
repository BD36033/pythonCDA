# test.py

def contenu_page():
    return "<h1>Exercice</h1>"

# Fonctions de calcul
def calculer_somme(a, b):
    return a + b

def calculer_multiplication(a, b):
    return a * b

def soustraire(a, b):
    return a - b

# Affichage de l'exercice pour la somme
def afficher_exercice1():
    return '''
    <div class="form-container">
        <h1>Exercice d'addition</h1>
        <form method="POST" class="exercise-form">
            <input type="text" name="a" placeholder="Entrez le premier nombre" required>
            <input type="text" name="b" placeholder="Entrez le deuxième nombre" required>
            <button type="submit" name="operation" value="somme">Calculer la somme</button>
        </form>
    </div>
    '''

# Affichage de l'exercice pour la multiplication
def afficher_exercice2():
    return '''
    <div class="form-container">
        <h1>Exercice de multiplication</h1>
        <form method="POST" class="exercise-form">
            <input type="text" name="a" placeholder="Entrez le premier nombre" required>
            <input type="text" name="b" placeholder="Entrez le deuxième nombre" required>
            <button type="submit" name="operation" value="multiplication">Multiplier les nombres</button>
        </form>
    </div>
    '''

    # Affichage de l'exercice pour la soustraction
def afficher_exercice3():
    return '''
    <div class="form-container">
        <h1>Exercice de soustraction</h1>
        <form method="POST" class="exercise-form">
            <input type="text" name="a" placeholder="Entrez le premier nombre" required>
            <input type="text" name="b" placeholder="Entrez le deuxième nombre" required>
            <button type="submit" name="operation" value="soustraction">Soustraire les nombres</button>
        </form>
    </div>
    '''

# Affichage de l'exercice pour le prénom
def afficher_exercice4():
    first_name = "Bryan"  # Définir la variable first_name
    return f'''
    <div class="form-container">
        <h1>Exercice de prénom</h1>
        <p>Bonjour {first_name}!</p>
    </div>
    '''


# Affichage de l'exercice pour la saisie du prénom
def afficher_exercice5():
    return '''
    <div class="form-container">
        <h1>Exercice de prénom</h1>
        <form method="POST" class="exercise-form">
            <input type="text" name="first_name" placeholder="Entrez votre prénom" required>
            <button type="submit">Soumettre</button>
        </form>
    </div>
    '''

# Affichage de l'exercice pour la saisie du prénom, nom et année de naissance
def afficher_exercice6():
    return '''
    <div class="form-container">
        <h1>Exercice de Saisie d'Informations</h1>
        <form method="POST" class="exercise-form">
            <input type="text" name="prenom" placeholder="Entrez votre prénom" required>
            <input type="text" name="nom" placeholder="Entrez votre nom" required>
            <input type="number" name="annee_naissance" placeholder="Entrez votre année de naissance" required>
            <button type="submit">Soumettre</button>
        </form>
    </div>
    '''

# Affichage de l'exercice pour le calcul de l'IMC
def afficher_exercice7():
    return '''
    <div class="form-container">
        <h1>Exercice de Calcul de l'IMC</h1>
        <form method="POST" class="exercise-form">
            <input type="number" name="poids" placeholder="Entrez votre poids (kg)" required>
            <input type="number" name="taille" placeholder="Entrez votre taille (m)" required>
            <button type="submit">Calculer l'IMC</button>
        </form>
    </div>
    '''

