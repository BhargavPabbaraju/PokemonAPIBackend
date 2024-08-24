from django.core.management.base import BaseCommand,CommandError

from api.models import Ability

import csv

class Command(BaseCommand):
    help = "Initializes default abilities from file"

    def add_arguments(self,parser):
        parser.add_argument('--file',type=str,default='data/abilities.csv',help="File path for abilities")

     

    def handle(self,*args,**options):
        file_path = options['file']
        with open(file_path,mode='r',newline='') as file:
            csv_reader = csv.DictReader(file)

            for ability in csv_reader:
                ability_obj = Ability(name=ability['name'],effect=ability['effect'])
                ability_obj.save()
            
        
        self.stdout.write(
            self.style.SUCCESS('Successfully initialized abilities')
        )
    