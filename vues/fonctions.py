def gagnant_match(match):
    while True:
        gagnant = input(f"Type '{match.idjoueur_1}' si le joueur 1 gagne\n"
                       f"Type '{match.idjoueur_2}' si le joueur 2 gagne\n"
                       f"Type 'N' si c'est un match nul \n")
        if not gagnant.isdecimal():
            print(" Le chiffre doit etre un entier et ne doit pas etre une decimale")
            continue
        return int(gagnant)

def demande_question(question):
    return input(question)

def montre_tout_tournois(touttournois):
    for tournoi in touttournois:
        print(f" Identifiant: {tournoi.id} /-/-/-/ Nom: {tournoi.nom}")

def montre_joueurs(tout_joueurs):
    for joueur in tout_joueurs:
        print(f"identifiant: {joueur.id} - Prenom et Nom: {joueur.prenom}"
              f" {joueur.nom} -  Niveau : {joueur.classement}") 

def joueurdanstournoi(touttournois, tout_joueurs):
    montre_tout_tournois(touttournois)
    tournoi_id = input("identifiant tournoi s'il vous plait\n")
    montre_joueurs(tout_joueurs)
    joueur_id = input(" Identifiant joueur s'il vous plait\n")
    return tournoi, joueur_id

def choisir_t(tournoi):
    montre_tout_tournois(tournoi)
    tournoi_id = input("identifiant tournoi s'il vous plait\n")
    while not tournoi_id.isdecimal():
        print('Entrez un entier sinon ca va mal aller')
        tournoi_id = input("identifiant tournoi s'il vous plait\n")
    return int(tournoi_id)


def montre_joueurs():
    return input("Tape pour voir les joueurs en fonction de leur classement \n"
                 "Tape pour voir les joueurs en fonction de leur classement\n")

def ajoueurtournoi():
    selection = input("Entre l'identifiant du joueur\n")
    while not selection.isdecimal():
        print('Entrez un entier sinon ca va mal aller')
        selection = input("Entre l'identifiant du joueur\n")
    return int(selection)

def erreurmessage(erreur):
    print(erreur)

def momessage(message):
    print(message)


def montreresultat(tournoiscores):
    if len(tournoiscores) >= 1:
        for id, score in tournoiscores.items():
            print(f'Joueur : {id}  (/-/-/-/)  Score : {score[0]}')
    else:
        print('Pas de donnees\n')


def montematches(nombre_rounds):
    if len(nombre_rounds) >= 1:
        for round in nombre_rounds:
            print(round.nom_round)
            for match in round.listematches:
                print(match)
    else:
        print('Erreur 404 erreur pas de donnees \n')

def montre_rounds(tournoi):
    if len(tournoi.listes_rounds) >= 1:
        for round in tournoi.listes_rounds:
            print(f'{round.nom_round} Commencement :'
                  f' {round.commence} Fini : {round.fini}')
    else:
        print('Erreur 404 erreur pas de donnees\n')

def playerch_id():
    player_id = input("Entrez l'identifiant du joueur\n")
    while not player_id.isdecimal():
        print("Must be integer")
        player_id = input("Entrez l'identifiant du joueur\n")
    return int(player_id)

def chjoueur_classement():
    nouveau_classement = input("C'est quoi le nouveau classement du joueur")
    while not new_rating.isdecimal():
        print("Erreur 404 erreur pas de donnees")
        nouveau_classement = input("C'est quoi le nouveau classement du joueur")
    return int(nouveau_classement)




