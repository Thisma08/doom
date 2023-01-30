from parametres import *
import pygame as pg
import math

class Joueur:
    def __init__(self, j):
        self.jeu = j
        self.x, self.y = POS_JOUEUR
        self.angle = ANGLE_JOUEUR

    def bouger(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        vitesse = VITESSE_JOUEUR * self.jeu.dt
        sin_vit = vitesse * sin_a
        cos_vit = vitesse * cos_a

        touches = pg.key.get_pressed()
        if touches[pg.K_z]:
            dx += cos_vit
            dy += sin_vit
        if touches[pg.K_s]:
            dx += -cos_vit
            dy += -sin_vit
        if touches[pg.K_q]:
            dx += sin_vit
            dy += -cos_vit
        if touches[pg.K_d]:
            dx += -sin_vit
            dy += cos_vit

        # self.x += dx
        # self.y += dy
        self.chequer_collision_murs(dx, dy)

        if touches[pg.K_LEFT]:
            self.angle -= VITESSE_ROT_JOUEUR * self.jeu.dt
        if touches[pg.K_RIGHT]:
            self.angle += VITESSE_ROT_JOUEUR * self.jeu.dt
        self.angle %= math.tau

    def chequer_murs(self, x, y):
        return (x, y) not in self.jeu.carte.carte_monde

    def chequer_collision_murs(self, dx, dy):
        if self.chequer_murs(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.chequer_murs(int(self.x), int(self.y + dy)):
            self.y += dy

    def dessiner(self):
        pg.draw.circle(self.jeu.ecran, 'green', (self.x * 100, self.y * 100), 15)

        pg.draw.line(self.jeu.ecran, 'yellow', (self.x * 100, self.y * 100),
                     (self.x * 100 + LARG * math.cos(self.angle),
                      self.y * 100 + LARG * math.sin(self.angle)), 2)

    def maj(self):
        self.bouger()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def carte_pos(self):
        return int(self.x), int(self.y)