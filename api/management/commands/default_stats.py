from django.core.management.base import BaseCommand, CommandError
from api.models import Stat

DEFAULT_STATS = [
    'HP',
    'Attack',
    'Defense',
    'Special Attack',
    'Special Defense',
    'Speed',
    
]


class Command(BaseCommand):
    help = "Initializes default Pokemon stats"

    def handle(self,*args,**options):
        for stat in DEFAULT_STATS:
            stat_obj = Stat(name = stat)
            stat_obj.save()
        
        self.stdout.write(
            self.style.SUCCESS('Successfully initialized default stats')
        )