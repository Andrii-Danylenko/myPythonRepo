class EventHandler:
    def __init__(self, gameWindow):
        self.gameWindow = gameWindow
        self.is_active = True
        self.gameWindow.bind_all('<Escape>', self.on_escape)

    def on_escape(self, event=None):
        self.is_active = False
        self.gameWindow.destroy()
        print("Гра завершена!")
