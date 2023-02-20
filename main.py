import pygame
pygame.init()

display_width = 800
display_height = 600

car_width = 73
carImg = pygame.image.load('assets/mainV.png')

fenetre = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Mon jeu de vaisseau')

clock = pygame.time.Clock()

def car(x,y):
    fenetre.blit(carImg, (x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0

# boucle d'événements pour garder la fenêtre ouverte
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    
    x += x_change

    fenetre.fill((0, 0, 0))

    car(x,y)

    pygame.display.update()

    clock.tick(60)

pygame.quit()