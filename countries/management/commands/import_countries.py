import requests
from django.core.management.base import BaseCommand
from countries.models import Country

class Command(BaseCommand):
    help = 'Importation des pays depuis l\'API REST Countries'

    def handle(self, *args, **options):
        self.stdout.write("Début de l'importation...")
        
        # L'URL imposée par l'exercice
        url = "https://restcountries.com/v3.1/all?fields=name,cca2,cca3,capital,region,subregion,population,area,flags,currencies"
        
        try:
            response = requests.get(url)
            response.raise_for_status() # Vérifie si la requête a réussi
            data = response.json()

            for item in data:
                # Extraction avec sécurité (get) pour éviter les erreurs si un champ manque
                cca3 = item.get('cca3')
                name = item.get('name', {}).get('common', 'N/A')
                # On prend la première capitale de la liste
                capitals_list = item.get('capital', [])
                capital = capitals_list[0] if capitals_list else "N/A"
                
                # On utilise update_or_create pour remplir l'Etape 4 (pas de doublons)
                Country.objects.update_or_create(
                    cca3=cca3,
                    defaults={
                        'name_common': name,
                        'capital': capital,
                        'region': item.get('region', 'Unknown'),
                        'subregion': item.get('subregion', 'Unknown'),
                        'population': item.get('population', 0),
                        'area': item.get('area', 0.0),
                        'flag_url': item.get('flags', {}).get('png', ''),
                    }
                )
            
            self.stdout.write(self.style.SUCCESS(f"Import terminé ! {len(data)} pays en base."))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erreur lors de l'import : {e}"))