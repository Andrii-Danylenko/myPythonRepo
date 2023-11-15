import random


class Egg:
    def __init__(self, canvas, color, score, paddle):
        self.paddle = paddle
        self.canvas = canvas
        self.score = score
        self.id = canvas.create_oval(0, 0, 25, 25, fill=color)
        self.canvas.move(self.id, random.randint(10, 490), -10)
        self.y = random.randint(1, 7)

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[3] >= self.canvas.winfo_height():
            self.score.lostEgg()
            self.canvas.delete(self.id)
            return 'hit bottom'
        elif self.hit_paddle(pos):
            self.score.caughtEgg()
            self.canvas.delete(self.id)
            return 'hit paddle'
        return None

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] and paddle_pos[1] <= pos[3] <= paddle_pos[3]:
            return True
        return False
