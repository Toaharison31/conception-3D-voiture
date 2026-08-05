from src.models.vehicule_model import VehiculeModel

class Vehicule3D(VehiculeModel):
    def __init__(self, marque, couleur):
        super().__init__(marque, couleur)

        # ATTRIBUTS GÉOMÉTRIQUES ET STRUCTURELS
        self.longueur = 0.00
        self.largeur = 0.00
        self.hauteur = 0.00
        self.empattement = 0.00
        self.garde_au_sol = 0.00
        self.epaisseur_coque = 0.00
        self.topologie = 0

        # ATTRIBUTS DE SURFACE ET MATÉRIAUX (PBR/SHADING)
        self.albedo = couleur
        self.roughness = 0.00
        self.metallic = 0.00
        self.clearcoat = 1.00 # couche de vernis
        self.opacity_vitre = 0.00
        self.ior = 0.00

        # ATTRIBUTS FONCTIONNELS ET MÉCANIQUES
        self.portes_ouvertes = False
        self.phares_allumes = False
        self.angle_braquage = 0.00

    # tsy vita
    def set_dimensions(self, longueur: float, largeur: float, hauteur: float, empattement: float):
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur
        self.empattement = empattement
        return self

    # tsy vita
    def set_garde_au_sol(self, distance: float):
        self.garde_au_sol = distance
        return self

    # tsy vita
    def set_epaisseur_coque(self, volume: float):
        self.epaisseur_coque = volume
        return self

    # tsy vita
    def set_topologie(self, polycount: float):
        self.topologie = polycount
        return self

    # tsy vita
    def set_pbr_carrosserie(self, roughness: float , metallic: float, clearcoat: float):
        self.roughness = roughness
        self.metallic = metallic
        self.clearcoat = clearcoat
        return self

    # vita
    def set_opacity_vitre(self, transparene: float):
        self.opacity_vitre = transparene
        return self

    # vita
    def set_ior(self, refraction: float):
        self.ior = refraction
        return self

    # vita
    def set_portes_ouvertes(self, est_ouverte: bool):
        self.portes_ouvertes = est_ouverte
        return self

    # vita
    def set_phares_allumes(self, est_allume: bool):
        self.phares_allumes = est_allume
        return self

    # tsy vita
    def set_braquer_roues(self, angle: float):
        self.angle_braquage = max(-35.0, min(35.0, angle))
        return self

    def __str__(self):
        return (
            f"Voiture {self.marque} {self.couleur}\n"
            f"Dimensions: ({self.longueur} x {self.largeur} x {self.hauteur} x {self.empattement})\n"
            f"Garde au sol: {self.garde_au_sol}\n"
            f"Epaisseur coque: {self.epaisseur_coque}\n"
            f"Polycount: {self.topologie} tris.\n"
            f"Carrosserie: ({self.roughness} x {self.metallic} x {self.clearcoat})\n"
            f"Opacity: {self.opacity_vitre}\n"
            f"IOR: {self.ior}\n"
            f"Portes: {self.portes_ouvertes}\n"
            f"Phares: {self.phares_allumes}\n"
        )