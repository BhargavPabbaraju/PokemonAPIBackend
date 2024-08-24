from django.core.management.base import BaseCommand,CommandError

from api.models import PokemonColor

DEFAULT_COLORS = [
    'Black',
    'Blue',
    'Brown',
    'Gray',
    'Green',
    'Pink',
    'Purple',
    'Red',
    'White',
    'Yellow'
]

class Command(BaseCommand):
    help = "Initializes default Pokemon colors"

    def handle(self,*args,**options):
        for color in DEFAULT_COLORS:
            try:
                color_obj = PokemonColor(name = color)
            except Exception as e:
                raise CommandError(e)
            
            color_obj.save()
        
        self.stdout.write(
            self.style.SUCCESS("Successfully initialized %d colors"%(len(DEFAULT_COLORS)))
        )