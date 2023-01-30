import pygame as pg
import sys
from parametres import *
from carte import *
from joueur import *

class Jeu:
    def __init__(self):
        pg.init()
        self.ecran = pg.display.set_mode(RES)
        self.horloge = pg.time.Clock()
        self.dt = 1
        self.nouvelle_part()

    def nouvelle_part(self):
        self.carte = Carte(self)
        self.joueur = Joueur(self)

    def maj(self):
        self.joueur.maj()
        pg.display.flip()
        self.dt = self.horloge.tick(FPS)
        pg.display.set_caption(f'{self.horloge.get_fps():.1f}')

    def dessine(self):
        self.ecran.fill('black')
        self.carte.dessiner()
        self.joueur.dessiner()

    def cheque_evenements(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def execute(self):
        while True:
            self.cheque_evenements()
            self.maj()
            self.dessine()

if __name__ == '__main__':
    j = Jeu()
    j.execute()
