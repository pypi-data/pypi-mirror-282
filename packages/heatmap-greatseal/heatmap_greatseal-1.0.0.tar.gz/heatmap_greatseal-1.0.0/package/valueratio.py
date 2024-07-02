import matplotlib.pyplot as plt
import numpy as np
import math

def generate(h, w, min, max):
    return np.random.uniform(min, max, size=(h,w)).tolist()

def add(m1, m2):
    if not m1 or not m2 or np.array(m1).shape != np.array(m2).shape:
        return False
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] += m2[i][j]
    return m1

def substract(m1, m2):
    if not m1 or not m2 or np.array(m1).shape != np.array(m2).shape:
         return False
    result = [[0 for _ in range(len(m1[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j] = m2[i][j] - m1[i][j]
    return result

def multiply(m1, m2):
    if not m1 or not m2 or np.array(m1).shape != np.array(m2).shape:
        return
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] *= m2[i][j]
    return m1

def rotate(matrix, degree):
    radians = math.radians(degree)

    rows = len(matrix)
    cols = len(matrix[0])

    center_x = (cols - 1) / 2.0
    center_y = (rows - 1) / 2.0

    rotated_matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            new_x = (j - center_x) * math.cos(radians) - (i - center_y) * math.sin(radians) + center_x
            new_y = (j - center_x) * math.sin(radians) + (i - center_y) * math.cos(radians) + center_y
            
            new_i = round(new_y)
            new_j = round(new_x)

            if 0 <= new_i < rows and 0 <= new_j < cols:
                rotated_matrix[new_i][new_j] = matrix[i][j]

    return rotated_matrix

def eigenvalue(matrix):
    if not matrix:
        return

    return np.linalg.eigvals(matrix)

def n_percent(matrix):
    heatmap = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            ns = neighbours(matrix, row, col)
            ratio = 0
            for n in ns:
                if matrix[row][col] > n:
                    ratio += 1
            heatmap.append((row,col,round(ratio/len(ns), 5)))
    return heatmap

def neighbours(matrix, r, c):
    if not matrix or r > len(matrix) or c > len(matrix[0]):
        return []
    
    n, offset = [], [-1,0,1]
    rows, cols = len(matrix), len(matrix[0])
    for i in offset:
        for j in offset:
            if (i != 0 or j != 0) and -1 < i+r < rows and -1 < j+c < cols:
                n.append(matrix[i+r][j+c])
    return n

def grid_visualize(matrix):
    data = n_percent(matrix)
    rows = max(d[0] for d in data) + 1
    cols = max(d[1] for d in data) + 1
    map = np.zeros((rows,cols))

    for r,c,value in data:
        map[r][c] = value

    plt.matshow(map,None)
    plt.colorbar(label='Value')
    plt.xticks(np.arange(cols), np.arange(cols))
    plt.yticks(np.arange(rows), np.arange(rows))
    plt.xlabel('Column')
    plt.ylabel('Row')
    plt.title('Heatmap of Value Ratio of Neighbours')
    plt.grid(True)

    plt.show()

def gaussian_visualize(matrix):
    data = n_percent(matrix)
    rows = max(d[0] for d in data) + 1
    cols = max(d[1] for d in data) + 1
    map = np.zeros((rows,cols))

    for r,c,value in data:
        map[r][c] = value

    plt.figure(figsize=(rows+5,cols+5))
    plt.imshow(map,cmap='plasma', interpolation='gaussian')
    plt.colorbar(label='Value')

    plt.xticks(np.arange(cols), np.arange(cols))
    plt.yticks(np.arange(rows), np.arange(rows))
    plt.xlabel('Column')
    plt.ylabel('Row')
    plt.title('Heatmap of Value Ratio of Neighbours')
    plt.grid(True)

    plt.show()

def distribution(matrix):
    data = n_percent(matrix)
    rows = max(d[0] for d in data) + 1
    cols = max(d[1] for d in data) + 1
    map = np.zeros((rows,cols))

    for r,c,value in data:
        map[r][c] = value

    flattened = map.flatten()
    sorted = np.sort(flattened)
    plt.hist(sorted, bins=10)
    plt.show()