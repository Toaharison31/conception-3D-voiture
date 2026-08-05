import customtkinter as ctk
from src import config
from src.ui.widgets.actions import bouton_phares_action, bouton_portes_action, slider_ior_action, \
    slider_opacity_vitre_action, bouton_voiture_action, slider_braquer_roues_action


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


        """ASIANA NY ACTIONS REHETRA ETO"""
        # slider opacity vitre
        self.slider_opacity_vitre = ctk.CTkSlider(
            self,
            fg_color="#CEC7C7",
            from_=0,
            to=100,
            number_of_steps=1000,
            command=slider_opacity_vitre_action
        )
        self.slider_opacity_vitre.set(0)
        self.slider_opacity_vitre.pack(side="top", anchor="w", padx=20, pady=(20, 20))

        # slider ior
        self.slider_ior = ctk.CTkSlider(
            self,
            fg_color="#CEC7C7",
            from_=0,
            to=3,
            number_of_steps=300,
            command=slider_ior_action
        )
        self.slider_ior.set(0)
        self.slider_ior.pack(side="top", anchor="w", padx=20, pady=(20, 20))

        # bouton portes
        self.bouton_portes = ctk.CTkButton(
            self,
            fg_color="green",
            text="CLOSE",
            command=lambda: bouton_portes_action(self.bouton_portes)
        )
        self.bouton_portes.pack(
            side="top",
            anchor="w",
            padx=15,
            pady=15
        )

        # bouton phares
        self.bouton_phares = ctk.CTkButton(
            self,
            fg_color="red",
            text="OFF",
            command=lambda: bouton_phares_action(self.bouton_phares)
        )
        self.bouton_phares.pack(
            side="top",
            anchor="w",
            padx=15,
            pady=15
        )
        # slider braquer roues
        self.slider_braquer_roues = ctk.CTkSlider(
            self,
            fg_color="#CEC7C7",
            from_=-35,
            to=35,
            number_of_steps=30,
            command=slider_braquer_roues_action
        )
        self.slider_braquer_roues.set(0)
        self.slider_braquer_roues.pack(side="top", anchor="w", padx=20, pady=(20, 20))

        # bouton de lancement
        self.ok = ctk.CTkButton(
            self,
            fg_color="blue",
            text="GÉNÉRER",
            command=bouton_voiture_action
        )
        self.ok.pack(
            side="top",
            anchor="w",
            padx=15,
            pady=15
        )



