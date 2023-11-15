class Score:
    def __init__(self, canvas):
        self.canvas = canvas
        self.score = 0
        self.lost = 0
        self.text = ""
        self.showText()

    def showText(self):
        if self.text == "":
            self.text = self.canvas.create_text(350, 10, text=f"Спіймав: 0, Пропустив: 0", font="Helvetica 16")
        else:
            self.canvas.itemconfig(self.text, text=f"Спіймав: {self.score}, Пропустив: {self.lost}")

    def caughtEgg(self):
        self.score += 1
        self.showText()

    def lostEgg(self):
        self.lost += 1
        self.showText()
