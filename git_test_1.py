import pygame


colors = ['#0000ff', '#ff0000', '#00ff00']


def draw(screen, wid, count):
    screen.fill((0, 0, 0))
    center = wid * count, wid * count
    while count > 0:
        pygame.draw.circle(screen, colors[count % 3], center, wid * count)
        count -= 1


def main(wid, count):
    pygame.init()
    pygame.display.set_caption('Мишень')

    size = wid * count * 2, wid * count * 2
    screen = pygame.display.set_mode(size)

    draw(screen, wid, count)
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()


try:
    wid, count = map(int, input().split())
    main(wid, count)
except:
    print('Неправильный формат ввода')
