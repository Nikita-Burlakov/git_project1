import pygame
#import random


def draw(screen, wid, height):
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 0),
                     (wid - 1, height - 1), width=5)
    pygame.draw.line(screen, (255, 255, 255), (wid - 1, 0),
                     (0, height - 1), width=5)


def main(wid, height):
    pygame.init()
    pygame.display.set_caption('Крест')

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
