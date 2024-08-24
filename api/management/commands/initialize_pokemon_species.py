from django.core.management.base import BaseCommand

from api.models import PokemonSpecies

import csv

class Command(BaseCommand):
    help = 'Initializes current pokemon species'

    def add_arguments(self,parser):
        parser.add_argument('--file',type=str,default='data/species.csv',help="File path for species")
    
    def handle(self,*args,**options):
        file_path = options['file']
        count = 0
        with open(file_path,'r') as file:
            csv_reader = csv.DictReader(file)

            for species in csv_reader:
                species_obj = PokemonSpecies(number=species['number'],name=species['name'])
                species_obj.save()
                count+=1
            
        self.stdout.write(
            self.style.SUCCESS(
                'Successfully initialized %d species' % (count)
            )
        )