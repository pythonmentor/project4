from datetime import datetime


class Round:
    def __init__(self, nom_round, nombre_round,
                 listematches, commence=None, fini=None):
        self.nom_round = nom_round
        self.nombre_round = int(nombre_round)
        self.listematches = listematches
        self.commence= commence if commence is not None else\
            datetime.now().strftime("%Y/%m/%d  %H:%M")
        self.fini = fini

    def __repr__(self):
        return f'{self.listematches}'

    def round_commence(self):
        self.commence = datetime.now().strftime("%Y/%m/%d  %H:%M")

    def round_fini(self):
        self.fini = datetime.now().strftime("%Y/%m/%d  %H:%M")

    def show_matches_in_round(self):
        for match in self.listematches:
            print(f'{self.nom_round}', match)

    def serie(self):
        serie_round = {
            'nom_round': self.nom_round,
            'nombre_round': self.nombre_round,
            'listematches': [match.serie() for
                                match in self.listematches],
            'commence': self.commence,
            'fini': self.fini
        }
        return serie_round
