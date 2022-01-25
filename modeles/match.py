class Match:
    

    def __init__(self, statut, idjoueur_1, idjoueur_2,
                 scorejoueur_1=0, scorejoueur_2=0):
        self.statut = statut
        self.idjoueur_1 = idjoueur_1
        self.idjoueur_2 = idjoueur_2
        self.scorejoueur_1 = scorejoueur_1
        self.scorejoueur_2 = scorejoueur_2

    def __repr__(self):
        return f'Player {self.idjoueur_1} ({self.scorejoueur_1} pts)' \
               f' -- VS -- ' \
               f'Player {self.idjoueur_2} ({self.scorejoueur_2} pts)'

    def scoring(self, winner):
        if self.idjoueur_1 == winner:
            self.scorejoueur_1 = 1

        elif self.idjoueur_2 == winner:
            self.scorejoueur_2 = 1

        else:
            self.scorejoueur_1 = 0.5
            self.scorejoueur_2 = 0.5

        self.statut = 'Fini'

    def serie(self):
        """serialize a match"""
        serie_match = {
            'statut': self.statut,
            'idjoueur_1': self.idjoueur_1,
            'idjoueur_2': self.idjoueur_2,
            'scorejoueur_1': self.scorejoueur_1,
            'scorejoueur_2': self.scorejoueur_2
        }

        return serialized_match