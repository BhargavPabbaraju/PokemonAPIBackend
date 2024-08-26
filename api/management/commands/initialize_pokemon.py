from django.core.management.base import BaseCommand,CommandError
from api.models import *
import csv

FILE_PATH = 'data/pokemon.csv'
ENCODING = 'Windows-1252'
BATCH_SIZE = 250


def get_stats(pokemon,pokemon_obj=None):
    for stat in Stat.objects.all():
        value = pokemon[stat.name]
        poke_stat = PokemonStat(pokemon=pokemon_obj,stat=stat,value=value)
        #print(poke_stat)
        poke_stat.save()

def get_abilities(pokemon,pokemon_obj=None):
    for ab in ['Ability 1','Ability 2','Hidden Ability']:
        ability = pokemon[ab]
        if ability:
            ability = Ability.objects.get(name = ability)
            is_hidden ='Hidden' in ab
            poke_ability = PokemonAbility(ability=ability,pokemon =pokemon_obj, is_hidden = is_hidden)
            #print(poke_ability)
            poke_ability.save()
        

class Command(BaseCommand):
    help = 'Loads existing pokemon and their forms data into the database'

    
    def handle(self,*args,**options):
        with open(FILE_PATH,encoding=ENCODING,mode='r') as file:
            try:
                csv_reader = csv.DictReader(file)
                count = 1
                for pokemon in csv_reader:
                    #self.stdout.write(str(pokemon))
                    
                    number = int(pokemon['Number'])
                    species = PokemonSpecies.objects.get(number = number)
                    name = pokemon['Form'] if pokemon['Form'] else pokemon['Name']
                    title = pokemon['Title']
                    
                    type1 = PokemonType.objects.get(name = pokemon['Type 1'])
                    type2 = pokemon['Type 2']
                    if type2:
                        type2 = PokemonType.objects.get(name = pokemon['Type 2'])
                    else:
                        type2 = None

                    generation = pokemon['Generation']
                    
                    form_order = int(pokemon['Form Order'])

                    dex_entry = pokemon['Dex Entry']
                    height = float(pokemon['Height'])
                    weight = float(pokemon['Weight'])
                    
                    shape = PokemonShape.objects.get(name=pokemon['Shape'])
                    color = PokemonColor.objects.get(name = pokemon['Color'])
                    
                    pokeapi_id = pokemon['PokeApi Id']

                    pokemon_obj = Pokemon(
                        name = name,
                        species = species,
                        title = title,
                        type1 = type1,
                        type2 = type2,
                        color = color,
                        generation = generation,
                        height = height,
                        weight = weight,
                        shape = shape,
                        dex_entry = dex_entry,
                        form_order = form_order,
                        pokeapi_id = pokeapi_id,
                    )

                    pokemon_obj.save()
                    
                    get_stats(pokemon,pokemon_obj)

                    get_abilities(pokemon,pokemon_obj)
                    if count % BATCH_SIZE == 0:
                        self.stdout.write(self.style.SUCCESS('Successfully initialized %d pokemon')%count)
                    count += 1
                    
            except Exception as e:
                self.stdout.write(self.style.ERROR(str(pokemon)))
                self.stdout.write(self.style.ERROR(str(e)))

            