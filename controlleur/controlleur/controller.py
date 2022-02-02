from vues import menup
from vues import fonctions
from vues import menutournoi 
from modeles.tournoi import Tournoi
from modeles.joueur import Joueur 
from modeles import donnees


class Controllar:

    def __init__(self):
        self.joueurdonnes = donnees.chargement_joueur()
        self.tournoi_donnes = donnees.chargement_tournoi()

    def obtournoi(self):
        tournoi_id = fonctions.choisir_t(self.tournoi_donnes)
        for tournoi in self.tournoi_donnes:
            if tournoi.id == int(tournoi_id):
                ctournoi = tournoi
                return ctournoi
        return None

    def menudutournoi(self, tournoi):
        quitter_menu = False
        while not quitter_menu:
            reponse = menutournoi.menu_tournoi()
            if reponse == 'A':  
                if len(tournoi.joueurs) == 8:
                    fonctions.erreurmessage('Le tournoi est complet')
                    return
                fonctions.montre_joueurs(self.joueurdonnes)
                choix = fonctions.ajoueurtournoi()
                for joueur in self.joueurdonnes:
                    if choix == joueur.id:
                        if joueur in tournoi.joueurs:
                            fonctions.erreurmessage('Joueur deja dans le tournoi ')
                        else:
                            tournoi.ajout(joueur)
                            donnees.sauvegarde(self.tournoi_donnes)
                        break

    def menu_principale(self):
        while True:
            reponse = menup.menu_origin()
            if reponse == "A":
                prenom = ""
                nom = ""
                sexe = ""
                classement = ""

                valide = False
                while not valide:
                    prenom = fonctions.demande_question(
                        "Prenom s'il vous plait\n")
                    if prenom == "":
                        fonctions.erreurmessage(" Mettez le prenom s'il vous plait\n")
                    else:
                        valide = True
                
                valide = False
                while not valide:
                    nom = fonctions.demande_question(
                        "Nom s'il vous plait\n")
                    if nom == "":
                        fonctions.erreurmessage(" Mettez le nom s'il vous plait\n")
                    else:
                        valide = True

                valide = False
                while not valide:
                    sexe = fonctions.demande_question(
                        "Sexe de la personne s'il vous plait\n")
                    if sexe == "":
                        fonctions.erreurmessage("Mettez le sexe de la personne ?\n")
                    else:
                        valide = True

                valide = False
                while not valide:
                    classement = fonctions.demande_question("Le classement du joueur\n")
                    if classement == "":
                        fonctions.erreurmessage('Mettez le classement.\n')
                    elif not classement.isnumeric():
                        fonctions.erreurmessage('Cela doit etre un entier\n')
                    else:
                        valide = True

                id = 0 if len(self.joueurdonnes) == 0 else \
                    self.joueurdonnes[-1].id
                id += 1
                joueur = Joueur(id, prenom, nom,
                                sexe, classement)
                donnees.inserer_joueur(joueur)
                self.joueurdonnes.append(joueur)

            

            elif reponse == 'G':  
                    self.joueurdonnes = donnees.chargement_joueur()
                    tout_joueurs = sorted(
                            self.joueurdonnes,
                            key=lambda joueur: joueur.obtiens_prenom().upper())
                    fonctions.montre_joueurs(tout_joueurs)

            elif reponse == 'F':  
                    self.joueurdonnes = donnees.chargement_joueur()
                    tout_joueurs = sorted(
                            self.joueurdonnes,
                            key=lambda joueur: joueur.obtiens_classement(),
                            reverse=True)
                    fonctions.montre_joueurs(tout_joueurs)


            elif reponse == "C":
                tout_joueurs = self.joueurdonnes
                fonctions.montre_joueurs(tout_joueurs)
                idjoueur = fonctions.playerch_id()
                trouve = False
                for joueur in tout_joueurs:
                    if idjoueur == joueur.id:
                        trouve = True
                        nouveau_classement = fonctions.chjoueur_classement()
                        donnees.chjoueur_classement(joueur.id, nouveau_classement)
            
            elif reponse == "T":
                tournoi_nom = ""
                tournoi_date = ""
                tournoinombre = 4
                tournoicontrole_temps = ""
                tournoi_description = ""

                valide = False
                while not valide:
                    tournoi_nom = \
                        fonctions.demande_question('Nom du tournoi.\n')
                    if tournoi_nom == "":
                        fonctions.erreurmessage("Nom du tournoi s'il vous plait ?\n")
                    else:
                        valide = True
                        
                valide = False
                while not valide:
                    tournoi_date = \
                        fonctions.demande_question('Entrez les dates du tournoi .\n')
                    if tournoi_date == "":
                        fonctions.erreurmessage("Dates du tournoi s'il vous plait ?\n")
                    else:
                        valide = True 

                valide = False
                while not valide:
                    tournoinombre = \
                        fonctions.demande_question('Tapez le nombre de tournoi desire (max 7) \n')
                    if not tournoinombre.isdecimal():
                        fonctions.erreurmessage("Entier s'il vous plait")
                    elif not int(tournoinombre) in range(1, 8):
                        fonctions.erreurmessage("Inserer entre 1 et 7")
                    else:
                        valide= True

                valide = False 
                while not valide:
                    tournoicontrole_temps = \
                        fonctions.demande_question('le controle du temps :\n'
                                       '"4" pour bullet\n'
                                       '"5" pour blitz\n'
                                       '"6" pour rapide\n')
                    if tournoicontrole_temps not in ["4", "5", "6"]:
                        fonctions.erreurmessage('Reessayez\n')
                    else:
                        valide = True 
                
                valide = False
                while not valide:
                    tournoi_description = fonctions.demande_question(
                        "Veuillez entrer des informations complementaires\n")
                    if tournoi_description == "":
                        fonctions.erreurmessage('Ecrivez des informations.\n')
                    else:
                        valide = True

                id = 0 if len(self.tournoi_donnes) == 0 else \
                    self.tournoi_donnes[-1].id
                id += 1
                tournoi= Tournoi(id, tournoi_nom, tournoi_date,
                                        tournoicontrole_temps,
                                        tournoi_description,
                                        int(tournoinombre))
                donnees.inserer_tournoi(tournoi)
                self.tournoi_donnes.append(tournoi)

            elif reponse == "3": 
                tournoi = self.obtournoi()
                fonctions.momessage(f'Tournoi: {tournoi}')
                if tournoi is not None:
                    self.menudutournoi(tournoi)

            elif reponse== "M":   
                fonctions.montre_tout_tournois(self.tournoi_donnes)

            elif reponse == "Q":   # quit the program
                return
            else:
                fonctions.erreurmessage('Mauvais choix.')

                        

                

                




             


                

                    


            
