import pygame
import pygame._sdl2 as pg_sdl2  # noqa

pygame.init()
screen = pygame.display.set_mode()

FPS = 60
clock = pygame.Clock() #게임의 FPS

window = pg_sdl2.Window.from_display_module()
window.maximize()

running = True
while running:
    clock.tick(FPS)
    screen.fill("black")

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()