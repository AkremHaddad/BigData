class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculer_surface(self):
        return self.longueur * self.largeur

    def calculer_perimetre(self):
        return 2 * (self.longueur + self.largeur)

rect1 = Rectangle(5, 3)
print(f"Surface du rectangle: {rect1.calculer_surface()}")
print(f"Perimetre du rectangle: {rect1.calculer_perimetre()}")


rect1 = Rectangle(7, 4)
print(f"Surface du deuxieme rectangle: {rect1.calculer_surface()}")
print(f"Perimetre du deuxieme rectangle: {rect1.calculer_perimetre()}")


class Voiture:
    def __init__(self, Marque, Couleur):
        self.Marque = Marque
        self.Couleur = Couleur

    def demarer(self):
        return "la voiture " + self.Couleur + " de marque " + self.Marque + " demare"


voiture1 = Voiture("Toyota", "Rouge")
voiture2 = Voiture("Honda", "Bleu")
print(voiture1.demarer())
print(voiture2.demarer())