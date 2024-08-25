from django.core.management import BaseCommand,CommandError
from api.models import Habitat, PokemonSpecies
import json

FILE_PATH = 'data/species/species_habitat.json'

class Command(BaseCommand):
    help = 'Initializes the habitats of pokemon species'

    def handle(self,*args,**options):
        habitats = dict()
        try:
            with open(FILE_PATH,'r') as f:
                habitats = json.load(f)
        except FileNotFoundError:
            raise CommandError('File does not exist')
        
        count = 0
        for habitat in habitats:
            habitat_obj = Habitat.objects.get(name=habitat)
            for species in habitats[habitat]:
                species_obj = PokemonSpecies.objects.get(name=species)
                species_obj.habitat = habitat_obj
                species_obj.save()
                count+=1
        
        self.stdout.write(
            self.style.SUCCESS(
                'Successfully set the habitats of %d species' % count
            )
        )
