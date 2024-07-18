import pygame, sys 
class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./graphics/cat_ship.png').convert_alpha()
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH /2, WINDOW_HEIGHT / 2))
    

# game setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode(( WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Kitty Astroid")
clock = pygame.time.Clock()

#sprite groups
spaceship_group = pygame.sprite.Group()

# sprite creation
ship = Ship(spaceship_group)


# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #delta time
    dt = clock.tick() / 1000

    #graphics
    spaceship_group.draw(display_surface)

    pygame.display.update()