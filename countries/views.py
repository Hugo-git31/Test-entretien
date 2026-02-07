from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator
from .models import Country

# LISTE DES PAYS
def country_list(request):
    query = request.GET.get('q', '')
    region_filter = request.GET.get('region', '')

    countries_list = Country.objects.all()

    if query:
        countries_list = countries_list.filter(name_common__istartswith=query)
    
    if region_filter:
        countries_list = countries_list.filter(region=region_filter)

    countries_list = countries_list.order_by('name_common')

    # Création de pages
    paginator = Paginator(countries_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    all_regions = Country.objects.values_list('region', flat=True).distinct().order_by('region')

    return render(request, 'countries/list.html', {
        'countries': page_obj,
        'query': query,
        'regions': all_regions,
        'region_filter': region_filter
    })

# DÉTAIL D'UN PAYS
def country_detail(request, cca3):
    country = get_object_or_404(Country, cca3=cca3)
    return render(request, 'countries/detail.html', {'country': country})

# STATS
def country_stats(request):
    total = Country.objects.count()
    top_population = Country.objects.order_by('-population')[:10]
    top_area = Country.objects.order_by('-area')[:10]
    regions_count = Country.objects.values('region').annotate(total=Count('cca3')).order_by('-total')

    return render(request, 'countries/stats.html', {
        'total': total,
        'top_population': top_population,
        'top_area': top_area,
        'regions': regions_count,
    })