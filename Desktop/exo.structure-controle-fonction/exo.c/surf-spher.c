#include <stdio.h>
#include <math.h> // Pour M_PI et pow()

#define _USE_MATH_DEFINES // Nécessaire pour certaines implémentations

double calculer_surface_sphere(double rayon) {
    if (rayon <= 0) {
        fprintf(stderr, "Erreur : Le rayon doit être positif\n");
        return -1.0;
    }
    
}

int main() {
    double rayon;
    
    printf("Calcul de la surface d'une sphère\n");
    printf("Entrez le rayon de la sphère : ");
    
    if (scanf("%lf", &rayon) != 1) {
        fprintf(stderr, "Erreur : Saisie invalide\n");
        return 1;
    }
    
    double surface = calculer_surface_sphere(rayon);
    
    if (surface != -1.0) {
        printf("Surface de la sphère : %.2f unités²\n", surface);
        return 0;
    }
    return 1;
}