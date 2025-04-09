import math

# Fonction pour calculer la surface et le périmètre d'un carré
def carre(cote):
    surface = cote * cote
    perimetre = 4 * cote
    return surface, perimetre

# Fonction pour calculer la surface et le périmètre d'un rectangle
def rectangle(longueur, largeur):
    surface = longueur * largeur
    perimetre = 2 * (longueur + largeur)
    return surface, perimetre

# Fonction pour calculer la surface et le périmètre d'un cercle
def cercle(rayon):
    surface = math.pi * (rayon ** 2)
    perimetre = 2 * math.pi * rayon
    return surface, perimetre

# Fonction pour calculer la surface et le volume d'une sphère
def sphere(rayon):
    surface = 4 * math.pi * (rayon ** 2)
    volume = (4/3) * math.pi * (rayon ** 3)
    return surface, volume

# Exemple d'utilisation des fonctions
if __name__ == "__main__":
    # Carré
    cote = 5
    surface_carre, perimetre_carre = carre(cote)
    print(f"Carré - Surface: {surface_carre}, Périmètre: {perimetre_carre}")

    # Rectangle
    longueur = 6
    largeur = 4
    surface_rectangle, perimetre_rectangle = rectangle(longueur, largeur)
    print(f"Rectangle - Surface: {surface_rectangle}, Périmètre: {perimetre_rectangle}")

    # Cercle
    rayon = 3
    surface_cercle, perimetre_cercle = cercle(rayon)
    print(f"Cercle - Surface: {surface_cercle}, Périmètre: {perimetre_cercle}")

    # Sphère
    rayon_sphere = 4
    surface_sphere, volume_sphere = sphere(rayon_sphere)
    print(f"Sphère - Surface: {surface_sphere}, Volume: {volume_sphere}")