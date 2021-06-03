#Imports
import pygame, sys
from pygame.locals import *
from SecretCodeModule import *
#Initialize
pygame.init()
canvas = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Secret Code")
#Loading
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
#Clues
clues = []
#Actions
def RedButton(): #RedButton Action
	pass
def OrangeButton(): #OrangeButton Action
	pass
def YellowButton(): #YellowButton Action
	pass
def GreenButton(): #GreenButton Action
	pass
def BlueButton(): #BlueButton Action
	pass
def PurpleButton(): #PurpleButton Action
	pass
def PinkButton(): #PinkButton Action
	pass
def WhiteButton(): #WhiteButton Action
	pass
#Buttons
buttons = {pygame.Rect(475, 100, 50, 50):RedButton, \
	pygame.Rect(475, 150, 50, 50):OrangeButton, \
	pygame.Rect(475, 200, 50, 50):YellowButton, \
	pygame.Rect(475, 250, 50, 50):GreenButton, \
	pygame.Rect(475, 300, 50, 50):BlueButton, \
	pygame.Rect(475, 350, 50, 50):PurpleButton, \
	pygame.Rect(475, 400, 50, 50):PinkButton, \
	pygame.Rect(475, 450, 50, 50):WhiteButton}
#Infinite Loop
while True:
	#Clear screen
	canvas.fill((255, 255, 255))
	#Display
	canvas.blit(Title, (0, 0))
	canvas.blit(SideBar, (400, 0))
	canvas.blit(pygame.Rect(475, 100))
	canvas.blit(pygame.Rect(475, 150))
	canvas.blit(pygame.Rect(475, 200))
	canvas.blit(pygame.Rect(475, 250))
	canvas.blit(pygame.Rect(475, 300))
	canvas.blit(pygame.Rect(475, 350))
	canvas.blit(pygame.Rect(475, 400))
	canvas.blit(pygame.Rect(475, 450))
	for x in range(110, 370, 80):
		for y in range(100, 600, 50):
			canvas.blit(BigHole, (x, y))
	for x in range(10, 75, 20):
		for y in range(117, 568, 50):
			canvas.blit(LittleHole, (x, y))
	#Event loop
	for event in pygame.event.get():
		#Quit if needed
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			for button in list(buttons.keys()):
				if button.collidepoint(pos):
					buttons[button]()
	pygame.display.update()
