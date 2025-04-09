def calculer_perimetre_rectangle(longueur, largeur):
    """
    Calcule le périmètre d'un rectangle
    Args:
        longueur (float): Longueur du rectangle
        largeur (float): Largeur du rectangle
    Returns:
        float: Périmètre calculé
    """
    if not (isinstance(longueur, (int, float)) and isinstance(largeur, (int, float))):
        raise TypeError("Les dimensions doivent être des nombres")
    if longueur <= 0 or largeur <= 0:
        raise ValueError("Les dimensions doivent être positives")
    return 2 * (longueur + largeur)

# Programme principal
try:
    # Saisie des dimensions
    l = float(input("Entrez la longueur du rectangle (en mètres) : "))
    w = float(input("Entrez la largeur du rectangle (en mètres) : "))
    
    # Calcul et affichage
    perimetre = calculer_perimetre_rectangle(l, w)
    print(f"\nPérimètre du rectangle : {perimetre:.2f} m")

except ValueError as e:
    print(f"\nErreur : {e}")
except TypeError as e:
    print(f"\nErreur de type : {e}")
except Exception as e:
    print(f"\nErreur inattendue : {e}")