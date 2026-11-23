objets = {
    "lingot": [1000, 83200, 3],  # 1 kg
    "stylo bic": [50, 1, 10],  # 10 stylos
    "ordinateur portable": [2500, 1200, 2],  # 2 ordinateurs
    "chaîne Hi-Fi": [8000, 600, 1],  # 1 chaîne Hi-Fi
    "sac de riz": [20000, 50, 2],  # 2 sacs de riz
    "montre de luxe": [150, 2500, 1],  # 1 montre
    "vélo": [15000, 500, 1],  # 1 vélo
    "diamant": [200, 5000, 1],  # 1 diamant
    "livre": [300, 20, 20],  # 20 livres
    "télévision": [10000, 800, 2],  # 2 télévisions
    "plantatition d'herbe médicinal": [200000, 999999, 1],  # 1 plantation
    "console de jeu": [1200, 300, 1],  # 1 console
    "tablette graphique": [2000, 150, 1],  # 1 tablette graphique
    "chaise de bureau": [5000, 50, 2],  # 2 chaises
    "clavier mécanique": [1500, 80, 2],  # 2 claviers
    "guitare électrique": [3000, 600, 1],  # 1 guitare
    "paire de lunettes": [200, 20, 2],  # 2 paires
    "smartphone": [500, 1200, 2],  # 2 smartphones
    "machine à café": [8000, 250, 1],  # 1 machine
    "sac à dos": [900, 60, 2],  # 2 sacs à dos
    "enceinte Bluetooth": [700, 100, 2],  # 2 enceintes
    "douche solaire": [18000, 300, 1],  # 1 douche solaire
    "pistolet à eau": [300, 15, 5],  # 5 pistolets à eau
    "couteau suisse": [200, 50, 3],  # 3 couteaux suisses
    "scooter électrique": [12000, 1000, 1],  # 1 scooter
    "bouteille isotherme": [500, 20, 4],  # 4 bouteilles
    "planche de surf": [8000, 600, 1],  # 1 planche
    "parapluie pliable": [800, 25, 3],  # 3 parapluies
    "sèche-cheveux": [1500, 120, 2],  # 2 sèche-cheveux
    "drone": [3000, 800, 1],  # 1 drone
    "trottinette": [7000, 300, 1],  # 1 trottinette
    "boîte à outils": [5000, 150, 2],  # 2 boîtes
    "lampe torche": [300, 40, 5],  # 5 lampes torches
    "valise à roulettes": [10000, 300, 2],  # 2 valises
    "jeux de société": [2000, 50, 6],  # 6 jeux de société
    "sachet de poudre blanche": [500, 10000, 2],  # 500 g
    "armes à feu": [3000, 20000, 2],  # 2 armes
    "pièces d'or volées": [10000, 30000, 5],  # 5 pièces
    "drogue": [300, 15000, 2],  # 4 tablettes
    "matériel de contrebande": [10000, 8000, 1],  # 1 lot
    "bijoux volés": [2000, 25000, 3],  # 3 bijoux
    "cartons de cigarettes de contrebande": [20000, 500, 10],  # 10 cartons
    "documents falsifiés": [150, 7000, 2],  # 5 documents
    "dynamite": [2500, 15000, 1]  # 1 barre
}



poids_max = 30000
argent_total=0

def voleur(poids):
    global objets_voler,argent_total
    objets_voler = []
    while poids > 0:
        if not objets:
            break
        a = max(objets, key=lambda p: objets[p][1]/objets[p][0])
        if objets[a][0] <= poids:
            objets_voler.append(a)
            poids -= objets[a][0]
            argent_total+= objets[a][1]
            objets[a][2]-=1
            if objets[a][2]==0:
                del objets[a]
        elif objets[a][0] >poids:
            del objets[a]
        else:
            break

    print(f"Il reste dans la maison:\n{", ".join([f"{valeurs[-1]} {nom}" for nom, valeurs in objets.items()])}. \nIl reste {poids} grammes disponibles dans notre sac et nous avons gagné {argent_total} euros.")
    return print(f"Il n'y a plus de place dans le sac, mais nou avons quand même réussi à voler:\n{"\n".join(objets_voler)}")

voleur(poids_max)

