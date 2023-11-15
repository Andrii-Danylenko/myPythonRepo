from Egg import Egg
import time
import random
from tkinter import *
from Score import Score
from Catcher import Catcher
gameWindow = Tk()
gameWindow.title("Ловець")
gameWindow.resizable(0, 0)
gameWindow.wm_attributes("-topmost", 1)
canvas = Canvas(gameWindow, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
score = Score(canvas)
colors = ["fuchsia", "red", "yellow", "blue", "black", "maroon", "purple"]
random.shuffle(colors)
catcher = Catcher(canvas, colors[0], score)
eggs = []
while True:
    catcher.canvas.update_idletasks()
    if score.lost == 10:
        break
    catcher.draw()
    if random.randint(1, 100) == 1:
        eggs.append(Egg(canvas, colors[random.randint(0, len(colors) - 1)], score, catcher))
    for egg in list(eggs):
        result = egg.draw()
        if result == 'hit bottom':
            eggs.remove(egg)
        if result == 'hit paddle':
            eggs.remove(egg)
    gameWindow.update_idletasks()
    gameWindow.update()
    time.sleep(0.01)

gameWindow.update()
time.sleep(5)

