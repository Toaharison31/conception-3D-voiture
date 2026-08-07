import customtkinter as ctk

from src import config
from src.ui.widgets.actions import bouton_phares_action, bouton_portes_action, slider_ior_action, \
    slider_opacity_vitre_action, bouton_voiture_action, slider_braquer_roues_action, entry_pbr_carrosserie_action, slider_topologie_action, slider_epaisseur_coque_action, slider_garde_au_sol_action, entry_dimensions_action


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
            fg_color="#0F378A",
            corner_radius=0
        )
        self.header_frame.pack(side="top", fill="x")

        self.header_title = ctk.CTkLabel(
            self.header_frame,
            text="🚘 c.3D.v",
            text_color="#C7B4C3",
            font=("Arial", 42, "bold")
        )
        self.header_title.pack(side="top", anchor="w", padx=6, pady=(6, 6))


        """ASIANA NY ACTIONS REHETRA ETO"""
        # entry dimmension longueur
        self.label_dimension_longueur = ctk.CTkLabel(
            self,
            text="Longueur",
            font=("Arial", 12, "bold"),
            text_color="#FFFFFF"
        )
        self.label_dimension_longueur.pack(side="top", anchor="w", padx=6, pady=(3, 0))
        self.entry_dimensions_longueur = ctk.CTkEntry(
            self,
            width=50,
            text_color="#FFF",
            font=("Arial", 12, "bold"),
        )
        self.entry_dimensions_longueur.pack(side="top", anchor="w", padx=6, pady=(6, 6))

        # entry dimmension largeur
        self.label_dimension_largeur = ctk.CTkLabel(
            self,
            text="Largeur",
            font=("Arial", 12, "bold"),
            text_color="#FFFFFF"
        )
        self.label_dimension_largeur.pack(side="top", anchor="w", padx=6, pady=(3, 0))
        self.entry_dimensions_largeur = ctk.CTkEntry(
            self,
            width=50,
            text_color="#FFF",
            font=("Arial", 12, "bold"),
        )
        self.entry_dimensions_largeur.pack(side="top", anchor="w", padx=6, pady=(6, 6))

        # entry dimmension hauteur
        self.label_dimension_hauteur = ctk.CTkLabel(
            self,
            text="Hauteur",
            font=("Arial", 12, "bold"),
            text_color="#FFFFFF"
        )
        self.label_dimension_hauteur.pack(side="top", anchor="w", padx=6, pady=(3, 0))
        self.entry_dimensions_hauteur = ctk.CTkEntry(
            self,
            width=50,
            text_color="#FFF",
            font=("Arial", 12, "bold"),
        )
        self.entry_dimensions_hauteur.pack(side="top", anchor="w", padx=6, pady=(6, 6))

        # entry dimmension empattement
        self.label_dimension_empattement = ctk.CTkLabel(
            self,
            text="Empattement",
            font=("Arial", 12, "bold"),
            text_color="#FFFFFF"
        )
        self.label_dimension_empattement.pack(side="top", anchor="w", padx=6, pady=(3, 0))
        self.entry_dimensions_empattement = ctk.CTkEntry(
            self,
            width=50,
            text_color="#FFF",
            font=("Arial", 12, "bold"),
        )
        self.entry_dimensions_empattement.pack(side="top", anchor="w", padx=6, pady=(6, 6))
        self.bouton_dimension_valide = ctk.CTkButton(
            self,
            text="VALIDER",
            command=self.dimensions_valide
        )
        self.bouton_dimension_valide.pack(side="top", anchor="w", padx=6, pady=(6, 6))

        # slider garde au sol
        self.slider_garde_au_sol = ctk.CTkSlider(
            self,
            from_=0,
            to=60,
            number_of_steps=3,
            command=slider_garde_au_sol_action
        )
        self.slider_garde_au_sol.pack(side="top", anchor="w", padx=6, pady=(6, 6))

        # slider epaisseur coque
        self.slider_epaiseur_coque = ctk.CTkSlider(
            self,
            from_=0,
            to=60,
            number_of_steps=3,
            command=slider_epaisseur_coque_action
        )
        self.slider_epaiseur_coque.pack(side="top", anchor="w", padx=6, pady=(6, 6))

        # slider topologie
        self.slider_topologie = ctk.CTkSlider(
            self,
            from_=0,
            to=60,
            number_of_steps=3,
            command=slider_topologie_action
        )
        self.slider_topologie.pack(side="top", anchor="w", padx=6, pady=(6, 6))

        # entry pbr_carrosserie roughness
        self.label_pbr_carrosserie_roughness = ctk.CTkLabel(
            self,
            text="Roughness",
            font=("Arial", 12, "bold"),
            text_color="#FFFFFF"
        )
        self.label_pbr_carrosserie_roughness.pack(side="top", anchor="w", padx=6, pady=(3, 0))
        self.entry_pbr_carrosserie_roughness = ctk.CTkEntry(
            self,
            width=50,
            text_color="#FFF",
            font=("Arial", 12, "bold")
        )
        self.entry_pbr_carrosserie_roughness.pack(side="top", anchor="w", padx=6, pady=(6, 6))

        # entry pbr_carrosserie metallic
        self.label_pbr_carrosserie_metallic = ctk.CTkLabel(
            self,
            text="Metallic",
            font=("Arial", 12, "bold"),
            text_color="#FFFFFF"
        )
        self.label_pbr_carrosserie_metallic.pack(side="top", anchor="w", padx=6, pady=(3, 0))
        self.entry_pbr_carrosserie_metallic = ctk.CTkEntry(
            self,
            width=50,
            text_color="#FFF",
            font=("Arial", 12, "bold"),
        )
        self.entry_pbr_carrosserie_metallic.pack(side="top", anchor="w", padx=6, pady=(6, 6))

        # entry pbr_carrosserie clearcoat
        self.label_pbr_carrosserie_clearcoat = ctk.CTkLabel(
            self,
            text="Clearcoat",
            font=("Arial", 12, "bold"),
            text_color="#FFFFFF"
        )
        self.label_pbr_carrosserie_clearcoat.pack(side="top", anchor="w", padx=6, pady=(3, 0))
        self.entry_pbr_carrosserie_clearcoat = ctk.CTkEntry(
            self,
            width=50,
            text_color="#FFF",
            font=("Arial", 12, "bold"),
        )
        self.entry_pbr_carrosserie_clearcoat.pack(side="top", anchor="w", padx=6, pady=(6, 6))
        self.bouton_pbr_carrosserie_valide = ctk.CTkButton(
            self,
            text="VALIDER",
            command=self.pbr_carrosserie_valide
        )
        self.bouton_pbr_carrosserie_valide.pack(side="top", anchor="w", padx=6, pady=(6, 6))

        # slider opacity vitre
        self.slider_opacity_vitre = ctk.CTkSlider(
            self,
            from_=0,
            to=60,
            number_of_steps=600,
            command=slider_opacity_vitre_action
        )
        self.slider_opacity_vitre.set(0)
        self.slider_opacity_vitre.pack(side="top", anchor="w", padx=6, pady=(6, 6))

        # slider ior
        self.slider_ior = ctk.CTkSlider(
            self,
            from_=0,
            to=3,
            number_of_steps=300,
            command=slider_ior_action
        )
        self.slider_ior.set(0)
        self.slider_ior.pack(side="top", anchor="w", padx=6, pady=(6, 6))

        # bouton portes
        self.bouton_portes = ctk.CTkButton(
            self,
            fg_color="green",
            text="CLOSE",
            command=lambda: bouton_portes_action(self.bouton_portes)
        )
        self.bouton_portes.pack(side="top", anchor="w", padx=11, pady=11)

        # bouton phares
        self.bouton_phares = ctk.CTkButton(
            self,
            fg_color="red",
            text="OFF",
            command=lambda: bouton_phares_action(self.bouton_phares)
        )
        self.bouton_phares.pack(side="top", anchor="w", padx=11, pady=11)

        # slider braquer roues
        self.slider_braquer_roues = ctk.CTkSlider(
            self,
            from_=-33,
            to=33,
            number_of_steps=30,
            command=slider_braquer_roues_action
        )
        self.slider_braquer_roues.set(0)
        self.slider_braquer_roues.pack(side="top", anchor="w", padx=6, pady=(6, 6))

        # bouton de lancement
        self.ok = ctk.CTkButton(
            self,
            fg_color="blue",
            text="GÉNÉRER",
            command=bouton_voiture_action
        )
        self.ok.pack(side="top", anchor="w", padx=11, pady=11)

    # validation (bouton VALIDER) DIMENSION
    def dimensions_valide(self):
        longueur = self.entry_dimensions_longueur.get()
        largeur = self.entry_dimensions_largeur.get()
        hauteur = self.entry_dimensions_hauteur.get()
        empattement = self.entry_dimensions_empattement.get()
        entry_dimensions_action(longueur, largeur, hauteur, empattement)

    # validation (bouton VALIDER) CARROSSERIE
    def pbr_carrosserie_valide(self):
        roughness = self.entry_pbr_carrosserie_roughness.get()
        metallic = self.entry_pbr_carrosserie_metallic.get()
        clearcoat = self.entry_pbr_carrosserie_clearcoat.get()
        entry_pbr_carrosserie_action(roughness, metallic, clearcoat)


