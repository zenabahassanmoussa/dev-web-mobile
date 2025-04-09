def calculer_perimetre_carre(cote):
    """
    Calcule le périmètre d'un carré
    Args:
        cote (float): Longueur du côté en unités
    Returns:
        float: Périmètre du carré
    """
    if not isinstance(cote, (int, float)):
        raise TypeError("Le côté doit être un nombre")
    if cote <= 0:
        raise ValueError("Le côté doit être positif")
    return 4 * cote

# Programme principal
try:
    # Demande de saisie utilisateur
    saisie = input("Entrez la longueur du côté du carré (en cm) : ")
    cote = float(saisie)
    
    # Calcul et affichage
    perimetre = calculer_perimetre_carre(cote)
    print(f"Périmètre du carré : {perimetre:.2f} cm")
    
except ValueError as e:
    print(f"Erreur : {e} - Veuillez entrer un nombre valide")
except TypeError as e:
    print(f"Erreur de type : {e}")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")