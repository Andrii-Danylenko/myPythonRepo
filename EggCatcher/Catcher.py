class Catcher:
    def __init__(self, canvas, color, score):
        self.canvas = canvas
        self.score = score
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 350)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turnLeft)
        self.canvas.bind_all('<KeyRelease-Left>', self.stop)
        self.canvas.bind_all('<KeyPress-Right>', self.turnRight)
        self.canvas.bind_all('<KeyRelease-Right>', self.stop)

    def turnLeft(self, evt):
        if self.canvas.coords(self.id)[0] > 0:
            self.x = -20

    def turnRight(self, evt):
        if self.canvas.coords(self.id)[2] >= self.canvas_width:
            self.x = 20

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= 500:
            self.x = 0

    def stop(self, evt):
        self.x = 0
