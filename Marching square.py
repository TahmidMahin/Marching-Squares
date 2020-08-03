import pygame as pg
from opensimplex import OpenSimplex

pg.init()

black = (0, 0, 0)
white = (255, 255, 255)

width = 1000
height = 800

screen = pg.display.set_mode((width, height))

pg.display.set_caption("Marching Squares")

distance = 20
block_probability = 0.5
noise = OpenSimplex()
nodes = []

class node:
	def __init__(self, x, y, p):
		self.x = x
		self.y = y
		self.r = 2
		self.p = (p+1)/2
		self.center = (x, y)
		if self.p >= block_probability:
			self.color = (round(p*255),)*3
		else:
			self.color = black
	def show_node(self):
		pg.draw.circle(screen, self.color, self.center, self.r)

def make_nodes(t):
	for j in range(0, height, distance):
		row = []
		for i in range(0, width, distance):
			row.append(node(i, j, noise.noise3d(i, j, t)))
		nodes.append(row)

def show_nodes():
	for row in nodes:
		for node in row:
			node.show_node()

def make_line(a, b, c, d, condition):
	if condition == 1:
		pg.draw.line(screen, white, a, d)
	elif condition == 2:
		pg.draw.line(screen, white, a, b)
	elif condition == 3:
		pg.draw.line(screen, white, b, d)
	elif condition == 4:
		pg.draw.line(screen, white, c, d)
	elif condition == 5:
		pg.draw.line(screen, white, a, c)
	elif condition == 6:
		pg.draw.line(screen, white, a, d)
		pg.draw.line(screen, white, b, c)
	elif condition == 7:
		pg.draw.line(screen, white, b, c)
	elif condition == 8:
		pg.draw.line(screen, white, b, c)
	elif condition == 9:
		pg.draw.line(screen, white, a, b)
		pg.draw.line(screen, white, c, d)
	elif condition == 10:
		pg.draw.line(screen, white, a, c)
	elif condition == 11:
		pg.draw.line(screen, white, c, d)
	elif condition == 12:
		pg.draw.line(screen, white, b, d)
	elif condition == 13:
		pg.draw.line(screen, white, a, b)
	elif condition == 14:
		pg.draw.line(screen, white, a, d)

def show_contour():
	for i in range(len(nodes)-1):
		for j in range(len(nodes[0])-1):
			x = nodes[i][j].x
			y = nodes[i][j].y
			a = (x + distance//2, y)
			b = (x + distance, y + distance//2)
			c = (x + distance//2, y + distance)
			d = (x, y + distance//2)
			bin_string = ""
			bin_string += "0" if nodes[i+1][j+1].color == black else "1"
			bin_string += "0" if nodes[i+1][j].color == black else "1"
			bin_string += "0" if nodes[i][j+1].color == black else "1"
			bin_string += "0" if nodes[i][j].color == black else "1"
			make_line(a, b, c, d, int(bin_string, 2))

def initialize():
	running = True
	time = -10000
	while running:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False
		screen.fill(black)
		if time%5 == 0 :
			nodes.clear()
			make_nodes(time/500)
			if time == 100000:
				time = 0
		show_nodes()
		show_contour()
		pg.display.update()
		time += 1

initialize()
