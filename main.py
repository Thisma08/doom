import pygame as pg
import sys
from parametres import *
from carte import *
from joueur import *
from raycasting import *
from moteur_rendu_objets import *

class Jeu:
    def __init__(self):
        pg.init()
        self.ecran = pg.display.set_mode(RES)
        self.horloge = pg.time.Clock()
        self.dt = 1
        self.nouveau_jeu()

    def nouveau_jeu(self):
        self.carte = Carte(self)
        self.joueur = Joueur(self)
        self.mro = MoteurRenduObjets(self)
        self.rc = RayCasting(self)

    def maj(self):
        self.joueur.maj()
        self.rc.maj()
        pg.display.flip()
        self.dt = self.horloge.tick(FPS)
        pg.display.set_caption(f'{self.horloge.get_fps():.1f}')

    def dessine(self):
        self.ecran.fill('black')
        self.mro.dessiner()
        # self.carte.dessiner()
        # self.joueur.dessiner()

    def chequer_evenements(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def execute(self):
        while True:
            self.chequer_evenements()
            self.maj()
            self.dessine()

if __name__ == '__main__':
    j = Jeu()
    j.execute()
