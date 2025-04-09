#include <stdio.h>
#include <math.h>   // Pour pow() et M_PI
#define _USE_MATH_DEFINES // Définition nécessaire pour M_PI

double calculer_volume_sphere(double rayon) {
    if (rayon <= 0) {
        fprintf(stderr, "Erreur : Le rayon doit être positif\n");
        return -1.0;
    }
    
}

int main() {
    double rayon;
    
    printf("Calcul du volume d'une sphère\n");
    printf("Entrez le rayon de la sphère : ");
    
    // Vérification de la saisie
    if (scanf("%lf", &rayon) != 1) {
        fprintf(stderr, "Erreur : Saisie invalide\n");
        return 1;
    }
    
    double volume = calculer_volume_sphere(rayon);
    
    if (volume != -1.0) {
        printf("Volume de la sphère : %.2f unités³\n", volume);
        return 0;
    }
    return 1;
}