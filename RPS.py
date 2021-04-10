#RPS sim
from random import *
import math
WIDTH = 700
HEIGHT = 800
#every bug check all mentions of scissors
#finish spacebar cooldown
#Win count ROCKS FOR THE WIN
rocks = []
papers = []
scissors = []
quantity = 20
speed = 1
loading = True
rwin=0
pwin=0
swin=0
cooldown=False
def draw():
    screen.clear()
    screen.fill('#aaccff')
    if loading:
        screen.draw.text('Quantity: '+ str(quantity),(100,100), color = '#000000', fontsize = 48)
        screen.draw.text('Speed: '+ str(int(speed*200)) + '%',(100,150), color = '#000000', fontsize = 48)
        screen.blit('dwayne',(100,197))
        screen.draw.text('Rock wins: '+ str(rwin),(130,200), color = '#000000', fontsize = 48)
        screen.blit('paper',(100,247))
        screen.draw.text('Paper wins: '+ str(pwin),(130,250), color = '#000000', fontsize = 48)
        screen.blit('scissor',(100,297))
        screen.draw.text('Scissors wins: '+ str(swin),(130,300), color = '#000000', fontsize = 48)
        screen.draw.text('Press space to start',(250,700), color = '#000000', fontsize = 30)
    else:
        for rock in rocks:
            rock.draw()

        for paper in papers:
            paper.draw()

        for scissor in scissors:
            scissor.draw()

def update():
    global rocks,papers,scissors,loading
    if keyboard.space and not loading:
        rocks = []
        papers = []
        scissors = []
        loading = True
        return
    if keyboard.space and loading:
        loading=False
        start()

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
        if len(scissors) != 0:
            move(rock, speed, rock.x > winner.x)
        else:
            rndmove(rock, speed)
        for paper in papers:
            if rock.colliderect(paper):
                rock.image = 'paper'
                rocks.remove(rock)
                papers.append(rock)
                break

    for paper in papers:
        win = 99999999999
        winner = ''
        for rock in rocks:
            a = dis(paper,rock)
            r = angle(paper,rock)
            if a < win:
                win = a
                winner = rock
                paper.rad = r
        if len(rocks) != 0:
            move(paper, speed, paper.x > winner.x)
        else:
            rndmove(paper, speed)
        for scissor in scissors:
            if paper.colliderect(scissor):
                paper.image = 'scissor'
                papers.remove(paper)
                scissors.append(paper)
                break
#paper = scissor rock = paper
    for scissor in scissors:
        win = 99999999999
        winner = ''
        for paper in papers:
            a = dis(scissor,paper)
            r = angle(scissor,paper)
            if a < win:
                win = a
                winner = paper
                scissor.rad = r
        if len(papers) != 0:
            move(scissor, speed, scissor.x > winner.x)
        else:
            rndmove(scissor, speed)
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
def move(actor, dist, move_left):
    angle = actor.rad
    x = dist * math.cos(angle)
    y = dist * math.sin(angle)
    if move_left:
        x = -x
        y= -y
    actor.x += x
    actor.y -= y

# 0 degrees equals up -y axis
def angle(actor1,actor2):
    adj = actor1.x - actor2.x
    op = -(actor1.y - actor2.y)
    if adj == 0:
        if op < 0:
            rad = math.pi
        if op >= 0:
            rad = 0
    else:
        rad = math.atan(op/adj)

    return rad

def rndmove(actor, dist):
    angle = randint(0,360)
    angle = math.radians(angle)
    x = dist * math.cos(angle)
    y = dist * math.sin(angle)
    actor.x += x
    actor.y -= y

def cooldowned():
    global cooldown
    cooldown = False

def start():
    for i in range(quantity):
        rock = Actor('dwayne',(randint(10,WIDTH-10),randint(10,HEIGHT-10)))
        paper = Actor('paper',(randint(10,WIDTH-10),randint(10,HEIGHT-10)))
        scissor = Actor('scissor',(randint(10,WIDTH-10),randint(10,HEIGHT-10)))
        rocks.append(rock)
        papers.append(paper)
        scissors.append(scissor)

start()