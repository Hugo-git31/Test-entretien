from django.db import models

class Country(models.Model):
    # Identifiant Unique (Clé Primaire)
    cca3 = models.CharField(max_length=3, primary_key=True) 
    
    # Informations textuelles
    name_common = models.CharField(max_length=255)
    capital = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100, blank=True, null=True) 
    
    # Données numériques
    population = models.BigIntegerField()
    area = models.FloatField(blank=True, null=True) # <-- AJOUTÉ ICI
    
    # Les drapeaux
    flag_url = models.URLField(max_length=500)
    
    # Les différentes monnaies
    currency_code = models.CharField(max_length=10, blank=True, null=True)
    currency_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name_common