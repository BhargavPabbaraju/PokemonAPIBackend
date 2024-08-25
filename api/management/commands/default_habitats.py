from django.core.management.base import BaseCommand

from api.models import Habitat

DEFAULT_HABITATS=[
    'Cave',
    'Forest',
    'Grassland',
    'Mountain',
    'Rare',
    'Rough Terrain',
    'Sea',
    'Urban',
    "Water's Edge"
]

class Command(BaseCommand):
    help = 'Initializes default Pokemon habitats'

    def handle(self,*args,**options):
        for habitat in DEFAULT_HABITATS:
            habitat_obj = Habitat(name=habitat)
            habitat_obj.save()
        
        self.stdout.write(
            self.style.SUCCESS(
                'Successfully initialized %d habitats' % (len(DEFAULT_HABITATS))
            )
        )
