import pygame

# Inicializace pygame
pygame.init()

# Vytvořeni obrazovky
width = 600
height = 300
screen = pygame.display.set_mode((width, height))

player = pygame.Rect((250, 250, 50, 50))


# Hlavni herni cyklus
lets_continue = True 


while lets_continue: 
    screen.fill((0, 0 ,0))
    pygame.draw.rect(screen, (138, 43, 226), player)

    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        player.move_ip(0, -1)

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            lets_continue = False
    pygame.display.update()
# Ukončeni pygame
pygame.quit()