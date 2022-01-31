from tinydb import TinyDB
from tinydb.table import Document
from modeles.joueur import Joueur
from modeles.match import Match
from modeles.round import Round
from modeles.tournoi import Tournoi

db = TinyDB('db.json')
joueurs_table = db.table('joueurs')
tournois_table = db.table('tournois')

def chargement_joueur():
    joueurs_document = players_table.all()
    joueurs = []
    for joueur in joueurs_document:
        joueur = deserie_joueur(joueur)
        joueurs.append(joueur)
    return joueurs

def inserer_joueur(joueur):
    joueurs_table.insert(Document(joueur.serie(), doc_id=joueur.id))

def inserer_tournoi(tournoi):
    tournois_table.insert(tournoi.serie())

def inserer_tournois(tournois):
    for tournoi in tournois:
        inserer_tournoi(tournoi)

def inserer_joueurs(joueurs):
    for joueur in joueurs:
        inserer_joueur(joueur)

def obtiens_joueur(id):
    return joueurs_table.get(doc_id=int(id))


def deserie_tournoi(tournoi: Document):
    tournoi_id = tournoi.doc_id
    nom = tournoi['nom']
    date = tournoi['date']
    nombretotalround = tournoi['nombretotalround']
    round_encours = tournoi['round_encours']
    joueurs = [deserie_joueur((joueur_id)) for
               joueur_id in tournoi['joueurs']]
    statut = tournament['statut']
    listes_rounds = [deserie_round(round) for
                      round in tournament['listes_rounds']]
    scores = {int(key): values for key, values in tournoi['scores'].items()}
    adversaires = {int(key): values for
                 key, values in tournoi['adversaires'].items()}
    controle_temps = tournament['controle_temps']
    description = tournament['description']
    return Tournoi(tournament_id, nom, date, controle_temps, description,
                      nombretotalround, round_encours, joueurs,
                      statut, listes_rounds, scores, adversaires)

def deserie_round(round: Document):
    nom_round = round['nom_round']
    nombre_round = round['nombre_round']
    listesmatches = [deserie_match(match) for
                       match in round['listesmatches']]
    commence = round['commence']
    fini = round['fini']
     return Round(nom_round, nombre_round,
                 listesmatches, commence, fini)

def deserie_match(match: Document):
    statut = match['statut']
    idjoueur_1 = match['idjoueur_1']
    idjoueur_2 = match['idjoueur_2']
    scorejoueur_1 = match['scorejoueur_1']
    scorejoueur_2 = match['scorejoueur_2']
    return Match(statut, idjoueur_1, idjoueur_2,
                 scorejoueur_1, scorejoueur_2)

def deserie_joueur(joueur: Document):
    prenom= joueur['prenom']
    nom = joueur['nom']
    sexe= joueur['sexe']
    classement = joueur['classement']
    joueur_id = joueur.doc_id
    return Joueur(joueur_id, prenom, nom, sexe, classement)

def chargement_tournoi():
    tournoi_document = tournois_table.all()
    tournois= []
    for tournoi in tournoi_document:
        tournoi = deserie_tournoi(tournoi)
        tournois.append(tournoi)
    return tournois

def tronque_tournoi():
    tournois_table.truncate()

def tronque_joueur():
    joueurs_table.truncate()

def chjoueur_classement(joueur_id, nouveau_classement):
    joueurs_table.update({'rating': nouveau_classement}, doc_ids=[joueur_id])
    joueurs_table.all()

def sauvegarde(tournoi):
    tournois_table.truncate()
    inserer_tournois(tournois)

    









