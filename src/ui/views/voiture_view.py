from src.models.voiture_model import Vehicule3D
voiture = Vehicule3D(marque="BMW", couleur="Red")

# Logique de calcul
# tsy vita
def dimensions_view(valeur1, valeur2, valeur3, valeur4):
    longueur = valeur1
    largeur = valeur2
    hauteur = valeur3
    empattement = valeur4
    return voiture.set_dimensions(
        longueur=longueur,
        largeur=largeur,
        hauteur=hauteur,
        empattement=empattement,
    )

# tsy vita
def garde_au_sol_view(valeur):
    distance = valeur
    return voiture.set_garde_au_sol(distance)

# tsy vita
def epaisseur_coque_view(valeur):
    volume = valeur
    return voiture.set_epaisseur_coque(volume)

# tsy vita
def topologie_view(valeur):
    polycount = valeur
    return voiture.set_topologie(polycount)

# tsy vita
def pbr_carrosserie_view(valeur1, valeur2, valeur3):
    roughness = valeur1
    metallic = valeur2
    clearcoat = valeur3
    return voiture.set_pbr_carrosserie(roughness, metallic, clearcoat)

# vita
def opacity_vitre_view(valeur):
    transparence = valeur
    return voiture.set_opacity_vitre(transparence)

# vita
def ior_view(valeur):
    refraction = valeur
    return voiture.set_ior(refraction)

# vita
def portes_ouvertes_view(valeur: bool):
    est_ouverte = valeur
    return voiture.set_portes_ouvertes(est_ouverte)

# vita
def phares_allumes_view(valeur: bool):
    get_est_allume = valeur
    return voiture.set_phares_allumes(get_est_allume)

# tsy vita
def braquer_roues_view(valeur):
    angle = valeur
    return voiture.set_braquer_roues(angle)
