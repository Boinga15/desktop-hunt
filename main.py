from actors import *
from shared_memory_dict import SharedMemoryDict
import time
import threading
import os
import keyboard

class Game:
    def __init__(self):
        # Base Variables
        self.isRunning = True

        self.gamePhase = 2
        """
        0 = Main Menu
        1 = Game Setup
        2 = Play Mode
        3 = Results Screen
        """

        # Shared Memory Dictionary Setup
        self.smd_config = SharedMemoryDict(name='config', size=1024)
        self.smd_config["x"] = 0
        self.smd_config["y"] = 0

        # Windows
        self.openWindows = []

        # Gameplay
        self.player = Player(500, 500)


    def windowThread(self, windowType):
        os.system('python -m window.py ' + str(windowType))
    
    def openNewWindow(self, windowType):
        """
        Window Types:
        0 = Player Window (the one that follows the player around).
        """
        newThread = threading.Thread(target=self.windowThread, args=(windowType,))
        newThread.start()
        self.openWindows.append([newThread, windowType])
    
    def setup(self):
        match self.gamePhase:
            case 0:
                pass

            case 1:
                pass

            case 2:
                self.openNewWindow(0)

            case 3:
                pass
    
    def logic(self):
        pass

    def inputs(self):
        if keyboard.is_pressed("d"):
            self.player.x += 5
        elif keyboard.is_pressed("a"):
            self.player.x -= 5

        if keyboard.is_pressed("w"):
            self.player.y -= 5
        elif keyboard.is_pressed("s"):
            self.player.y += 5


    def dataWrite(self):
        self.smd_config["x"] = self.player.x
        self.smd_config["y"] = self.player.y

game = Game()
game.setup()

while game.isRunning:
    game.logic()
    game.inputs()
    game.dataWrite()
    time.sleep(0.01)

for window in game.openWindows:
    window[0].join()
