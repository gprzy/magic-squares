# Magic Squares
An algorithm that generate symmetric and random magic squares.

## Whats is a Magic Square?
A magic square is a special square that is completely **symmetrical**. The sum of any column generates a **constant number**, that is simultaneously the sum of any line or diagonal of this square.

## Generating a square
1. Open terminal and run:
    ```
    pip install requirements.txt
    ```
2. Finally, run:
    ```powershell
    python main.py
    ```

    Example of output
    ``` 
    Padrão: [300, 100, 350, 150, 400, 200, 450, 250, 50]

    [[ 50 300 100 350 150 400 200 450 250]
    [300 100 350 150 400 200 450 250  50]
    [100 350 150 400 200 450 250  50 300]
    [350 150 400 200 450 250  50 300 100]
    [150 400 200 450 250  50 300 100 350]
    [400 200 450 250  50 300 100 350 150]
    [200 450 250  50 300 100 350 150 400]
    [450 250  50 300 100 350 150 400 200]
    [250  50 300 100 350 150 400 200 450]]

    Número mágico: 2250
    ```

## Base square
Every Magic Square of this module is generated based on a common primitive square, shown below:
```
Padrão: [3, 8, 4, 9, 5, 1, 6, 2, 7]

[[1 6 2 7 3 8 4 9 5] 
 [6 2 7 3 8 4 9 5 1] 
 [2 7 3 8 4 9 5 1 6] 
 [7 3 8 4 9 5 1 6 2] 
 [3 8 4 9 5 1 6 2 7] 
 [8 4 9 5 1 6 2 7 3] 
 [4 9 5 1 6 2 7 3 8] 
 [9 5 1 6 2 7 3 8 4] 
 [5 1 6 2 7 3 8 4 9]]

Número mágico: 45
```