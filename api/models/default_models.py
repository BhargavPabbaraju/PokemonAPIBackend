from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError



class Stat(models.Model):
    name = models.CharField(max_length = 100,unique = True)
    def get_short_name(self):
        short_names = {'HP':'HP',
                        'Attack':'ATK',
                        'Defense':'DEF',
                        'Special Attack':'SPATK',
                        'Special Defense':'SPDEF',
                        'Speed':'SPD'
                        }
        return short_names[self.name] if self.name in short_names else self.name

    def __str__(self):
        return self.name

class PokemonType(models.Model):
    name = models.CharField(max_length = 100,unique=True)
    def __str__(self):
        return self.name


class PokemonColor(models.Model):
    name = models.CharField(max_length = 100,unique = True)
    def __str__(self):
        return self.name

class EvolutionTrigger(models.Model):
    name = models.CharField(max_length = 100,unique = True)
    verbose_name = models.TextField(default='')
    parameter = models.CharField(max_length = 100,default='Level')
    def __str__(self):
        return self.name

class GrowthRate(models.Model):
    name = models.CharField(max_length = 100,unique = True)
    latex_formula = models.TextField()
    python_formula = models.TextField()

    def __str__(self):
        return self.name

class PokemonShape(models.Model):
    name = models.CharField(max_length = 100,unique = True)
    awesome_name = models.CharField(max_length = 100,unique = True)
    def __str__(self):
        return self.name


class Ability(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    effect = models.TextField()

    class Meta:
        verbose_name_plural = "Abilities"
    
    def __str__(self):
        return self.name


class EggGroup(models.Model):
    name = models.CharField(max_length = 200,unique = True)

    def __str__(self):
        return self.name

class Habitat(models.Model):
    name = models.CharField(max_length=200,unique = True)
    def __str__(self):
        return self.name