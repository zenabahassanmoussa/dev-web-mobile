import math

def calculer_volume_sphere(rayon):
    """
    Calcule le volume d'une sphère
    Args:
        rayon (float): Rayon de la sphère
    Returns:
        float: Volume calculé
    Lève:
        ValueError: Si le rayon est négatif ou nul
    """
    if rayon <= 0:
        raise ValueError("Le rayon doit être strictement positif")
    return (4/3) * math.pi * (rayon ** 3)

# Programme principal
try:
    saisie = input("Entrez le rayon de la sphère (en mètres) : ")
    r = float(saisie)
    
    volume = calculer_volume_sphere(r)
    print(f"Volume de la sphère : {volume:.2f} m³")

except ValueError as e:
    if "could not convert" in str(e):
        print("Erreur : Veuillez entrer un nombre valide")
    else:
        print(f"Erreur : {e}")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")