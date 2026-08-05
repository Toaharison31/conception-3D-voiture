# Classe véhicule
class VehiculeModel:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur

    def __str__(self):
        return f"{self.marque} {self.couleur}"


