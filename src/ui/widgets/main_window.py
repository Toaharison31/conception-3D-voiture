import customtkinter as ctk
from src import config

class MainWindow(ctk.CTk):
    def __init__(self, main_controller):
        super().__init__()
        self.main_controller = main_controller

        # titre
        self.title(f"{config.APP_NAME} - v{config.APP_VERSION}")

        # fenêtre
        self.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.minsize(config.WINDOW_MIN_WIDTH, config.WINDOW_MIN_HEIGHT)

        # thème
        ctk.set_appearance_mode(config.APPEARANCE_MODE)
        ctk.set_default_color_theme(config.COLOR_THEME)

        """ETO NO MAMPIDITRA NY INTERFACE"""

