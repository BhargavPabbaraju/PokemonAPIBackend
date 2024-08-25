from django.core.management import BaseCommand,CommandError
from api.models import GrowthRate, PokemonSpecies
import json

FILE_PATH = 'data/species/species_growth_rates.json'

class Command(BaseCommand):
    help = 'Initializes the growth rates of pokemon species'

    def handle(self,*args,**options):
        growth_rates = dict()
        try:
            with open(FILE_PATH,'r') as f:
                growth_rates = json.load(f)
        except FileNotFoundError:
            raise CommandError('File does not exist')
        
        count = 0
        for growth_rate in growth_rates:
            growth_rate_obj = GrowthRate.objects.get(name=growth_rate)
            for species in growth_rates[growth_rate]:
                species_obj = PokemonSpecies.objects.get(name=species)
                species_obj.growth_rate = growth_rate_obj
                species_obj.save()
                count+=1
        
        self.stdout.write(
            self.style.SUCCESS(
                'Successfully set the growth rates of %d species' % count
            )
        )
