import math

RES = LARG, HAUT = 1600, 900
DEMI_LARG = LARG // 2
DEMI_HAUT = HAUT // 2
FPS = 0

POS_JOUEUR = 1.5, 5
ANGLE_JOUEUR = 0
VITESSE_JOUEUR = 0.004
VITESSE_ROT_JOUEUR = 0.002
TAILLE_JOUEUR = 60

SENSIBILITE_SOURIS = 0.0001
MVT_REL_MAX_SOURIS = 40
BORDURE_GAUCHE_SOURIS = 100
BORDURE_DROITE_SOURIS = LARG - BORDURE_GAUCHE_SOURIS

COULEUR_SOL = (30, 30, 30)

FOV = math.pi / 3
DEMI_FOV = FOV / 2
NB_RAYONS = LARG // 2
DEMI_NB_RAYONS = NB_RAYONS // 2
D_ANGLE = FOV / NB_RAYONS
PROF_MAX = 20

DIST_MUR = DEMI_LARG / math.tan(DEMI_FOV)
ECHELLE = LARG // NB_RAYONS

TAILLE_TEXTURE = 256
DEMI_TAILLE_TEXTURE = TAILLE_TEXTURE // 2
