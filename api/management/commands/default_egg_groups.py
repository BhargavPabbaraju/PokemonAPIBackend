from django.core.management.base import BaseCommand
from api.models import EggGroup

DEFAULT_EGG_GROUPS = [
    'Monster',
    'Water 1',
    'Bug',
    'Flying',
    'Field',
    'Fairy',
    'Grass',
    'Human-Like',
    'Water 3',
    'Mineral',
    'Amorphous',
    'Water 2',
    'Ditto',
    'Dragon',
    'Undiscovered',
]

class Command(BaseCommand):
    help = "Initializes default Pokemon egg groups"

    def handle(self,*args,**options):
        for egg_group in DEFAULT_EGG_GROUPS:
            EggGroup(name=egg_group).save()
        
        self.stdout.write(
            self.style.SUCCESS('Successfully initialized %d egg groups' % len(DEFAULT_EGG_GROUPS))
        )
