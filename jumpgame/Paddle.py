class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.offset = 3
        self.speedOffset = 2
        self.maxSpeed = 5
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyRelease-Left>', self.stop)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyRelease-Right>', self.stop)
        self.speed = 0

    def turn_left(self, event):
        if self.canvas.coords(self.id)[0] > 0 + self.maxSpeed + self.offset:
            self.x -= min(self.offset - self.offset * 0.1, self.maxSpeed)
            self.speed += self.speedOffset * 0.1

    def turn_right(self, event):
        currOffset = min(self.offset + self.offset * 0.1, self.maxSpeed)
        if self.canvas.coords(self.id)[2] <= self.canvas.winfo_width() - (self.maxSpeed + self.offset):
            self.x += currOffset
            self.speed += self.speedOffset * 0.1

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        if self.__getPos__(0) <= 0 or self.__getPos__(2) >= self.canvas.winfo_width():
            self.stop(event=0)

    def __getPos__(self, value):
        return self.canvas.coords(self.id)[value]

    def stop(self, event):
        self.x = 0
        self.speed = 0

    def get_speed(self):
        return self.speed
