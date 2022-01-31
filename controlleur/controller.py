from vues import menup
from vues import fonctions
from vues import menutournoi 
from modeles.tournoi import Tournoi
from modeles.joueur import Joueur 
from modeles import donnees


class Controllar:
    def menu_principale(self):
        while True:
            reponse = menup.menu_origin()
            
