import pygame
import math
from model import guess
import ctypes

pygame.init()

sz = 18
dim = 28
w = h = dim * sz
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Draw")

run = True

boxes = []


def valid(i, j):
    return -1 < i < dim and -1 < j < dim


class Box(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 0
        self.value = 0
        self.im = 0.5
        self.dir = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if valid(x + i, y + j):
                    self.dir += [x + i, y + j],

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def draw(self):
        pygame.draw.rect(screen, [self.color, self.color, self.color],
                         (self.x * sz, self.y * sz, sz, sz))

    def ink(self, c=0.9, ng=0):
        self.value += c
        self.color = math.ceil(255 * self.sigmoid(self.value))
        if ng == 0:
            # print(c*self.im)
            for i, j in self.dir:
                ngb = boxes[i][j]
                ngb.ink(c * self.im, 1)

    def deink(self):
        self.value -= 1
        self.color = round(255 * self.sigmoid(self.value))


def draw():
    screen.fill(255)
    for boxset in boxes:
        for box in boxset:
            box.draw()
    pygame.display.update()


def reset():
    for i in range(dim):
        for j in range(dim):
            boxes[i][j].color = 0


for i in range(dim):
    boxes.append([])
    for j in range(dim):
        boxes[i].append(Box(i, j))


def fun():
    num = []
    for i in range(dim):
        num += [],
        for j in range(dim):
            num[i] += boxes[i][j].color,

    p = guess(num)
    ctypes.windll.user32.MessageBoxW(0, "Guess : " + p, "Prediction", 0)


pen = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    x, y = pygame.mouse.get_pos()
    x //= sz
    y //= sz

    if pygame.mouse.get_pressed()[0]:
        if pen:
            boxes[x][y].deink()
        else:
            boxes[x][y].ink()

    if keys[pygame.K_BACKSPACE]:
        reset()
    elif keys[pygame.K_LSHIFT]:
        pen = 1
    elif keys[pygame.K_TAB]:
        pen = 0
    elif keys[pygame.K_SPACE]:
        fun()
        reset()

    draw()


pygame.QUIT
