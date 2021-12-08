import pygame
#import random


def draw(screen, wid, hue):
    screen.fill('#000000')
    if wid == 0:
        return
    side = wid // 4
    color = pygame.Color(0, 0, 0)
    #
    color.hsva = (hue, 100, 100)
    top = [(150 - 3 * side, 150 - side),
           (150 - side, 150 - 3 * side),
           (149 + 3 * side, 150 - 3 * side),
           (149 + side, 150 - side)]
    pygame.draw.polygon(screen, color, top)
    #
    color.hsva = (hue, 100, 50)
    #right = [(150 - 3 * side, 150 - side),
    #       (150 - side, 150 - 3 * side),
    #       (149 + 3 * side, 150 - 3 * side),
    #       (149 + side, 150 - side)]
    #pygame.draw.polygon(screen, color, top)


def main(wid, hue):
    pygame.init()
    pygame.display.set_caption('Шахматная клетка')

    screen = pygame.display.set_mode((300, 300))

    draw(screen, wid, hue)


    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


try:
    wid, hue = map(int, input().split())
    assert wid % 4 == 0 and wid <= 100
    assert 0 <= hue <= 360
    main(wid, hue)
except AssertionError:
    print('Неправильный формат ввода')
