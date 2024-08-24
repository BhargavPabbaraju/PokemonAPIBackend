from django.contrib import admin

from api.models import default_models

@admin.register(default_models.PokemonType)
class PokemonTypeAdmin(admin.ModelAdmin):
    ordering = ['name']

@admin.register(default_models.Stat)
class StatAdmin(admin.ModelAdmin):
    ordering = ['name']

@admin.register(default_models.GrowthRate)
class GrowthRateAdmin(admin.ModelAdmin):
    ordering = ['name']

@admin.register(default_models.PokemonShape)
class PokemonShapeAdmin(admin.ModelAdmin):
    ordering = ['name']

@admin.register(default_models.PokemonColor)
class PokemonColorAdmin(admin.ModelAdmin):
    ordering = ['name']

@admin.register(default_models.EvolutionTrigger)
class EvolutionTriggerAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name','verbose_name']

@admin.register(default_models.Ability)
class AbilityAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name','effect']

@admin.register(default_models.EggGroup)
class EggGroupAdmin(admin.ModelAdmin):
    ordering = ['name']
