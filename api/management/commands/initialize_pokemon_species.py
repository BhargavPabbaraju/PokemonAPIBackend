from django.core.management.base import BaseCommand
from django.core.management import call_command
from api.models import PokemonSpecies

import csv

class Command(BaseCommand):
    help = 'Initializes current pokemon species'

    def add_arguments(self,parser):
        parser.add_argument('--file',type=str,default='data/species/species.csv',help="File path for species")
    
    def handle(self,*args,**options):
        file_path = options['file']
        count = 0
        with open(file_path,'r') as file:
            csv_reader = csv.DictReader(file)

            for species in csv_reader:
                species_obj = PokemonSpecies(
                    number = int(species['number']),
                    name = species['name'],
                    catch_rate = int(species['catch_rate']),
                    hatch_cycles = int(species['hatch_cycles']),
                    base_happiness = int(species['base_happiness']),
                    has_gender_differences = eval(species['has_gender_differences']),
                    is_legendary = eval(species['is_legendary']),
                    is_mythical = eval(species['is_mythical']),
                    is_baby = eval(species['is_baby']),
                    gender_rate = int(species['gender_rate']),
                    )
                species_obj.save()
                count+=1
        
        call_command('initialize_species_growth_rates')
        call_command('initialize_species_habitats')
        call_command('initialize_species_egg_groups')
        
        
            
        self.stdout.write(
            self.style.SUCCESS(
                'Successfully initialized %d species' % (count)
            )
        )