import requests
from django.core.management.base import BaseCommand
from countries.models import Country

class Command(BaseCommand):
    help = 'Importation des pays depuis l\'API REST Countries'

    def handle(self, *args, **options):
        self.stdout.write("Début de l'importation...")
        
        # Lien pour récupérer les données
        url = "https://restcountries.com/v3.1/all?fields=name,cca2,cca3,capital,region,subregion,population,area,flags,currencies"
        
        try:
            response = requests.get(url)
            response.raise_for_status() 
            data = response.json()

            for item in data:
              
                cca3 = item.get('cca3')
                name = item.get('name', {}).get('common', 'N/A')
               
                capitals_list = item.get('capital', [])
                capital = capitals_list[0] if capitals_list else "N/A"
                
               
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