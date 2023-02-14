import pygame as pg
from parametres import *


class ObjetSprite:
    def __init__(self, j, c='ressources/sprites/statiques/chandelle.png', p=(10.5, 3.5)):
        self.jeu = j
        self.joueur = j.joueur
        self.x, self.y = p
        self.image = pg.image.load(c).convert_alpha()
        self.LARG_IM = self.image.get_width()
        self.DEMI_LARG_IM = self.image.get_width() // 2
        self.RATIO_IM = self.LARG_IM / self.image.get_height()
        self.dx, self.dy, self.theta, self.x_ecran, self.dist, self.dist_norm = 0, 0, 0, 0, 1, 1
        self.demi_larg_sprite = 0

    def get_projection_sprite(self):
        proj = DIST_MUR / self.dist_norm
        larg_proj, haut_proj = proj * self.RATIO_IM, proj

        image = pg.transform.scale(self.image, (larg_proj, haut_proj))

        self.demi_larg_sprite = larg_proj // 2
        pos = self.x_ecran - self.demi_larg_sprite, DEMI_HAUT - haut_proj // 2

        self.jeu.rc.objets_a_rendre.append((self.dist_norm, image, pos))

    def get_sprite(self):
        dx = self.x - self.joueur.x
        dy = self.y - self.joueur.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.joueur.angle
        if(dx > 0 and self.joueur.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        d_rays = delta / D_ANGLE
        self.x_ecran = (DEMI_NB_RAYONS + d_rays) * ECHELLE

        self.dist = math.hypot(dx, dy)
        self.dist_norm = self.dist * math.cos(delta)
        if -self.DEMI_LARG_IM < self.x_ecran < (LARG + self.DEMI_LARG_IM) and self.dist_norm > 0.5:
            self.get_projection_sprite()

    def maj(self):
        self.get_sprite()
