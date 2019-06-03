#! /usr/bin/python

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

display = pygame.display.set_mode((600,600))

pygame.display.set_caption('Hello PyGame')
pygame.display.update()


font = pygame.font.Font(None, 36)
text = font.render('Hello',1,(255, 255, 255))

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	display.blit(text, pygame.mouse.get_pos())
	pygame.display.update()
