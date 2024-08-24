from rest_framework import viewsets,permissions
from api.serializers.default_serializers import *
from api.models.default_models import *

class PokemonTypeViewSet(viewsets.ModelViewSet):
    queryset = PokemonType.objects.all().order_by('name')
    serializer_class = PokemonTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AbilityViewSet(viewsets.ModelViewSet):
    queryset = Ability.objects.all().order_by('name')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return AbilityListSerializer
        return AbilityDetailSerializer


class StatViewSet(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatSerializer

class PokemonShapeViewSet(viewsets.ModelViewSet):
    queryset = PokemonShape.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return PokemonShapeListSerializer
        return PokemonShapeDetailSerializer

class GrowthRateViewSet(viewsets.ModelViewSet):
    queryset = GrowthRate.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return GrowthRateListSerializer
        return GrowthRateDetailSerializer

class PokemonColorViewSet(viewsets.ModelViewSet):
    queryset = PokemonColor.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PokemonColorSerializer

class EggGroupViewSet(viewsets.ModelViewSet):
    queryset = EggGroup.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EggGroupSerializer


