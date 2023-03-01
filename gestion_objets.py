from objet_sprite import *

class GestionObjets:
    def __init__(self, j):
        self.jeu = j
        self.liste_sprites = []
        self.chemin_sprites_statiques = 'ressources/sprites/statiques/'
        self.chemin_sprites_animes = 'ressources/sprites/animes/'

        self.ajouter_sprite(ObjetSprite(j))
        self.ajouter_sprite(SpriteAnime(j))
        self.ajouter_sprite(SpriteAnime(j, p=(1.5, 1.5)))
        self.ajouter_sprite(SpriteAnime(j, p=(1.5, 7.5)))
        self.ajouter_sprite(SpriteAnime(j, p=(5.5, 3.25)))
        self.ajouter_sprite(SpriteAnime(j, p=(5.5, 4.75)))
        self.ajouter_sprite(SpriteAnime(j, p=(7.5, 2.5)))
        self.ajouter_sprite(SpriteAnime(j, p=(7.5, 5.5)))
        self.ajouter_sprite(SpriteAnime(j, p=(14.5, 1.5)))
        self.ajouter_sprite(SpriteAnime(j, c=self.chemin_sprites_animes+'flamme_rouge/0.png', p=(14.5, 7.5)))
        self.ajouter_sprite(SpriteAnime(j, c=self.chemin_sprites_animes+'flamme_rouge/0.png', p=(12.5, 7.5)))
        self.ajouter_sprite(SpriteAnime(j, c=self.chemin_sprites_animes+'flamme_rouge/0.png', p=(9.5, 7.5)))

    def maj(self):
        [s.maj() for s in self.liste_sprites]

    def ajouter_sprite(self, sprite):
        self.liste_sprites.append(sprite)
