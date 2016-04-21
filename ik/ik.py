from math import *
import pygame as pg
import time
import serial

l1=150   #link 1 length
l2=100	 #link 2 length

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
	
	temp = ((x*x+y*y-l1*l1-l2*l2)*1.0)/(2*l1*l2*1.0)
	try:
		b=atan2(sqrt(1.0-temp*temp),temp)
	except:
		b=0
	b=-1*b
	k1=l1+l2*cos(b)
	k2=l2*sin(b)
	a=atan2(y,x)-atan2(k2,k1)
	c=0
	print ceil(a*57.3),ceil(-1*b*57.3),c
	#ser.write(str(ceil(57.3*a))+"+"+str(ceil(57.3*-1*b))+"+"+str(ceil(57.3*c))+"+"+"\0")
	return a,b,c

LEFT = 1
MIDDLE = 2
RIGHT = 3
WHEEL_UP = 4
WHEEL_DOWN = 5

pg.init()
pg.display.set_caption('Final year project')
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
	pg.draw.line(screen,(233,188,82),(0+250,500-50),(l1*cos(a)+250,500-l2*(sin(a))-50),3)
	pg.draw.line(screen,(23,199,45),(l1*cos(a)+250,500-l2*(sin(a))-50),(x+250,y-50),3)
	pg.display.flip()
	screen.fill((255,255,255))


pg.quit()	
sys.exit()
	
