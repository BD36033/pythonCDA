def rendre_monnaie(montant, pieces):
    liste = []
    
    montant_en_centimes = int(montant * 100)

    pieces.sort(reverse=True)

    for piece in pieces:
        while montant_en_centimes >= piece:
            liste.append(piece)
            montant_en_centimes -= piece

    if montant_en_centimes > 0:
        print(f"Il reste un montant non rendu : {montant_en_centimes / 100:.2f}€")
    
    return liste

pieces = [200, 100, 50, 20, 10, 5, 2, 1, 500, 1000, 2000, 5000, 10000]
montant = 3.47

liste = rendre_monnaie(montant, pieces)

print("Pièces rendus :")
for piece in liste:
    print(f"{piece / 100:.2f}€")
