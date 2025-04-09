def calculer_surface_rectangle(longueur, largeur):
    """
    Calcule la surface d'un rectangle
    Args:
        longueur (float): Longueur du rectangle
        largeur (float): Largeur du rectangle
    Returns:
        float: Surface calculée
    """
    if not (isinstance(longueur, (int, float)) and isinstance(largeur, (int, float))):
        raise TypeError("Les dimensions doivent être des nombres")
    if longueur <= 0 or largeur <= 0:
        raise ValueError("Les dimensions doivent être positives")
    return longueur * largeur

# Programme principal
try:
    # Saisie des dimensions
    l = float(input("Entrez la longueur du rectangle (en mètres) : "))
    w = float(input("Entrez la largeur du rectangle (en mètres) : "))
    
    # Calcul et affichage
    surface = calculer_surface_rectangle(l, w)
    print(f"\nSurface du rectangle : {surface:.2f} m²")

except ValueError as e:
    print(f"\nErreur : Saisie invalide - {e}")
except TypeError as e:
    print(f"\nErreur de type : {e}")
except Exception as e:
    print(f"\nErreur inattendue : {e}")