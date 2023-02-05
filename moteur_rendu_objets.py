import pygame as pg
from parametres import *

class MoteurRenduObjets:
    def __init__(self, j):
        self.jeu = j
        self.ecran = self.jeu.ecran
        self.textures_murs = self.charger_textures_murs()

    def dessiner(self):
        self.rendre_objets()

    def rendre_objets(self):
        liste_objets = self.jeu.rc.objets_a_rendre
        for prof, image, pos in liste_objets:
            self.ecran.blit(image, pos)

    @staticmethod
    def get_texture(chemin, res=(TAILLE_TEXTURE, TAILLE_TEXTURE)):
        texture = pg.image.load(chemin).convert_alpha()
        return pg.transform.scale(texture, res)

    def charger_textures_murs(self):
        return {
            1: self.get_texture('ressources/textures/m1.png'),
            2: self.get_texture('ressources/textures/m2.png')
        }
