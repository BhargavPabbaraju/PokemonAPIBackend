from django.core.management.base import BaseCommand,CommandError

from api.models import EggGroup, PokemonSpecies
import json

FILE_PATH = 'data/species/species_egg_group.json'

class Command(BaseCommand):
    help = 'Initializes egg groups of pokemon species'

    def handle(self,*args,**options):
        egg_groups = dict()
        try:
            with open(FILE_PATH,'r') as f:
                egg_groups = json.load(f)
        except FileNotFoundError:
            raise CommandError('File does not exist')
        
        count = 0

        
        for egg_group in egg_groups:
            egg_group_obj = EggGroup.objects.get(name=egg_group)
            for pokemon in egg_groups[egg_group]:
                try:
                    species_obj = PokemonSpecies.objects.get(name=pokemon['pokemon'])
                    if pokemon['number'] == 1:
                        species_obj.egg_group1 = egg_group_obj
                    else:
                        species_obj.egg_group2 = egg_group_obj
                    
                    species_obj.save()
                    count+=1
                except PokemonSpecies.DoesNotExist:
                    print(species)
                
                
        
        
        self.stdout.write(
            self.style.SUCCESS(
                'Successfully set the growth rates of %d species' % count
            )
        )
