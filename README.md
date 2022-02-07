# Magic Squares

## What is a magic square?

<img src="https://github.com/gprzy/magic-squares/blob/master/assets/magic-square.jpg" width="25%" height="25%"/>

Is a special type of numeric square, being completely **symmetrical**. The sum of any column generates a **constant number**, that is simultaneously the sum of any line or diagonal of the square.

## 🚀 Running with docker container

1\) Building python docker image:

```powershell
docker build -t python-image .
```

2\) Running the built image:

```powershell
docker run -d -i --name python-env python-image bash
```

3.1\) Accessing bash from container:

```powershell
docker exec -it python-env bin/bash
```

3.2\) In case of errors with the above command, use:

```powershell
docker exec -it python-env sh
```

4\) Run the code:

```bash
python3 main.py
```

## Example of output

```prolog
Pattern: [300, 100, 350, 150, 400, 200, 450, 250, 50]

[[ 50 300 100 350 150 400 200 450 250]
 [300 100 350 150 400 200 450 250  50]
 [100 350 150 400 200 450 250  50 300]
 [350 150 400 200 450 250  50 300 100]
 [150 400 200 450 250  50 300 100 350]
 [400 200 450 250  50 300 100 350 150]
 [200 450 250  50 300 100 350 150 400]
 [450 250  50 300 100 350 150 400 200]
 [250  50 300 100 350 150 400 200 450]]

Magic number: 2250
```

## Base square
Every magic square is generated based on a common primitive square, shown below:

```haskell
Pattern: [3, 8, 4, 9, 5, 1, 6, 2, 7]

[[1 6 2 7 3 8 4 9 5] 
 [6 2 7 3 8 4 9 5 1] 
 [2 7 3 8 4 9 5 1 6] 
 [7 3 8 4 9 5 1 6 2] 
 [3 8 4 9 5 1 6 2 7] 
 [8 4 9 5 1 6 2 7 3] 
 [4 9 5 1 6 2 7 3 8] 
 [9 5 1 6 2 7 3 8 4] 
 [5 1 6 2 7 3 8 4 9]]

Magic number: 45
```
