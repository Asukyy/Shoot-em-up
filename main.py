import pygame
import random

pygame.init()

display_width = 800
display_height = 600

car_width = 73
ammo_width = 20
ammo_height = 40
ammo_speed = 5

fenetre = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Mon jeu de vaisseau')

carImg = pygame.image.load('assets/mainV.png')
carImg = pygame.transform.scale(carImg, (car_width, car_width))
VaisseauEnnemiImg = pygame.image.load('assets/vaisseauE1.png')
VaisseauEnnemiImg = pygame.transform.scale(VaisseauEnnemiImg, (car_width, car_width))
ammoImg = pygame.image.load('assets/ammo.png')
ammoImg = pygame.transform.scale(ammoImg, (ammo_width, ammo_height))

# position initiale du vaisseau
x = (display_width - car_width) / 2
y = display_height - car_width

# position initiale de la balle
ammo_x = x + car_width / 2 - ammo_width / 2
ammo_y = y

# vitesse de déplacement du vaisseau
vitesse = 3

# liste des balles
balles = []

# boucle d'événements pour garder la fenêtre ouverte
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    # vérifier les touches appuyées pour contrôler le mouvement
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and x > 0 or touches[pygame.K_q] and x > 0:
        x -= vitesse
    if touches[pygame.K_RIGHT] and x < display_width - car_width or touches[pygame.K_d] and x < display_width - car_width:
        x += vitesse
    if touches[pygame.K_UP] and y > 0 or touches[pygame.K_z] and y > 0:
        y -= vitesse
    if touches[pygame.K_DOWN] and y < display_height - car_width or touches[pygame.K_s] and y < display_height - car_width:
        y += vitesse
        
        
    #si on appuie sur espace, on tire et on peut spam mais pas rester appuyer
    if touches[pygame.K_SPACE]:
        balles.append([x + car_width / 2 - ammo_width / 2, y])

    # Remplir la fenêtre avec une couleur de fond noire
    fenetre.fill((0, 0, 0))

    # Afficher l'image du vaisseau à sa position actuelle
    fenetre.blit(carImg, (x, y))

    # Boucle pour afficher et faire avancer toutes les balles
    for balle in balles:
        # Afficher la balle
        fenetre.blit(ammoImg, (balle[0], balle[1]))
        # Faire avancer la balle
        balle[1] -= ammo_speed
        

    # Rafraîchir l'écran
    pygame.display.flip()
            
    # Générer un vaisseau ennemi
    if random.randint(0, 100) == 0:
        fenetre.blit(VaisseauEnnemiImg, (random.randint(0, display_width - car_width), 0))

pygame.quit()