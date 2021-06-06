#Imports
import pygame, sys, random
from pygame.locals import *
from SecretCodeModule import *
#Initialize
pygame.init()
canvas = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Secret Code")
#--- Clue Class ---
class Piece:
	def __init__(self, image):
		img_val = {RED:1, ORANGE:2, YELLOW:3, GREEN:4, BLUE:5, PURPLE:6, PINK:7, WHITE:8}
		self.image = image
		self.value = img_val[image]
#Loading
ClickedHole = pygame.image.load("Images/ClickedHole.png")
SideBar = pygame.image.load("Images/SideBar.png")
Title = pygame.image.load("Images/Title.png")
BigHole = pygame.image.load("Images/BigHole.png")
BlueBead = pygame.image.load("Images/BlueBead.png")
Correct = pygame.image.load("Images/Correct.png")
Error = pygame.image.load("Images/Error.png")
GreenBead = pygame.image.load("Images/GreenBead.png")
LittleHole = pygame.image.load("Images/LittleHole.png")
OrangeBead = pygame.image.load("Images/OrangeBead.png")
PinkBead = pygame.image.load("Images/PinkBead.png")
PurpleBead = pygame.image.load("Images/PurpleBead.png")
RedBead = pygame.image.load("Images/RedBead.png")
WhiteBead = pygame.image.load("Images/WhiteBead.png")
YellowBead = pygame.image.load("Images/YellowBead.png")
#Constants
RED = RedBead
ORANGE = OrangeBead
YELLOW = YellowBead
GREEN = GreenBead
BLUE = BlueBead
PURPLE = PurpleBead
PINK = PinkBead
WHITE = WhiteBead
#Variables
code = [random.randint(1, 8), random.randint(1, 8), random.randint(1, 8), random.randint(1, 8)]
clues = []
currentClue = [None, None, None, None]
buttonMode = None
Hole = 0
Layer = 9
#Actions
def RedButton(): #RedButton Action
	global buttonMode
	buttonMode = RED
def OrangeButton(): #OrangeButton Action
	global buttonMode
	buttonMode = ORANGE
def YellowButton(): #YellowButton Action
	global buttonMode
	#print ("BUTTON YELLOW")
	buttonMode = YELLOW
def GreenButton(): #GreenButton Action
	global buttonMode
	#print ("BUTTON GREEN")
	buttonMode = GREEN
def BlueButton(): #BlueButton Action
	global buttonMode
	#print ("BUTTON BLUE")
	buttonMode = BLUE
def PurpleButton(): #PurpleButton Action
	global buttonMode
	#print ("BUTTON PURPLE")
	buttonMode = PURPLE
def PinkButton(): #PinkButton Action
	global buttonMode
	#print ("BUTTON PINK")
	buttonMode = PINK
def WhiteButton(): #WhiteButton Action
	global buttonMode
	#print ("BUTTON WHITE")
	buttonMode = WHITE
#Buttons
buttons = {(475, 100, 50, 50):RedButton, \
	(475, 150, 50, 50):OrangeButton, \
	(475, 200, 50, 50):YellowButton, \
	(475, 250, 50, 50):GreenButton, \
	(475, 300, 50, 50):BlueButton, \
	(475, 350, 50, 50):PurpleButton, \
	(475, 400, 50, 50):PinkButton, \
	(475, 450, 50, 50):WhiteButton}
#Conversion Dict
convert = {1:RED, 2:ORANGE, 3:YELLOW, 4:GREEN, 5:BLUE, 6:PURPLE, 7:PINK, 8:WHITE}
#print (code)
#Infinite Loop
while True:
	#Clear screen
	canvas.fill((255, 255, 255))
	#Display
	canvas.blit(Title, (0, 0))
	canvas.blit(SideBar, (400, 0))
	canvas.blit(RedBead, (475, 100))
	canvas.blit(OrangeBead, (475, 150))
	canvas.blit(YellowBead, (475, 200))
	canvas.blit(GreenBead, (475, 250))
	canvas.blit(BlueBead, (475, 300))
	canvas.blit(PurpleBead, (475, 350))
	canvas.blit(PinkBead, (475, 400))
	canvas.blit(WhiteBead, (475, 450))
	for x in range(110, 370, 80):
		for y in range(100, 600, 50):
#			print (currentClue)
			if currentClue[(x-110)//80] != None and (y - 100)/50 == Layer:
				canvas.blit(currentClue[(x-110)//80].image, (x, y))
				#print ("Whoopdy doo")
			elif (y - 100)//50 > Layer:
				#print ((y-100)//80)
				canvas.blit(convert[clues[Layer-(y-100)//50][0][(x-110)//80]], (x, y))
			if (x - 110)/80 == Hole and (y - 100)/50 == Layer:
				canvas.blit(ClickedHole, (x, y))
				continue
			#print ((x-110)//80)
			canvas.blit(BigHole, (x, y))

	for x in range(10, 75, 20):
		for y in range(117, 568, 50):
			canvas.blit(LittleHole, (x, y))
			if (y - 117)//50 > Layer and (x-10)//20 + 1 <= clues[Layer-(y-117)//50][1] + clues[Layer-(y-117)//50][2]:
				if (x-10)//20 + 1<= clues[Layer-(y-117)//50][1]:
					canvas.blit(Correct, (x, y))
#				elif (x-10)<=clues[Layer-(y-117)//50][1]:
#					pass
				else:
					canvas.blit(Error, (x, y))
	#Event loop
	for event in pygame.event.get():
		#Quit if needed
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			for button in list(buttons.keys()):
				if pygame.Rect(*button).collidepoint(pos):
					buttons[button]()
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				if Hole + 1 > 3:
					continue
				Hole += 1
			if event.key == K_LEFT:
				if Hole - 1 < 0:
					continue
				Hole -= 1
			if event.key == K_SPACE:
				#print (buttonMode != None)
				if buttonMode != None:
					currentClue[Hole] = Piece(buttonMode)
					#print (currentClue[Hole])
			if event.key == K_RETURN:
				if None not in currentClue:
					#print (currentClue)
					clues += [get_clue(code, [x.value for x in currentClue])]
					#print (clues[-1])
					currentClue = [None, None, None, None]
					Layer -= 1
	pygame.display.update()
