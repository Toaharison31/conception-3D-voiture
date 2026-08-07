from src.ui.views.voiture_view import *
from src.ui.widgets.main_window import *

"""LES AUTRES"""
# lancement
est_lance = False
def bouton_voiture_action():
    global est_lance
    est_lance = True
    if est_lance:
        print(voiture)
    else:
        est_lance = False

# apparenses dimensions
def entry_dimensions_action(valeur1, valeur2, valeur3, valeur4):
    longueur = valeur1
    largeur = valeur2
    hauteur = valeur3
    empattement = valeur4
    dimensions_view(longueur, largeur, hauteur, empattement)

# apparences garde au sol
def slider_garde_au_sol_action(sld_garde_au_sol):
    distance = round(sld_garde_au_sol, 2)
    garde_au_sol_view(distance)
    # print("Garde au sol", distance)

# apparences epaisseur coque
def slider_epaisseur_coque_action(sld_epaiseur_coque):
    volume = round(sld_epaiseur_coque, 2)
    epaisseur_coque_view(volume)
    # print("Épaisseur coque: ", volume)

# apparences topologie
def slider_topologie_action(sld_topologie):
    polycount = round(sld_topologie, 2)
    topologie_view(polycount)
    # print("Polycount: ", polycount)

# apparences carrosserie
def entry_pbr_carrosserie_action(valeur1, valeur2, valeur3):
    roughness = valeur1
    metallic = valeur2
    clearcoat = valeur3
    pbr_carrosserie_view(roughness, metallic, clearcoat)

# apparences opacity vitre
def slider_opacity_vitre_action(sld_opacity):
    transparence = round(sld_opacity, 2)
    opacity_vitre_view(transparence)
    # print(f"Transparence: {transparence}%") # anaovana test fa fafana après

# apparences ior
def slider_ior_action(sld_ior):
    refraction = round(sld_ior, 2)
    ior_view(refraction)
    # print("Réfraction: ", refraction) # anaovana test fa fafana après

# apparences phares
def bouton_phares_action(btn_phares):
    est_allume = not voiture.phares_allumes
    phares_allumes_view(est_allume)
    if est_allume:
        btn_phares.configure(text="ON", fg_color="green", hover_color="green")
    else:
        btn_phares.configure(text="OFF", fg_color="red", hover_color="red")
    # print("Phares: ", est_allume) # anaovana test fa fafana après

# apparences portes
def bouton_portes_action(btn_portes):
    est_ouverte = not voiture.portes_ouvertes
    portes_ouvertes_view(est_ouverte)
    if est_ouverte:
        btn_portes.configure(text="OPEN", fg_color="green", hover_color="green")
    else:
        btn_portes.configure(text="CLOSE", fg_color="red", hover_color="red")
    # print("Portes: ", est_ouverte) # anaovana test fa fafana après

# apparences braquage
def slider_braquer_roues_action(sld_braquage):
    braquage = round(sld_braquage, 2)
    braquer_roues_view(braquage)
    # print("Braquage", braquage)
