import random
from tkinter import *
import time
from Ball import Ball
from Paddle import Paddle
from EventHandler import EventHandler
from Score import Score


def game(gameWindow, canvas, btn1) -> None:
    counter(canvas, 3)
    randomColors = ["red", "yellow", "blue", "black", "green", "cyan"]
    random.shuffle(randomColors)
    btn1.destroy()
    gameWindow.update()
    paddle = Paddle(canvas, color=randomColors[0])
    ball = Ball(canvas, paddle, color=randomColors[len(randomColors) - 1])
    gameWindow.bind_all('<Escape>', on_escape)
    event_handler = EventHandler(gameWindow)
    isRendered = False
    score = Score()

    def restart_game():
        gameWindow.destroy()
        main()

    while True:
        if not isRendered:
            canvas.create_text(170, 50, anchor=NW, text=f"Балів: {score.getCurrent()}",
                               font="Arial 20", fill="#FF0000", tags="points")
            isRendered = True

        if not event_handler.is_active:
            break
        if not ball.hit_bottom:
            ball.draw()
            if ball.hit_floor:
                canvas.delete("points")
                score.incrementAndGet()
                ball.hit_floor = False
                isRendered = False
            paddle.draw()
        else:
            loseImage = PhotoImage(file="gameloseImage.png")
            canvas.create_image(10, 10, anchor=NW, image=loseImage)
            canvas.create_text(170, 50, anchor=NW,
                               text=f"Ви програли...\nАле набрали {score.getCurrent()} бал(и)!",
                               font="Arial 20", fill="#ffffff")
            btn = Button(text="Грати знову", font="Arial 20", command=restart_game)
            btn.pack()
            gameWindow.mainloop()

        gameWindow.update_idletasks()
        gameWindow.update()
        time.sleep(0.01)


def on_escape(gameWindow):
    gameWindow.destroy()
    print("Користувач закінчив гру!")


def main() -> None:
    gameWindow = Tk()
    gameWindow.title("Гра")
    gameWindow.resizable(False, False)
    gameWindow.wm_attributes("-topmost", 1)
    canvas = Canvas(gameWindow, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    btn1 = Button(text="Почати ігру", anchor=NW, font="Arial 20", command=lambda: game(gameWindow, canvas, btn1))
    btn1.pack()
    gameWindow.mainloop()


def counter(canvas, seconds):
    counter_text = canvas.create_text(230, 80, anchor=NW,
                                      text=f"{seconds}",
                                      font="Arial 50", fill="#FF0000", tags="counter")
    while seconds > 0:
        canvas.itemconfig(counter_text, text=f"{seconds}")
        canvas.update()
        time.sleep(1)
        seconds -= 1
    canvas.delete("counter")


main()
