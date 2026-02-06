from django.db import models

class Country(models.Model):
    # 1. L'Identifiant Unique (Clé Primaire)
    cca3 = models.CharField(max_length=3, primary_key=True)
    
    # 2. Les informations textuelles
    name_common = models.CharField(max_length=255)
    capital = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100, blank=True, null=True) 
    
    # 3. Les données numériques (pour les stats)
    population = models.BigIntegerField() # Utilise BigIntegerField car certains pays ont bcp d'habitants !
    area = models.FloatField()
    
    # 4. L'image
    flag_url = models.URLField(max_length=500)
    
    # 5. Monnaies
    currency_code = models.CharField(max_length=10, blank=True, null=True)
    currency_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name_common