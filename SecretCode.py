#Imports
import pygame, sys
from pygame.locals import *
from SecretCodeModule import *
#Initialize
pygame.init()
canvas = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Secret Code")
#Loading
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
#Infinite Loop
while True:
	#Clear screen
	canvas.fill((255, 255, 255))
	#Display
	canvas.blit(Title, (0, 0))
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
	pygame.display.update()
