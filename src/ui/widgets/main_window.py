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

        """ETO NO MAMPIDITRA NY UI REHETRA"""
        # header
        self.header_frame = ctk.CTkFrame(
            self,
            fg_color="#0F578A",
            corner_radius=0
        )
        self.header_frame.pack(side="top", fill="x")

        self.header_title = ctk.CTkLabel(
            self.header_frame,
            text="🚘 c.3D.v",
            text_color="#CEC7C7",
            font=("Arial", 42, "bold")
        )
        self.header_title.pack(side="top", anchor="w", padx=20, pady=(20, 20))


