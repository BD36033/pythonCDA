from flask import Blueprint, request, render_template_string, render_template
from test import afficher_exercice2, afficher_exercice3, afficher_exercice4, afficher_exercice5, afficher_exercice6, afficher_exercice7, soustraire, calculer_multiplication, contenu_page, calculer_somme, afficher_exercice1
import requests
# from ..calendrier import calendrier 
# Définir un blueprint
route = Blueprint('route', __name__)
taches = {}
# route.register_blueprint(calendrier)

def nav_bar():
    return '''
    <nav>
        <ul>
            <li><a href="/">Accueil</a></li>
            <li><a href="/test">Exercice</a></li>
            <li><a href="/cours">Cours</a></li>
            <li><a href="/calendrier">Calendrier</a></li>
            <li><a href="/api-data">Liste produits</a></li>
        </ul>
    </nav>
    '''

@route.route('/')
def home():
    # Liste des exercices
    exercices = [
        {"nom": "Addition", "fonction": calculer_somme},
        {"nom": "Multiplication", "fonction": calculer_multiplication},
        {"nom": "Soustraction", "fonction": soustraire}
    ]
    
    # Comptage des exercices
    nombre_exercices = len(exercices)

    # Liste des thèmes abordés dans /cours
    themes_cours = [
        "Introduction à Python",
        "Structures de données",
        "Contrôle de flux",
        "Fonctions et modules",
        "Programmation orientée objet"
    ]
    
    # Comptage des thèmes de cours
    nombre_themes = len(themes_cours)

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
            <style>
                .bar-chart {
                    display: flex;
                    align-items: flex-end;
                    justify-content: center;
                    height: 300px;
                    width: 100%;
                    background-color: #f4f4f4;
                    border: 1px solid #ddd;
                    padding: 20px;
                    box-sizing: border-box;
                }
                .bar {
                    width: 50px;
                    margin: 0 10px;
                    background-color: #007bff;
                    color: white;
                    text-align: center;
                    line-height: 1.5;
                    border-radius: 5px 5px 0 0;
                    transition: all 0.3s ease;
                }
                .bar:hover {
                    background-color: #0056b3;
                }
                .label {
                    text-align: center;
                    margin-top: 5px;
                    font-size: 14px;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            ''' + nav_bar() + '''
            <div class="home-content">
                <h1>Accueil Python</h1>
                <p>Statistiques :</p>
                <div class="bar-chart">
                    <div>
                        <div class="bar" style="height: {{ nombre_exercices * 50 }}px;">{{ nombre_exercices }}</div>
                        <div class="label">Exercices</div>
                    </div>
                    <div>
                        <div class="bar" style="height: {{ nombre_themes * 50 }}px; background-color: #28a745;">{{ nombre_themes }}</div>
                        <div class="label">Thèmes</div>
                    </div>
                </div>
            </div>
        </body>
        </html>
    ''', nombre_exercices=nombre_exercices, nombre_themes=nombre_themes)


@route.route('/test', methods=['GET', 'POST'])
def test():
    result_somme = ""
    result_multiplication = ""
    result_soustraction = ""
    first_name = ""  # Initialiser first_name
    birth_message = ""  # Initialiser le message de naissance
    imc_message = ""  # Initialiser le message d'IMC

    if request.method == 'POST':
        # Vérifiez si le formulaire de prénom a été soumis
        if 'first_name' in request.form:
            first_name = request.form['first_name']  # Récupérer le prénom saisi
        elif 'prenom' in request.form:  # Vérifiez si le formulaire d'exercice 6 a été soumis
            prenom = request.form['prenom']
            nom = request.form['nom']
            annee_naissance = int(request.form['annee_naissance'])
            birth_message = f"Vous êtes né en {annee_naissance}."  # Créer le message de naissance
        elif 'poids' in request.form and 'taille' in request.form:  # Vérifiez si le formulaire d'IMC a été soumis
            poids = float(request.form['poids'])
            taille = float(request.form['taille'])
            if taille > 0:  # Éviter la division par zéro
                imc = poids / (taille ** 2)  # Calculer l'IMC
                imc_message = f"Votre IMC est de {imc:.2f}."  # Créer le message d'IMC
            else:
                imc_message = "La taille doit être supérieure à zéro."
        else:
            a = float(request.form.get('a', 0))  # Utiliser .get() pour éviter KeyError
            b = float(request.form.get('b', 0))
            operation = request.form.get('operation')

            if operation == "somme":
                result_somme = calculer_somme(a, b)
            elif operation == "multiplication":
                result_multiplication = calculer_multiplication(a, b)
            elif operation == "soustraction":
                result_soustraction = soustraire(a, b)

    return render_template_string('''<!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
        </head>
        <body>
            ''' + nav_bar() + '''
            ''' + afficher_exercice1() + '''
            <h2>Résultat de l'addition : {{ result_somme }}</h2>
            
            ''' + afficher_exercice2() + '''
            <h2>Résultat de la multiplication : {{ result_multiplication }}</h2>

            ''' + afficher_exercice3() + '''
            <h2>Résultat de la soustraction : {{ result_soustraction }}</h2>
            
            ''' + afficher_exercice5() + '''  <!-- Appel de la fonction afficher_exercice5 -->
            {% if first_name %}
                <p>Bonjour {{ first_name }}!</p>  <!-- Afficher le prénom saisi -->
            {% endif %}
            
            ''' + afficher_exercice6() + '''  <!-- Appel de la fonction afficher_exercice6 -->
            {% if birth_message %}
                <p>{{ birth_message }}</p>  <!-- Afficher le message de naissance -->
            {% endif %}
            
            ''' + afficher_exercice7() + '''  <!-- Appel de la fonction afficher_exercice7 -->
            {% if imc_message %}
                <p>{{ imc_message }}</p>  <!-- Afficher le message d'IMC -->
            {% endif %}
        </body>
        </html>
    ''', result_somme=result_somme, result_multiplication=result_multiplication, result_soustraction=result_soustraction, first_name=first_name, birth_message=birth_message, imc_message=imc_message)


@route.route('/cours')
def cours():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
        </head>
        <body>
            ''' + nav_bar() + '''
            <div class="cours-content">
                <h1>Cours de Python</h1>
                <p>Bienvenue dans le cours de Python. Ici vous trouverez des ressources et des exercices pour améliorer vos compétences.</p>
                <h2>Thèmes abordés :</h2>
                <ul>
                    <li>Introduction à Python</li>
                    <li>Structures de données</li>
                    <li>Contrôle de flux</li>
                    <li>Fonctions et modules</li>
                    <li>Programmation orientée objet</li>
                </ul>
                <h2>Notions de base pour apprendre Python :</h2>
                <ul>
                    <li><strong>Syntaxe de base :</strong> Comprendre comment écrire des instructions simples et utiliser des commentaires.</li>
                    <li><strong>Types de données :</strong> Connaître les types de données de base (int, float, string, list, dict, etc.) et leur utilisation.</li>
                    <li><strong>Conditions :</strong> Apprendre à utiliser les instructions conditionnelles (if, elif, else) pour prendre des décisions.</li>
                    <li><strong>Boucles :</strong> Utiliser des boucles (for, while) pour itérer sur des séquences ou des collections.</li>
                    <li><strong>Fonctions :</strong> Comprendre comment définir et appeler des fonctions pour structurer le code.</li>
                    <li><strong>Gestion des erreurs :</strong> Utiliser try et except pour gérer les exceptions et rendre le code plus robuste.</li>
                    <li><strong>Modules et bibliothèques :</strong> Apprendre à importer et utiliser des modules pour étendre les fonctionnalités de base de Python.</li>
                </ul>
            </div>
        </body>
        </html>
    ''')


@route.route('/calendrier', methods=['GET', 'POST'])
def calendrier_view():
    if request.method == 'POST':
        date = request.form['date']  # Récupère la date du formulaire
        jour = request.form['jour']  # Récupère le jour du formulaire
        tache = request.form['tache']  # Récupère la tâche du formulaire
        
        # Crée une clé combinée pour stocker les tâches par date et jour
        key = f"{date} - {jour}"
        
        if key in taches:
            taches[key].append(tache)  # Ajoute la tâche à la liste existante
        else:
            taches[key] = [tache]  # Crée une nouvelle entrée avec la tâche

    return render_template('calendrier.html', taches=taches, nav_bar=nav_bar()) 




@route.route('/api-data', methods=['GET'])
def afficher_api_data():
    # URL de l'API
    api_url = "https://gourmandise-api.bdessis.v70208.campus-centre.fr/products"
    
    try:
        # Envoyer une requête GET à l'API
        response = requests.get(api_url)
        response.raise_for_status()  # Lève une exception si le statut HTTP indique une erreur
        data = response.json()  # Extraire les données JSON

        # Passer les données à un template
        return render_template('api_data.html', products=data, nav_bar=nav_bar)
    except requests.exceptions.RequestException as e:
        # En cas d'erreur, afficher un message
        return f"Erreur lors de la récupération des données : {e}"




if __name__ == '__main__':
    route.run(debug=True)


