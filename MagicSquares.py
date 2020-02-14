from functools import reduce
import random
import pygame, random
from pygame.locals import *

class Magic_squares:
    def __init__(self):
        self.string = lambda n: str(n)                                                                                                                      #1
        self.separar = lambda n: [int(i) for i in self.string(n)]                                                                                           #2
        self.juntar = lambda l: reduce(self.somar, [str(i) for i in l])                                                                                     #3
        self.somar = lambda x, y: x + y
        self.somarDigitos = lambda n: reduce(self.somar, self.separar(n))                                                                                   #4

        self.complemento = lambda k, v: [i if self.somarDigitos(int(self.juntar([k, i]))) == v else -1 for i in range(0, 16)]                               #5
        self.encontrar_complemento = lambda v, k: list(filter(lambda i: i != -1, self.complemento(k, v)))                                                   #6

        self.index_central = lambda m: int((len(m) - 1)/2 + 1 - 1)                                                                                          #7
        self.cruz_matriz = lambda m: [[m[self.index_central(m)][i] for i in range(len(m))], [m[i][self.index_central(m)] for i in range(len(m))]]           #8
        self.x_matriz = lambda m: [[m[i][i] for i in range(len(m))], [m[i][self.encontrar_complemento(8, i)[0]] for i in range(len(m))]]                    #9

        self.showSquare = lambda m: [print(i) for i in m]                                                                                                   #10
        self.somaLinhas = lambda m: [sum(i) for i in m]                                                                                                     #11
        self.somaX = lambda m: [sum(self.x_matriz(m)[0]), sum(self.x_matriz(m)[1])]                                                                         #12
        self.somaColunas = lambda m: [sum([m[i][0] for i in range(len(m))]) for k in range(len(m))]                                                         #13
        self.comparador = lambda m: [self.somaX(m), self.somaLinhas(m), self.somaColunas(self.magic)]                                                       #14
        self.validar = lambda m: [True if sum(i) == len(i) * i[0] else False for i in m]                                                                    #15
        self.criar_magic = lambda len: [[0,0,0,0,0,0,0,0,0] for i in range(int(len**(1/2)))]                                                                #16
        self.magic = self.criar_magic(81)                                                                                                                   #17
        self.padrao = [0, 0, 0, 0, 0, 0, 0, 0, 0]                                                                                                           #18

    #19
    def buildPattern(self, pattern):
        self.padrao = pattern
        self.magic[self.index_central(self.magic)] = self.padrao

        for i in range(len(self.magic)):
            self.magic[i][self.index_central(self.magic)] = self.padrao[i]

        #---------------------------------------------------------------------------- Cruz x

        for i in range(self.index_central(self.magic) + 1, len(self.magic)):
            self.magic[0][i] = self.padrao[i - self.index_central(self.magic)]

        for i in range(0, self.index_central(self.magic)):
            self.magic[0][i] = self.padrao[i + self.index_central(self.magic) + 1]

        #---------------------------------------------------------------------------- cruz y

        for i in range(self.index_central(self.magic) + 1, len(self.magic)):
            self.magic[-1][i] = self.padrao[i - self.index_central(self.magic) - 1]

        for i in range(0, self.index_central(self.magic)):
            self.magic[-1][i] = self.padrao[i - self.index_central(self.magic) - 1]

        #------------------------------------------------------------------------------------------------------------ Diagonal direita-esquerda

        for i in range(1, len(self.magic)):
            self.magic[i][self.encontrar_complemento(8, i)[0]] = self.magic[0][8]

        #----------------------------------------------------------------------------
        for i in range(1, len(self.magic) -1):
            self.magic[i][self.encontrar_complemento(7, i)[0]] = self.magic[0][7]

        #----------------------------------------------------------------------------
        for i in range(1, len(self.magic) -2):
            self.magic[i][self.encontrar_complemento(6, i)[0]] = self.magic[0][6]

        #----------------------------------------------------------------------------
        for i in range(1, len(self.magic) -3):
            self.magic[i][self.encontrar_complemento(5, i)[0]] =self.magic[0][5]

        #----------------------------------------------------------------------------
        for i in range(1, len(self.magic) -4):
            self.magic[i][self.encontrar_complemento(4, i)[0]] = self.magic[0][4]

        #----------------------------------------------------------------------------
        for i in range(1, len(self.magic) -5):
            self.magic[i][self.encontrar_complemento(3, i)[0]] = self.magic[0][3]

        #----------------------------------------------------------------------------
        for i in range(1, len(self.magic) -6):
            self.magic[i][self.encontrar_complemento(2, i)[0]] = self.magic[0][2]

        #----------------------------------------------------------------------------
        for i in range(1, len(self.magic) -7):
            self.magic[i][self.encontrar_complemento(1, i)[0]] = self.magic[0][1]

        #------------------------------------------------------------------------------------------------------------ Diagonal esquerda direita

        for i in range(1, len(self.magic)):
            self.magic[self.encontrar_complemento(9, i)[0]][i] = self.magic[8][1]

        #----------------------------------------------------------------------------
        for i in range(2, len(self.magic)):
            self.magic[self.encontrar_complemento(10, i)[0]][i] = self.magic[8][2]

        #----------------------------------------------------------------------------
        for i in range(3, len(self.magic)):
            self.magic[self.encontrar_complemento(11, i)[0]][i] = self.magic[8][3]

        #----------------------------------------------------------------------------
        for i in range(4, len(self.magic)):
            self.magic[self.encontrar_complemento(12, i)[0]][i] = self.magic[8][4]

        #----------------------------------------------------------------------------
        for i in range(5, len(self.magic)):
            self.magic[self.encontrar_complemento(13, i)[0]][i] = self.magic[8][5]

        #----------------------------------------------------------------------------
        for i in range(6, len(self.magic)):
            self.magic[self.encontrar_complemento(14, i)[0]][i] = self.magic[8][6]

        #----------------------------------------------------------------------------
        for i in range(7, len(self.magic)):
            self.magic[self.encontrar_complemento(15, i)[0]][i] = self.magic[8][7]

    #20
    def Random_square(self, nums):
        square = []
        initial_pattern = nums

        for i in range(len(self.magic)):
            square.append([])

        for i in square:
            for k in range(len(self.magic)):
                i.append(0)

        nums.sort()

        for i in range(0, len(self.magic)):
            for k in range(0, len(self.magic)):
                if self.magic[i][k] == 1:
                    square[i][k] = int(nums[0])
                    continue
                if self.magic[i][k] == 2:
                    square[i][k] = int(nums[1])
                    continue
                if self.magic[i][k] == 3:
                    square[i][k] = int(nums[2])
                    continue
                if self.magic[i][k] == 4:
                    square[i][k] = int(nums[3])
                    continue
                if self.magic[i][k] == 5:
                    square[i][k] = int(nums[4])
                    continue
                if self.magic[i][k] == 6:
                    square[i][k] = int(nums[5])
                    continue
                if self.magic[i][k] == 7:
                    square[i][k] = int(nums[6])
                    continue
                if self.magic[i][k] == 8:
                    square[i][k] = int(nums[7])
                    continue
                if self.magic[i][k] == 9:
                    square[i][k] = int(nums[8])
                    continue

        return [square, initial_pattern]

    #21
    def generateNums(self):
        pattern = [1,6,2,7,3,8,4,9,5]
        new_pattern = [0,0,0,0,0,0,0,0,0]

        n = random.randint(1,50)
        nums = [i * n for i in pattern]

        for k in range(len(nums)):
            for i in range(len(pattern)):
                if self.somarDigitos(self.somarDigitos(self.somarDigitos((nums[i])))) == pattern[k]:
                    new_pattern[k] = nums[i]

        return new_pattern

    #22
    def render(self, magic):
        screen = pygame.display.set_mode((595, 595))
        font = pygame.font.Font('freesansbold.ttf', 18)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        screen.fill((0, 0, 0))

        for x in range(0, 595, 66):                                         # Draw vertical lines
            pygame.draw.line(screen, (148, 189, 177), (x, 0), (x, 594))
        for y in range(0, 595, 66):                                         # Draw horizontal lines
            pygame.draw.line(screen, (148, 189, 177), (0, y), (594, y))

        passo = 66
        pos = -45

        n = [3.5 + (2.55 * i) for i in range(-1, 9)]
        n[0] = 1

        # Render all numers of magic
        for k in range(9):
            pos = -45
            for i in range(9):
                nums_font = font.render(str(magic[k][i]), True, (255, 255, 255))
                num_rect = nums_font.get_rect()
                pos += passo
                num_rect.topleft = (pos, n[k] * 26)
                screen.blit(nums_font, num_rect)





