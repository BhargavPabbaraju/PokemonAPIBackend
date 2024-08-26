from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

from django.db.models.signals import pre_save
from django.dispatch import receiver




from .default_models import *


class PokemonSpecies(models.Model):
    class Meta:
        verbose_name = 'Pokémon Species'
        verbose_name_plural = 'Pokémon Species'
    
    class GenderRate(models.IntegerChoices):
        GENDERLESS = -1
        MALE = 0
        FEMALE = 8
        EQUAL = 4
        SEVENMALE = 1
        SEVENFEMALE = 7
        THREEMALE = 2
        THREEFEMALE = 6
    
    number = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(2000)],unique=True)
    name = models.CharField(max_length = 100,unique=True)
    
    growth_rate = models.ForeignKey(GrowthRate,on_delete = models.RESTRICT,null=True)
    egg_group1 = models.ForeignKey(to=EggGroup, on_delete = models.RESTRICT, related_name = 'egg_group_1',null=True)
    egg_group2 = models.ForeignKey(to=EggGroup, on_delete = models.RESTRICT,blank=True,null=True, related_name = 'egg_group_2')

    
    habitat = models.ForeignKey(to=Habitat, on_delete=models.RESTRICT,null=True)
    
    catch_rate = models.SmallIntegerField(validators=[MinValueValidator(0),MaxValueValidator(255)],default=45)

    is_legendary = models.BooleanField(default=False)
    is_mythical = models.BooleanField(default=False)
    is_baby = models.BooleanField(default=False)

    has_gender_differences = models.BooleanField(default=False)

    hatch_cycles = models.PositiveIntegerField(validators=[MinValueValidator(5),MaxValueValidator(255)],default=15)

    base_happiness = models.SmallIntegerField(validators=[MinValueValidator(0),MaxValueValidator(255)],default=50)
    
    gender_rate = models.IntegerField(choices = GenderRate,default=GenderRate.EQUAL)

    def __str__(self):
        return self.name



class Pokemon(models.Model):
    


    class Meta:
        verbose_name = 'Pokémon'
        verbose_name_plural = 'Pokémon'

    
    species = models.ForeignKey(to=PokemonSpecies,on_delete=models.CASCADE)
    name = models.CharField(max_length = 255,blank=True)
    title = models.CharField(max_length = 255)
    
    type1 = models.ForeignKey(to=PokemonType, on_delete=models.RESTRICT,related_name = 'type1_pokemon')
    type2 = models.ForeignKey(to=PokemonType, on_delete=models.RESTRICT, blank = True, null = True, related_name = 'type2_pokemon')
    color = models.ForeignKey(to=PokemonColor,on_delete=models.RESTRICT,null=True)
   
    
    generation = models.PositiveIntegerField(default = 1)
    
    
    height = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0.01)])
    weight = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0.01)])
    shape = models.ForeignKey(to=PokemonShape,on_delete=models.RESTRICT,null=True)
    dex_entry = models.TextField(default = '')
    form_order = models.SmallIntegerField(validators=[MinValueValidator(0)],default=0)
    
    pokeapi_id = models.PositiveIntegerField(default=1)
    
   

    

    def __str__(self):
        return self.name





@receiver(pre_save,sender=Pokemon)
def set_default_name(sender,instance,**kwargs):
    
    if not instance.name:
        instance.name = instance.species.name




class PokemonStat(models.Model):
    pokemon = models.ForeignKey(to=Pokemon, on_delete=models.CASCADE)
    stat = models.ForeignKey(to=Stat, on_delete=models.CASCADE)
    value = models.SmallIntegerField(validators =[MinValueValidator(0),MaxValueValidator(255)],default=0)
    
    class Meta:
        unique_together = ('pokemon','stat')
    
    def __str__(self):
        return f"{self.pokemon.name} - {self.stat.name}: {self.value}"

    

class PokemonAbility(models.Model):
    pokemon = models.ForeignKey(to=Pokemon, on_delete=models.CASCADE)
    ability = models.ForeignKey(to=Ability,on_delete=models.CASCADE)
    is_hidden = models.BooleanField(default = False)

    class Meta:
        unique_together = ('pokemon','ability')
    
    def __str__(self):
        return ("Hidden Ability: " if self.is_hidden else "") + f"{self.ability.name}"
    
    
