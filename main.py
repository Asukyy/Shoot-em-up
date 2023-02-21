import pygame
import random

pygame.init()
#initialisation de la font

display_width = 800
display_height = 600

car_width = 73
ammo_width = 20
ammo_height = 40
ammo_speed = 5
enemy_width = 73
enemy_height = 73
enemy_speed = 2

score = 0
vie = 3

fenetre = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Mon jeu de vaisseau')

carImg = pygame.image.load('assets/mainV.png')
carImg = pygame.transform.scale(carImg, (car_width, car_width))
VaisseauEnnemiImg = pygame.image.load('assets/vaisseauE1.png')
VaisseauEnnemiImg = pygame.transform.scale(VaisseauEnnemiImg, (enemy_width, enemy_height))
ammoImg = pygame.image.load('assets/ammo.png')
ammoImg = pygame.transform.scale(ammoImg, (ammo_width, ammo_height))

# position initiale du vaisseau
x = (display_width - car_width) / 2
y = display_height - car_width

# vitesse de déplacement du vaisseau
vitesse = 5

# liste des balles
balles = []

# temps entre chaque tir (en millisecondes)
temps_entre_tirs = 200
dernier_tir = pygame.time.get_ticks() - temps_entre_tirs

# liste des ennemis
ennemis = []
# temps entre chaque création d'ennemi (en millisecondes)
temps_entre_ennemis = 1000
derniere_apparition = pygame.time.get_ticks() - temps_entre_ennemis

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
        
    # tirer une balle si la touche Espace est enfoncée et si le temps minimum entre les tirs est écoulé
    maintenant = pygame.time.get_ticks()
    if touches[pygame.K_SPACE] and maintenant - dernier_tir > temps_entre_tirs:
        dernier_tir = maintenant
        balles.append([x + car_width / 2 - ammo_width / 2, y])

    # créer un ennemi si le temps minimum entre les apparitions est écoulé
    maintenant = pygame.time.get_ticks()
    if maintenant - derniere_apparition > temps_entre_ennemis:
        derniere_apparition = maintenant
        ennemis.append([random.randint(0, display_width - enemy_width), 0])

    # Remplir la fenêtre avec une couleur
    fenetre.fill((0, 0, 0))
    
    # afficher le vaisseau
    fenetre.blit(carImg, (x, y))
    

    # afficher les balles
    for balle in balles:
        balle[1] -= ammo_speed
        fenetre.blit(ammoImg, (balle[0], balle[1]))
        # supprimer la balle si elle sort de l'écran
        if balle[1] < 0:
            balles.remove(balle)
            
    for ennemi in ennemis:
        if ennemi[0] + enemy_width > x and ennemi[0] < x + car_width and ennemi[1] + enemy_height > y and ennemi[1] < y + car_width or ennemi[1] + enemy_height > display_height:
            vie -= 1
            ennemis.remove(ennemi)
            if(vie == 0):
                continuer = False
                print("Game Over")
                print("Score : ", score)
                print("Vie : ", vie)

    # afficher les ennemis
    for ennemi in ennemis:
        ennemi[1] += enemy_speed
        fenetre.blit(VaisseauEnnemiImg, (ennemi[0], ennemi[1]))
        # supprimer l'ennemi si il sort de l'écran
        if ennemi[1] > display_height:
            ennemis.remove(ennemi)
        # supprimer l'ennemi si il est touché par une balle
        for balle in balles:
            if balle[0] + ammo_width > ennemi[0] and balle[0] < ennemi[0] + enemy_width and balle[1] + ammo_height > ennemi[1] and balle[1] < ennemi[1] + enemy_height:
                ennemis.remove(ennemi)
                balles.remove(balle)
                score += 10
                
    #evolution du temps d'apparition des ennemis
    if(score > 300):
        temps_entre_ennemis = 700
        
        
        
            
    # mettre à jour l'affichage
    pygame.display.flip()
    
pygame.quit()