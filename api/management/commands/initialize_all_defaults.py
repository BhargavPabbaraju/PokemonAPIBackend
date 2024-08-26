
from django.core.management.base import BaseCommand,CommandError
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Initializes default Pokemon types,shapes,colors and growth rates'

    def handle(self,*args,**kwargs):
        commands = [

            'default_growth_rates',
            'default_types',
            'default_pokemon_shapes',
            'default_pokemon_colors',
            'default_egg_groups',
            'default_stats',
            'default_abilities',
            'default_habitats',
            'initialize_pokemon_species',
            'initialize_pokemon',
            
        ]

        for command in commands:
            self.stdout.write(f"Running {command}...")
            call_command(command)
            self.stdout.write(self.style.SUCCESS(f"{command} executed successfully"))
        
        

        