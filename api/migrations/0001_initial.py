# Generated by Django 5.1 on 2024-08-26 18:38

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('effect', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Abilities',
            },
        ),
        migrations.CreateModel(
            name='EggGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EvolutionTrigger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('verbose_name', models.TextField(default='')),
                ('parameter', models.CharField(default='Level', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GrowthRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('latex_formula', models.TextField()),
                ('python_formula', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonShape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('awesome_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonSpecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2000)])),
                ('name', models.CharField(max_length=100, unique=True)),
                ('catch_rate', models.SmallIntegerField(default=45, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(255)])),
                ('is_legendary', models.BooleanField(default=False)),
                ('is_mythical', models.BooleanField(default=False)),
                ('is_baby', models.BooleanField(default=False)),
                ('has_gender_differences', models.BooleanField(default=False)),
                ('hatch_cycles', models.PositiveIntegerField(default=15, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(255)])),
                ('base_happiness', models.SmallIntegerField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(255)])),
                ('gender_rate', models.IntegerField(choices=[(-1, 'Genderless'), (0, 'Male'), (8, 'Female'), (4, 'Equal'), (1, 'Sevenmale'), (7, 'Sevenfemale'), (2, 'Threemale'), (6, 'Threefemale')], default=4)),
                ('egg_group1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='egg_group_1', to='api.egggroup')),
                ('egg_group2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='egg_group_2', to='api.egggroup')),
                ('growth_rate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.growthrate')),
                ('habitat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.habitat')),
            ],
            options={
                'verbose_name': 'Pokémon Species',
                'verbose_name_plural': 'Pokémon Species',
            },
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('generation', models.PositiveIntegerField(default=1)),
                ('height', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('dex_entry', models.TextField(default='')),
                ('form_order', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('pokeapi_id', models.PositiveIntegerField(default=1)),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.pokemoncolor')),
                ('shape', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.pokemonshape')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pokemonspecies')),
                ('type1', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='type1_pokemon', to='api.pokemontype')),
                ('type2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='type2_pokemon', to='api.pokemontype')),
            ],
            options={
                'verbose_name': 'Pokémon',
                'verbose_name_plural': 'Pokémon',
            },
        ),
        migrations.CreateModel(
            name='PokemonAbility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_hidden', models.BooleanField(default=False)),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ability')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pokemon')),
            ],
            options={
                'unique_together': {('pokemon', 'ability')},
            },
        ),
        migrations.CreateModel(
            name='PokemonStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(255)])),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pokemon')),
                ('stat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stat')),
            ],
            options={
                'unique_together': {('pokemon', 'stat')},
            },
        ),
    ]
