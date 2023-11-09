import pygame
import cv2
from pygame.locals import *
from pygame.mixer import pre_init, get_init, Sound
from array import array
import math
import time
import random

# Classe pour générer des notes de musique
class Note(Sound):
    def __init__(self, fréquence, volume=0.01):
        self.fréquence = fréquence
        Sound.__init__(self, self.construire_échantillons())
        self.set_volume(volume)

    # Méthode pour construire des échantillons sonores
    def construire_échantillons(self):
        période = int(round(get_init()[0] / self.fréquence))
        échantillons = array("h", [0] * période)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for temps in range(période):
            if temps < période / 2:
                échantillons[temps] = amplitude
            else:
                échantillons[temps] = -amplitude
        return échantillons

# Initialisation de Pygame et Pygame Mixer
pre_init(44100, -16, 1, 1024)
pygame.init()
pygame.mixer.init()

# Chargement de l'image et obtention de ses dimensions
image = cv2.imread('foreground_image.jpg')
X = image.shape[1]
Y = image.shape[0]

# Randomisation de la position initiale de rect3 dans la fenêtre
rect3_x = random.randint(0, X - 16)
rect3_y = random.randint(0, Y - 16)

# Création de la fenêtre de jeu
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Trouvez le point d\'intérêt')

# Chargement et affichage de l'image sur la fenêtre de jeu
imp = pygame.image.load('foreground_image.jpg').convert()
screen.blit(imp, (0, 0))
pygame.display.flip()

# Initialisation des variables de jeu et de l'horloge
status = True
clock = pygame.time.Clock()
FPS = 60

# Fonction pour calculer la distance entre deux points
def calculer_distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

# Classe du joueur
class Joueur(object):
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (0, 0, 128), (64, 54, 16, 16))
        self.dist = 2

    # Gestion des touches
    def gérer_touches(self):
        touches = pygame.key.get_pressed()
        for événement in pygame.event.get():
            if événement.type == QUIT:
                pygame.quit()
                exit()

        self.dx = 0
        self.dy = 0

        touches = pygame.key.get_pressed()

        if touches[K_LEFT]:
            self.dx = -self.dist
            self.jouer_son()
        if touches[K_RIGHT]:
            self.dx = self.dist
            self.jouer_son()
        if touches[K_UP]:
            self.dy = -self.dist
            self.jouer_son()
        if touches[K_DOWN]:
            self.dy = self.dist
            self.jouer_son()
        self.dessiner_rectangle(self.dx, self.dy)

    # Jouer un son
    def jouer_son(self):
        distance = calculer_distance(self.rect.x, self.rect.y, rect3_x, rect3_y)
        fréquence_max = 300
        fréquence_min = 100
        fréquence = fréquence_min + (fréquence_max - fréquence_min) * (1 - distance / X)
        Note(fréquence).play(1)

    # Dessiner le rectangle du joueur
    def dessiner_rectangle(self, x, y):
        self.rect = self.rect.move(x * self.dist, y * self.dist)
        screen.blit(imp, (0, 0))
        pygame.draw.rect(screen, (0, 0, 128), self.rect)
        pygame.display.update()

# Création de l'objet Joueur
joueur = Joueur()

# Obtention de l'heure de début
heure_de_début = time.time()

# Définition des polices pour le rendu du texte
police = pygame.font.Font(None, 36)
police_message_fin = pygame.font.Font(None, 72)

# Boucle principale du jeu
while status:
    for événement in pygame.event.get():
        if événement.type == pygame.QUIT:
            status = False

    rect3 = pygame.draw.rect(screen, (255, 0, 0), (rect3_x, rect3_y, 16, 16))
    screen.blit(imp, (0, 0))
    pygame.draw.rect(screen, (0, 0, 255), joueur.rect)

    # Calcul du temps écoulé
    temps_écoulé = time.time() - heure_de_début

    secondes = int(temps_écoulé)
    message_temps_écoulé = police.render(f"Temps écoulé : {secondes} secondes", True, (255, 255, 255))
    screen.blit(message_temps_écoulé, (10, 10))
    joueur.gérer_touches()

    clock.tick(FPS)

    if joueur.rect.colliderect(rect3):
        status = False
        message_gagné = police_message_fin.render("Vous avez trouvé le point d'intérêt !", True, (0, 255, 0))
        screen.blit(message_gagné, (X // 2 - 220, Y // 2))
        message_temps_écoulé = police.render(f"Temps écoulé : {secondes} secondes", True, (255, 255, 255))
        screen.blit(message_temps_écoulé, (X // 2 - 150, Y // 2 + 50))
        pygame.display.update()
        pygame.time.delay(2000)  # Pause de 2 secondes

    if temps_écoulé >= 60:
        status = False
        message_perdu = police_message_fin.render("Vous avez perdu !", True, (255, 0, 0))
        screen.blit(message_perdu, (X // 2 - 100, Y // 2))
        message_temps_écoulé = police.render(f"Temps écoulé : {secondes} secondes", True, (255, 255, 255))
        screen.blit(message_temps_écoulé, (X // 2 - 75, Y // 2 + 50))
        pygame.display.update()
        pygame.time.delay(2000)  # Pause de 2 secondes

pygame.quit()
