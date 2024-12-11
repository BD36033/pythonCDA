import requests

# L'URL de l'API
url = "https://gourmandise-api.bdessis.v70208.campus-centre.fr/products"

# Envoyer une requête GET à l'API
response = requests.get(url)

# Vérifier si la requête a réussi (code HTTP 200)
if response.status_code == 200:
    # La réponse de l'API est au format JSON, donc on la charge
    data = response.json()
    
    # Afficher les données reçues
    print("Données récupérées de l'API :")
    for item in data:
        print(f"Nom : {item.get('designation')}, Prix : {item.get('prix_unitaire_HT')}, Description : {item.get('descriptif')}")
else:
    print(f"Erreur de la requête. Code de statut : {response.status_code}")
