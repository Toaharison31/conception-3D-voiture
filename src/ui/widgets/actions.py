from src.ui.views.voiture_view import *

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

