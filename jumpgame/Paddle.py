class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.offset = 2
        self.speedOffset = 2
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

        self.speed = 0

    def turn_left(self, event):
        self.x = -self.offset
        self.speed = self.speedOffset

    def turn_right(self, event):
        self.x = self.offset
        self.speed = self.speedOffset

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.stop()

    def stop(self):
        self.x = 0

    def get_speed(self):
        return self.speed
