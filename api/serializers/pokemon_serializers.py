
from rest_framework import serializers
from api.models.pokemon_models import Pokemon,PokemonSpecies
from api.models.default_models import *
from django.urls import reverse



class PokemonSpeciesSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pokemon-species-detail')
    class Meta:
        model = PokemonSpecies
        fields = ['url','number','name']


class PokemonListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pokemon-detail')
    number = serializers.IntegerField(source='species.number',read_only=True)
    class Meta:
        model = Pokemon
        fields = ['url','number','name']



class PokemonDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pokemon-detail')
    species = serializers.SerializerMethodField()
    type1 = serializers.SerializerMethodField()
    type2 = serializers.SerializerMethodField()


    color = serializers.SerializerMethodField()
    shape = serializers.SerializerMethodField()

    growth_rate = serializers.SerializerMethodField()

    egg_group1 = serializers.SerializerMethodField()
    egg_group2 = serializers.SerializerMethodField()

    pokeapi_id = serializers.SerializerMethodField()
    
    class Meta:
        model = Pokemon
        fields = [
            'url',
            'species',
            'name',
            'title',
            'generation',
            'type1',
            'type2',
            'height',
            'weight',
            'gender',
            'color',
            'shape',
            'growth_rate',
            'egg_group1',
            'egg_group2',
            'dex_entry',
            'pokeapi_id',
            

        ]

    def get_related_field(self,obj,field_name,view_name):
        field_instance = getattr(obj,field_name)
        if field_instance:
            return {
                'name': field_instance.name,
                'url': self.context['request'].build_absolute_uri(
                    reverse(view_name+'-detail', args=[field_instance.pk])
                ),

            }
        return None

    def get_species(self,obj):
        return self.get_related_field(obj, 'species', 'pokemon-species')

    def get_type1(self,obj):
        return self.get_related_field(obj,'type1','type')
    
    def get_type2(self,obj):
        return self.get_related_field(obj,'type2','type')
    
    def get_shape(self,obj):
        return self.get_related_field(obj,'shape','pokemon-shape')
    
    def get_color(self,obj):
        return self.get_related_field(obj,'color','pokemon-color')
    
    def get_growth_rate(self,obj):
        return self.get_related_field(obj,'growth_rate','growth-rate')
    
    def get_egg_group1(self,obj):
        return self.get_related_field(obj,'egg_group_1','egg-group')
    
    def get_egg_group2(self,obj):
        return self.get_related_field(obj,'egg_group_2','egg-group')
    
    def get_pokeapi_id(self,obj):
        field_instance = getattr(obj,'pokeapi_id')
        if field_instance:
            return {
                'id': field_instance,
                'url': f'https://pokeapi.co/api/v2/pokemon/{field_instance}',
                

            }
        return None