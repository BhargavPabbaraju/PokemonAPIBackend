from django.contrib import admin

from api.models.pokemon_models import *
from api.models.default_models import Stat
from django import forms



@admin.register(PokemonSpecies)
class PokemonSpeciesAdmin(admin.ModelAdmin):
    ordering = ['number']

class PokemonStatInlineForm(forms.ModelForm):
    class Meta:
        model = PokemonStat
        fields = ['stat','value']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields['stat'].disabled = True
    


class PokemonStatInlineFormSet(forms.BaseInlineFormSet):
    def __init__(self,*args,**kwargs):
        
        #If creating a new Pokemon , populate the formset with all stats
        stats = Stat.objects.all()
        kwargs['initial'] = [{'stat':stat ,'value':100} for stat in stats]

        self.form = PokemonStatInlineForm
       
        super().__init__(*args,**kwargs)
    

    
        
    def save_new(self,form,commit=True):
        form.instance.pokemon = self.instance
        return super().save_new(form,commit = commit)


   
    



class PokemonStatInline(admin.TabularInline):
    model = PokemonStat
    extra = Stat.objects.count() #Populate all existing stats
    can_delete = False #Prevents deleting stat fields
    
    formset = PokemonStatInlineFormSet

    
            

    def get_max_num(self,request,obj=None,**kwargs):
        return Stat.objects.count()
    def get_min_num(self,request,obhj=None,**kwargs):
        return Stat.objects.count()



class PokemonAbilityInline(admin.StackedInline):
    model = PokemonAbility
    extra = 0
    
    def get_max_num(self,request,obj=None,**kwargs):
        return 3
    def get_min_num(self,request,obhj=None,**kwargs):
        return 1


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    ordering=['species__number']
    fieldsets=[
        (
            None,
            {
                "fields":['species','name','title',('type1','type2'),'generation'],
            },
        ),
        (
            'Pokedex Information',
            {   
                "classes":['collapse'],
                "fields":[('height','weight'),'color','gender','shape','growth_rate','dex_entry'],
            }
            
        ),
        (
            "Egg Groups",
            {
                "classes":['collapse'],
                "fields":[('egg_group_1','egg_group_2')],
            }
        )
    ]

    inlines = [PokemonStatInline,PokemonAbilityInline]

    list_display = ['species_number','name']

    def species_number(self,obj):
        return obj.species.number
    
    species_number.short_description = 'number'