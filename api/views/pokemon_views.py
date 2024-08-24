from rest_framework import viewsets,permissions
from api.models import Pokemon

from api.serializers.pokemon_serializers import *


class PokemonSpeciesViewSet(viewsets.ModelViewSet):
    queryset = PokemonSpecies.objects.all().order_by('number')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PokemonSpeciesSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all().order_by('species__number')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

    def get_serializer_class(self):
        if self.action == 'list':
            return PokemonListSerializer
        return PokemonDetailSerializer