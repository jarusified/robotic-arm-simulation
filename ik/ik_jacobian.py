from math import *
import pygame as pg
import time
import serial
import sympy

l1=150   #link 1 length
l2=150	 #link 2 length

"""
try:
	ser = serial.Serial('/dev/ttyUSB0',9600)
except:
	try:
		ser = serial.Serial('/dev/ttyUSB1',9600)
	except:
		try:
			ser = serial.Serial('/dev/ttyUSB2',9600)
		except:
			try:
				ser = serial.Serial('/dev/ttyUSB3',9600)
			except:
				#ser = serial.Serial('/dev/ttyUSB5',9600)
				pass
			#ser = serial.Serial('/dev/ttyUSB3',9600)
"""
def inv(x,y,z):	
	a1,a2,l1,l2 = symbols('a1 a2 l1 l2')
	hx = l1*cos(a1) + l2*cos(a1+a2)
	hy = l1*sin(a1) + l2*sin(a1+a2)
	J11 = diff(hx,a1)
	J12 = diff(hx,a2)
	J21 = diff(hy,a1)
	J22 = diff(hy,a2)
	print J11
	print J12
	print J21
	print J22

LEFT = 1
MIDDLE = 2
RIGHT = 3
WHEEL_UP = 4
WHEEL_DOWN = 5

pg.init()
pg.display.set_caption('simulation')
screen=pg.display.set_mode((500,500))
Run = True
while Run:
	
	#time.sleep(1)
	(x,y)=pg.mouse.get_pos()
	x=x-250
	y=y+50
	a,b,c=inv(x,500-y,10)

	for event in pg.event.get():
		if (event.type==pg.QUIT):
			Run=False
	
	#pg.draw.line(screen,(255,0,0),(0,500),(l1*cos(a),l1*sin(a)),3)
	#pg.draw.line(screen,(255,0,0),(l1*cos(a),l1*sin(a)),(x,y),3)
	pg.draw.line(screen,(255,0,0),(0+250,500-50),(l1*cos(a)+250,500-l2*(sin(a))-50),3)
	pg.draw.line(screen,(255,0,0),(l1*cos(a)+250,500-l2*(sin(a))-50),(x+250,y-50),3)
	pg.display.flip()
	screen.fill((255,255,255))


pg.quit()	
sys.exit()
	
