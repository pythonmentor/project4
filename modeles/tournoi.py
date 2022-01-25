from modeles.joueur import Joueur 
from modeles.round import Round
from modeles.match import Match

def obtiens_match (joueurs, adversaires):
    if len(joueurs) % 2 == 1 :
        return []
    if len(joueurs) == 0 :
        return[]
    premier_joueur = joueurs[0]
    for joueur in joueurs [1:]:
        if not joueur[0] in adversaires[premier_joueur[0]]:
            paire = (premier_joueur, joueur)
            joueur_restants = joueurs[1:]
            joueur_restants.remove(joueur)
            paires = obtiens_match(joueur_restants, adversaires)
            if paires is not None:
                return[paire] + paires

class Tournoi:
    def __init__(self, id, nom, date, controle_temps, description,
                 nombretotalround=4, round_encours=1,
                 joueurs=None, statut='initialisation',
                 listes_rounds=None, scores=None, adversaires=None):      
        if adversaires is None:
            adversaires = {}
        if scores is None:
            scores = {}
        if listes_rounds is None:
            listes_rounds = []
        if joueurs is None:
            joueurs = []

        self.id = id
        self.nom = nom
        self.date = date
        self.nombretotalround = nombretotalround
        self.round_encours = round_encours
        self.joueurs = joueurs
        self.statut = statut
        self.listes_rounds = listes_rounds
        self.scores = scores
        self.adversaires = adversaires
        self.controle_temps = controle_temps
        self.description = description

    def __repr__(self):
        return f'{self.nom}'

    def serie(self):
        serie_tournoi = {
            'nom': self.nom,
            'date': self.date,
            'nombretotalround': self.nombretotalround,
            'round_encours': self.round_encours,
            'joueurs': [joueur.id for joueur in self.joueurs],
            'statut': self.statut,
            'listes_rounds': [round.serie() for
                               round in self.listes_rounds],
            'scores': self.scores,
            'adversaires': self.adversaires,
            'controle_temps': self.controle_temps,
            'description': self.description
        }
        return serie_tournoi
    
    def ajout(self, joueur):        
        self.joueurs.append(joueur)
        self.scores[joueur.id] = [0, joueur.classement]
        self.adversaires[joueur.id] = []

    def round_suivant(self):
        if self.round_encours == 1 :
            self.joueurs = sorted(self.joueurs, key = Joueur.obtiens_classement,
                                  reverse = True)
            premier_partie = self.joueurs[:4]
            deuxieme_partie = self.joueurs[4:]
            listematches = []
            for joueur_a, joueur_b in zip (premier_partie, deuxieme_partie):
                match = Match('encours', joueur_a, joueur_b)
                listematches.append(match)
            round_un = Round('1', 1, listematches)
            self.listes_rounds.append(round_un)
            self.ajout_adversaire()
            self.round_encours +=1

        else:
            sorted_joueurs = sorted(self.scores.items(),
                                    key=lambda item: (item[1][0], item[1][1]),
                                    reverse=True) 
            listematches = []
            matches = obtiens_match(sorted_joueurs, self.adversaires)
            for paire in matches:
                match = Match ('on going', paire[0][0], paire[1][0])
                listematches.append(match)
            round_suiv = Round(f'round {self.round_encours} |',
                               self.round_encours, listematches)
            self.listes_rounds.append(round_suiv)
            self.ajout_adversaire()
            self.round_encours += 1

    def ajout_adversaire(self):
        for match in self.listes_rounds[-1].listematches:
            if not self.adversaires[match.idjoueur_1].count(match.idjoueur_2):
                self.adversaires[match.idjoueur_1].append(match.idjoueur_2)
            if not self.adversaires[match.idjoueur_2].count(match.idjoueur_1):
                self.adversaires[match.idjoueur_2].append(match.idjoueur_1)

    
    def round_fin(self):
        """finish the round and update the scores """
        self.listes_rounds[-1]round_fini()
        dernier_round = self.round_encours - 1
        for match in self.listes_rounds[dernier_round - 1].listematches:
            self.scores[match.idjoueur_1][0] += match.scorejoueur_1
            self.scores[match.idjoueur_2][0] += match.scorejoueur_2





