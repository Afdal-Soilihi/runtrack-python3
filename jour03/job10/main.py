def verifier_pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre pair.")
        else:
            print(f"{nombre} est un nombre impair.")
    else:
        print("Veuillez entrer un nombre entier positif.")

# Appels de la fonction avec différents paramètres
verifier_pair_impair(10)
verifier_pair_impair(7)
verifier_pair_impair(0)
verifier_pair_impair(-5)  # Un exemple avec un nombre négatif
verifier_pair_impair("abc")  # Un exemple avec une chaîne de caractères