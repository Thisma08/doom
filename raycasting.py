import pygame as pg
import math
from parametres import *

class RayCasting:
    def __init__(self, j):
        self.jeu = j

    def ray_cast(self):
        jx, jy = self.jeu.joueur.pos
        x_carte, y_carte = self.jeu.joueur.carte_pos
        angle_ray = self.jeu.joueur.angle - DEMI_FOV + 0.0001
        for ray in range(NB_RAYONS):
            angle_ray += D_ANGLE
            sin_a = math.sin(angle_ray)
            cos_a = math.cos(angle_ray)

            y_hor, dy = (y_carte + 1, 1) if sin_a > 0 else (y_carte - 1e-6, -1)
            prof_hor = (y_hor - jy) / sin_a
            x_hor = jx + prof_hor * cos_a
            d_prof = dy / sin_a
            dx = d_prof * cos_a

            for i in range(PROF_MAX):
                tuile_hor = int(x_hor), int(y_hor)
                if tuile_hor in self.jeu.carte.carte_monde:
                    break
                x_hor += dx
                y_hor += dy
                prof_hor += d_prof

            x_vert, dx = (x_carte + 1, 1) if cos_a > 0 else (x_carte - 1e-6, -1)
            prof_vert = (x_vert - jx) / cos_a
            y_vert = jy + prof_vert * sin_a
            d_prof = dx / cos_a
            dy = d_prof * sin_a

            for i in range(PROF_MAX):
                tuile_vert = int(x_vert), int(y_vert)
                if tuile_vert in self.jeu.carte.carte_monde:
                    break
                x_vert += dx
                y_vert += dy
                prof_vert += d_prof

            if prof_vert < prof_hor:
                prof = prof_vert
            else:
                prof = prof_hor

            #Retire l'effet "Fisheye"
            prof *= math.cos(self.jeu.joueur.angle - angle_ray)

            haut_proj = DIST_MUR / (prof + 0.0001)

            couleur = [255 / (1 + prof ** 5 * 0.00002)] * 3
            pg.draw.rect(self.jeu.ecran, couleur, (ray * ECHELLE, DEMI_HAUT - haut_proj // 2, ECHELLE, haut_proj))

    def maj(self):
        self.ray_cast()

