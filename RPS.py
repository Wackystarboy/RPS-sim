#RPS sim
from random import *
WIDTH = 600
HEIGHT = 800
#every bug check all mentions of scissors
rocks = []
papers = []
scissors = []
quantity = 20

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
        win = 999
        winner = ''
        for scissor in scissors:
            a = dis(rock,scissor)
            if a < win:
                win = a
                winner = scissor
        rock.
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

def dis(actor1,actor2):
    a = actor1.x - actor2.x
    b = actor1.y - actor2.y

    c = (a**2+b**2)**.5
    return c
def ratio(actor1,actor2):
    a = actor1.x - actor2.x
    b = actor1.y - actor2.y

    c = a/b
    return c
#finish the ratio x = c y = 1

def start():
    for i in range(quantity):
        rock = Actor('dwayne',(randint(10,WIDTH-10),randint(10,HEIGHT-10)))
        paper = Actor('paper',(randint(10,WIDTH-10),randint(10,HEIGHT-10)))
        scissor = Actor('scissor',(randint(10,WIDTH-10),randint(10,HEIGHT-10)))
        rocks.append(rock)
        papers.append(paper)
        scissors.append(scissor)

start()