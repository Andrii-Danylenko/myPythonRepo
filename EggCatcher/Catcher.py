class Catcher:
    def __init__(self, canvas, color, score):
        self.canvas = canvas
        self.score = score
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 350)
        self.x = 0
        self.offset = 20
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turnLeft)
        self.canvas.bind_all('<KeyRelease-Left>', self.stop)
        self.canvas.bind_all('<KeyPress-Right>', self.turnRight)
        self.canvas.bind_all('<KeyRelease-Right>', self.stop)

    def turnLeft(self, evt):
        if self.canvas.coords(self.id)[0] > 0:
            self.x -= self.offset

    def turnRight(self, evt):
        if self.canvas.coords(self.id)[2] <= self.canvas.winfo_width() - self.offset:
            self.x += self.offset

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        if self.__getPos__(0) <= 0 or self.__getPos__(2) >= self.canvas.winfo_width():
            self.stop(evt=0)

    def __getPos__(self, value):
        return self.canvas.coords(self.id)[value]

    def stop(self, evt):
        self.x = 0
