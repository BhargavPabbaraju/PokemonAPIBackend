from django.core.management.base import BaseCommand , CommandError

from api.models import PokemonShape

DEFAULT_SHAPES = [
    ('Ball', 'Pomaceous'),
    ('Squiggle', 'Caudal'),
    ('Fish', 'Ichthyic'),
    ('Arms', 'Brachial'),
    ('Blob', 'Alvine'),
    ('Upright', 'Sciurine'),
    ('Legs', 'Crural'),
    ('Quadruped', 'Mensal'),
    ('Wings', 'Alar'),
    ('Tentacles', 'Cilial'),
    ('Heads', 'Polycephalic'),
    ('Humanoid', 'Anthropomorphic'),
    ('Bug wings', 'Lepidopterous'),
    ('Armor', 'Chitinous'),
]



class Command(BaseCommand):
    help = "Initializes default pokemon shapes"

    def handle(self,*args,**options):
        for shape in DEFAULT_SHAPES:
            try:
                shape_obj = PokemonShape(name = shape[0],awesome_name=shape[1])
            except Exception as e:
                raise CommandError(e)
            shape_obj.save()
        
        self.stdout.write(
            self.style.SUCCESS("Successfully initialized %d shapes"%len(DEFAULT_SHAPES))
        )