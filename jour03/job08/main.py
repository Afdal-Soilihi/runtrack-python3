def afficher_produits(type, saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("Artichaut, aubergine, navet")
    else:
        print("Aucune correspondance trouvée pour le type et la saison donnés")

# Appels de la fonction avec différents paramètres
afficher_produits("fruits", "hiver")
afficher_produits("fruits", "ete")
afficher_produits("legume", "hiver")
afficher_produits("legume", "ete")
afficher_produits("poisson", "printemps")  # Exemple avec des valeurs non spécifiées dans les conditions