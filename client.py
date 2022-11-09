import pygame
from network import Network
from player import Player

width = 800
height = 640

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Client")

def redrawWindow(win, p1, p2):
    win.fill((61,176,247))
    p1.draw(win)
    p2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    a = n.getP()
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        b = n.send(a)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        a.move()
        redrawWindow(win, a, b)

main()