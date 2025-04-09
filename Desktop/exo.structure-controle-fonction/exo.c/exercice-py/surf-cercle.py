import math

def calculer_surface_cercle(rayon):
    """
    Calcule la surface d'un cercle
    Args:
        rayon (float): Rayon du cercle en unités
    Returns:
        float: Surface calculée
    Lève:
        TypeError: Si le rayon n'est pas un nombre
        ValueError: Si le rayon est négatif ou nul
    """
    if not isinstance(rayon, (int, float)):
        raise TypeError("Le rayon doit être un nombre")
    if rayon <= 0:
        raise ValueError("Le rayon doit être strictement positif")
    return math.pi * (rayon ** 2)

# Exemple d'utilisation
try:
    r = float(input("Entrez le rayon du cercle (en mètres) : "))
    surface = calculer_surface_cercle(r)
    print(f"Surface du cercle : {surface:.2f} m²")
except ValueError as e:
    print(f"Erreur : {e}")
except TypeError as e:
    print(f"Erreur de type : {e}")