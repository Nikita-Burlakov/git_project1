import pygame
#import random


def draw(screen, wid, height):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, '#ff0000', (1, 1, wid - 2, height - 2))


def main(wid, height):
    pygame.init()
    pygame.display.set_caption('Прямоугольник')

    size = wid, height
    screen = pygame.display.set_mode(size)

    draw(screen, wid, height)
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()


try:
    w, h = map(int, input().split())
    main(w, h)
except:
    print('Неправильный формат ввода')
