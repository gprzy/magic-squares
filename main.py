from MagicSquares import Magic_squares
import pygame, random
from pygame.locals import *

s = Magic_squares()
pygame.init()
pygame.display.set_caption('Magic Squares')
i = 1

while True:
    magic = s.buildPattern([3, 8, 4, 9, 5, 1, 6, 2, 7])
    new_pattern = s.generateNums()
    square = s.Random_square(new_pattern)[0]

    if s.validar(s.comparador(square))[0] and s.validar(s.comparador(square))[1] and s.validar(s.comparador(square))[2]:
        print(f"Quadrado: {i}")
        print(f"Padrão: {square[1]}")
        print(f"Número mágico: {sum(new_pattern)}\n")

        s.render(square)
        pygame.display.update()
        pygame.time.wait(50000)
        i += 1
    else:
        continue
