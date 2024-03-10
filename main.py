from actors import *
import time
import threading
import os

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

        # Windows
        self.openWindows = []

        # Gameplay
        self.player = Player(500, 500)


    def windowThread(self, windowType):
        os.system('python window.py ' + str(windowType))
    
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
        pass

game = Game()
game.setup()

while game.isRunning:
    game.logic()
    game.inputs()
    time.sleep(0.01)

for window in game.openWindows:
    window[0].join()
