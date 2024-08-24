from django.core.management.base import BaseCommand, CommandError

from api.models import PokemonType


DEFAULT_TYPES = [
    'Bug',
    'Dark',
    'Dragon',
    'Electric',
    'Fairy',
    'Fighting',
    'Fire',
    'Flying',
    'Ghost',
    'Grass',
    'Ground',
    'Ice',
    'Normal',
    'Poison',
    'Psychic',
    'Rock',
    'Steel',
    'Water',
]

class Command(BaseCommand):
    help = "Creates records for default Pokemon types"

    def handle(self, *args, **options):
        for type_name in DEFAULT_TYPES:
            try:
                type_obj = PokemonType(name = type_name)
            except Exception as e:
                raise CommandError(e)
            
            type_obj.save()
            self.stdout.write(
                self.style.SUCCESS('Successfully initialized default type %s'%type_name)
            )
