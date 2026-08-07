from src.ui.widgets.main_window import MainWindow

class MainController:
    def __init__(self):
        self.main_window = MainWindow(self)

    def start(self):
        self.main_window.mainloop()

