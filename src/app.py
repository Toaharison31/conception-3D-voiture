from src.core.controllers.main_controller import MainController

class App:
    def __init__(self):
        self.run_controller = MainController()

    def run(self):
        self.run_controller.start()