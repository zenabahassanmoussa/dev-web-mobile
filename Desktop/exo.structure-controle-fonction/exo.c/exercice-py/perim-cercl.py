import math

def perimetre_cercle(rayon):
    """
    Calcule le périmètre (circonférence) d'un cercle
    Args:
        rayon (float): Rayon du cercle en unités
    Returns:
        float: Périmètre calculé
    Lève:
        TypeError: Si le rayon n'est pas un nombre
        ValueError: Si le rayon est négatif ou nul
    """
    if not isinstance(rayon, (int, float)):
        raise TypeError("Le rayon doit être un nombre")
    if rayon <= 0:
        raise ValueError("Le rayon doit être strictement positif")
    return 2 * math.pi * rayon

# Exemple d'utilisation
try:

    r = float(input("Entrez le rayon du cercle : "))
    print(f"Périmètre : {perimetre_cercle(r):.2f} unités")
except ValueError as e:
    print(f"Erreur de valeur : {e}")
except TypeError as e:
    print(f"Erreur de type : {e}")
except Exception as e:
    print(f"Erreur inattendue : {e}")