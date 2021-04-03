#RPS sim
from random import *
import math
WIDTH = 700
HEIGHT = 800
#every bug check all mentions of scissors
rocks = []
papers = []
scissors = []
quantity = 5

def draw():
    screen.clear()
    screen.fill('#aaccff')
    for rock in rocks:
        rock.draw()

    for paper in papers:
        paper.draw()

    for scissor in scissors:
        scissor.draw()

def update():
    for rock in rocks:
        win = 99999999999
        winner = ''
        for scissor in scissors:
            a = dis(rock,scissor)
            r = angle(rock,scissor)
            if a < win:
                win = a
                winner = scissor
                rock.rad = r
        move(rock, 1)
        for paper in papers:
            if rock.colliderect(paper):
                rock.image = 'paper'
                rocks.remove(rock)
                papers.append(rock)
                break

    for paper in papers:
        for scissor in scissors:
            if paper.colliderect(scissor):
                paper.image = 'scissor'
                papers.remove(paper)
                scissors.append(paper)
                break
    for scissor in scissors:
        for rock in rocks:
            if scissor.colliderect(rock):
                scissor.image = 'dwayne'
                scissors.remove(scissor)
                rocks.append(scissor)
                break

'''
def move_forward(self, dist):
    angle = math.radians(self.angle)
    dx = dist * math.cos(angle)
    dy = dist * math.sin(angle)
    self.x += dx
    self.y -= dy
'''
def dis(actor1,actor2):
    a = actor1.x - actor2.x
    b = actor1.y - actor2.y

    c = (a**2+b**2)**.5
    return c
'''
def ratio(actor1,actor2):
    a = actor1.x - actor2.x
    b = actor1.y - actor2.y
    if abs(b) < 1:
        b = 1
    c = a/b
    return c
'''
def move(actor, dist):
    angle = actor.rad
    x = dist * math.cos(angle)
    y = dist * math.sin(angle)
    actor.x += x
    actor.y -= y

# 0 degrees equals up -y axis
def angle(actor1,actor2):
    adj = actor1.x - actor2.x
    op = actor1.y - actor2.y
    if adj == 0:
        if op < 0:
            rad = math.pi
        if op >= 0:
            rad = 0
    else:
        rad = math.atan(op/adj)
        if adj < 0:
            rad += math.pi
    print(rad)
    return rad



def start():
    for i in range(quantity):
        rock = Actor('dwayne',(randint(10,WIDTH-10),randint(10,HEIGHT-10)))
        paper = Actor('paper',(randint(10,WIDTH-10),randint(10,HEIGHT-10)))
        scissor = Actor('scissor',(randint(10,WIDTH-10),randint(10,HEIGHT-10)))
        rocks.append(rock)
        papers.append(paper)
        scissors.append(scissor)

start()