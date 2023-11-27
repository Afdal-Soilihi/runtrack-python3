def check_nombre(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("Le nombre est égal à 0")

# Appels de la fonction avec différents paramètres
check_nombre(5)
check_nombre(-3)
check_nombre(0)