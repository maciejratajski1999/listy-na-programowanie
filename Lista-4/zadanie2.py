from random import randint
import matplotlib.pyplot as plt
from matplotlib import colors
import os
from PIL import Image
from datetime import datetime
import numpy as np

def jump(pos):
    x_y = randint(-1, 1), randint(-1, 1)
    if x_y == (0, 0):
        return jump(pos)
    new_pos = pos[0] + x_y[0], pos[1] + x_y[1]

    if new_pos[0] not in range(1, 21):
        if new_pos[0] > 20:
            new_pos = pos[0] + x_y[0] - 20,  pos[1] + x_y[1]
        if new_pos[0] < 1:
            new_pos = pos[0] + x_y[0] + 20, pos[1] + x_y[1]

    if new_pos[1] not in range(1, 21):
        if new_pos[1] > 20:
            new_pos = pos[0] + x_y[0], pos[1] + x_y[1] - 20
        if new_pos[1] < 1:
            new_pos = pos[0] + x_y[0], pos[1] + x_y[1] + 20

    return new_pos

def generate_image(pos, i, grid):
    grid[pos[0] - 1][pos[1] - 1] = 1
    cmap = colors.ListedColormap(['white', 'red'])
    plt.figure(figsize=(10, 10))
    plt.pcolor(grid[::-1], cmap=cmap, edgecolors='black', linewidths=5)
    plt.xticks(np.arange(1, 20.1, step=1))
    plt.yticks(np.arange(1, 20.1, step=1))
    plt.savefig('temporary_images//' + str(i))
    grid[pos[0] - 1][pos[1] - 1] = 0

def generate_gif(dir):
    files_indexes = []
    for (direc, subdirs, files) in os.walk(dir):
        for file in files:
            dot_index = file.find(".")
            file_index = int(file[:dot_index])
            files_indexes.append(file_index)
    files_indexes.sort()
    frames = []
    for index in files_indexes:
        file =  str(index) + ".png"
        new_frame = Image.open(os.path.join(dir, file))
        frames.append(new_frame)

    time_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    frames[0].save('agents_path' + time_now + '.gif', format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=100, loop=0)

    for (direc, subdirs, files) in os.walk(dir):
        for file in files:
            os.remove(os.path.join(dir, file))
    os.rmdir(dir)


def generate_path(n):
    pos = 10, 10
    grid = np.zeros(400).reshape(20,20)
    os.mkdir('temporary_images')

    for i in range(0, n):
        pos = jump(pos)
        generate_image(pos, i, grid)

    generate_gif('temporary_images')


generate_path(100)