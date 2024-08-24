from rest_framework import serializers
from api.models.default_models import *

class PokemonTypeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='type-detail')
    class Meta:
        model = PokemonType
        fields = ['url','name']

class AbilityListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ability
        fields = ['url','name']
        
class AbilityDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ability
        fields = ['url','name','effect']


class StatSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='stat-detail')
    class Meta:
        model = Stat
        fields = ['url','name']

class PokemonShapeListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pokemon-shape-detail')
    class Meta:
        model = PokemonShape
        fields = ['url','name']

class PokemonShapeDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pokemon-shape-detail')
    class Meta:
        model = PokemonShape
        fields = ['url','name','awesome_name']

class GrowthRateListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='growth-rate-detail')
    class Meta:
        model = GrowthRate
        fields = ['url','name']
    
class GrowthRateDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='growth-rate-detail')
    class Meta:
        model = GrowthRate
        fields = ['url','name','latex_formula','python_formula']


class PokemonColorSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pokemon-color-detail')
    class Meta:
        model = PokemonColor
        fields = ['url','name']

class EggGroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='egg-group-detail')
    class Meta:
        model = EggGroup
        fields = ['url','name']
    