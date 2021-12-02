import pygame
#import random


def draw(screen, wid, side):
    screen.fill('#ffffff')
    size = wid // side
    for i in range(side):
        for j in range(side):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, '#000000',
                                 (i * size, wid - (j + 1) * size, size, size))


def main(wid, side):
    pygame.init()
    pygame.display.set_caption('Шахматная клетка')

    size = wid, wid
    screen = pygame.display.set_mode(size)

    draw(screen, wid, side)
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()


try:
    wid, side = map(int, input().split())
    assert wid % side == 0
    main(wid, side)
except:
    print('Неправильный формат ввода')
