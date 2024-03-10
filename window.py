import sys
import pygame
import time
import os
import tkinter as tk
import math

from actors import *
from shared_memory_dict import SharedMemoryDict

screenType = int(sys.argv[1])

screenWidth = [400][screenType]
screenHeight = [400][screenType]

root = tk.Tk()
embed = tk.Frame(root, width=screenWidth, height=screenHeight)
embed.pack()

title = ["You"][screenType]

root.resizable(False, False)
root.title(title)

root.update()

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEORIVER'] = "windib"

pygame.init()
pygame.font.init()

# Game properties
tickDelay = 0.01  # Time between updates. Lower time = faster game.
gameTitle = title

screen = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption(gameTitle)

# Game class
class Game:
    def __init__(self):
        self.smd_config = SharedMemoryDict(name='config', size=1024)

    def logic(self):
        global root
        match screenType:
            case 0:
                root.geometry('+' + str(self.smd_config["x"]) + "+" + str(self.smd_config["y"]))
        
    def draw(self):
        global screen
        global screenType
        
        match screenType:
            case 0:
                screen.fill((30, 30, 30))
                pygame.draw.rect(screen, (0, 200, 0), pygame.Rect(180, 180, 40, 40))
        

        pygame.display.flip() # Display drawn objects on screen

# Run the actual game
game = Game() # Game object

gameRunning = True
while gameRunning:
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.QUIT:
            gameRunning = False

    game.logic()
    game.draw()

    root.update()

    time.sleep(tickDelay)

pygame.quit()
root.destroy()
