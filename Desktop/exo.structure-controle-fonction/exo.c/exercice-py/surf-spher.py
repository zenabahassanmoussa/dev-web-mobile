import math

def calculer_surface_sphere(rayon):
    """
    Calcule la surface d'une sphère (aire de la sphère)
    
    Args:
        rayon (float): Rayon de la sphère en unités
        
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
    return 4 * math.pi * (rayon ** 2)

# Exemple d'utilisation avec saisie utilisateur
try:
    r = float(input("Entrez le rayon de la sphère : "))
    surface = calculer_surface_sphere(r)
    print(f"Surface de la sphère : {surface:.2f} unités²")
    
except ValueError as e:
    print(f"Erreur : {e}")
except TypeError as e:
    print(f"Erreur de type : {e}")
except Exception as e:
    print(f"Erreur inattendue : {e}")