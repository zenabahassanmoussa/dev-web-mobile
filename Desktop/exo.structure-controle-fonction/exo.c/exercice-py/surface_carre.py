def surface_carre(cote):
    """
    Calcule la surface d'un carré.

    :param cote: Longueur du côté du carré (nombre positif).
    :return: La surface du carré.
    """
    return cote ** 2


cote = int(input("Entrez le coté du carré: "))
print(f"La surface du carré de côté {cote} est : {surface_carre(cote)}")