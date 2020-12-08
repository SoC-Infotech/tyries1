import pygame
import random
pygame.init()
winHeight = 480; winWidth = 700; GREEN = (0,255,0)
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Hangman - by Steven")

#-----------------------------------------------------
# Main program here
inPlay = True
while inPlay:
# Use loop to draw window
    win.fill(GREEN)
    pygame.display.update()
    pygame.time.delay(100)

#-----------------------------------------------------
pygame.quit() # always quit oygame when done!
