from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.FloatField()
    date_creation = models.DateField()

    def __str__(self):
        return self.nom