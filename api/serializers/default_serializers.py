from rest_framework import serializers
from api.models import *
from django.urls import reverse



def get_species_list(instance,field,obj):
    species_list = []
    queryset = PokemonSpecies.objects.filter(**{field:obj})
    for species in queryset:
        species_list.append(
            {
            'name': species.name,
            'url': instance.context['request'].build_absolute_uri(
            reverse('pokemon-species-detail', args=[species.pk])
            ),
            })

    return species_list



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
    pokemon = serializers.SerializerMethodField()
    class Meta:
        model = Ability
        fields = ['url','name','effect','pokemon']
    
    def get_pokemon(self,obj):
        pokemon_list = []
        for pokemon_ability in PokemonAbility.objects.filter(ability = obj):
            pokemon = pokemon_ability.pokemon
            pokemon_list.append(
                {'url':self.context['request'].build_absolute_uri(
                    reverse('pokemon-detail',args=[pokemon.pk]),
                ),
                'name':pokemon.name}
            )
        return pokemon_list


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
    pokemon = serializers.SerializerMethodField()
    class Meta:
        model = PokemonShape
        fields = ['url','name','awesome_name','pokemon']
    
    def get_pokemon(self,obj):
        pokemon_list = []
        for pokemon in Pokemon.objects.filter(shape = obj):
            pokemon_list.append(
                {'url':self.context['request'].build_absolute_uri(
                    reverse('pokemon-detail',args=[pokemon.pk]),
                ),
                'name':pokemon.name}
            )
        return pokemon_list

class GrowthRateListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='growth-rate-detail')
    class Meta:
        model = GrowthRate
        fields = ['url','name']
    
class GrowthRateDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='growth-rate-detail')
    pokemon_species = serializers.SerializerMethodField()
    class Meta:
        model = GrowthRate
        fields = ['url','name','latex_formula','python_formula','pokemon_species']
        
    def get_pokemon_species(self,obj):
        return get_species_list(self, 'growth_rate', obj)
    



class PokemonColorListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pokemon-color-detail')
    class Meta:
        model = PokemonColor
        fields = ['url','name']

class PokemonColorDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pokemon-color-detail')
    pokemon = serializers.SerializerMethodField()
    class Meta:
        model = PokemonColor
        fields = ['url','name','pokemon']
    def get_pokemon(self,obj):
        pokemon_list = []
        for pokemon in Pokemon.objects.filter(color = obj):
            pokemon_list.append(
                {'url':self.context['request'].build_absolute_uri(
                    reverse('pokemon-detail',args=[pokemon.pk]),
                ),
                'name':pokemon.name}
            )
        return pokemon_list
    

class EggGroupListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='egg-group-detail')
    class Meta:
        model = EggGroup
        fields = ['url','name']

class EggGroupDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='egg-group-detail')
    pokemon_species = serializers.SerializerMethodField()
    class Meta:
        model = EggGroup
        fields = ['url','name','pokemon_species']
    
    def get_pokemon_species(self,obj):
        return get_species_list(self, 'egg_group1', obj) + get_species_list(self, 'egg_group2', obj)


class HabitatListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='habitat-detail')
    class Meta:
        model = Habitat
        fields = ['url','name']

class HabitatDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='habitat-detail')
    pokemon_species = serializers.SerializerMethodField()
    class Meta:
        model = Habitat
        fields = ['url','name','pokemon_species']
    
    def get_pokemon_species(self,obj):
        return get_species_list(self, 'habitat', obj)