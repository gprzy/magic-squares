import numpy as np
from msquares import MagicSquare

if __name__ == "__main__":
    s = MagicSquare()

    magic = s.build_pattern([3, 8, 4, 9, 5, 1, 6, 2, 7])
    new_pattern = s.generate_nums()
    square = s.random_square(new_pattern)[0]

    if s.validar(s.comparador(square))[0] and \
       s.validar(s.comparador(square))[1] and \
       s.validar(s.comparador(square))[2]:

        print(f"Padrão: {square[1]}\n")
        print(f'{np.array(square)}\n')
        print(f"Número mágico: {sum(new_pattern)}\n")