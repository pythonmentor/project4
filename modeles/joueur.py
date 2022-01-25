class Player:

    def __init__(self, id, prenom, nom, sexe, classement):
        self.id = id
        self.prenom = prenom
        self.nom = nom
        self.sexe = sexe
        self.classement = int(classement)

    def obtiens_classement(self):
        return self.classement

    def obtiens_sexe(self):
        return self.sexe

    def obtiens_id(self):
        return self.id

    def obtiens_nom(self):
        return self.nom

    def __repr__(self):
        return f'  # {self.id} - {self.prenom} ' \
               f'{self.nom} - Rating # {self.classement}'

    def serie(self):
        serie_joueur= {
            'prenom': self.prenom,
            'nom': self.nom,
            'sexe': self.sexe,
            'classement': self.classement
            }
        return serie_joueur
