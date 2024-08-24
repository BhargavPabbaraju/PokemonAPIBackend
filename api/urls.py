from django.urls import include,path 
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('type',views.PokemonTypeViewSet,basename='type')
router.register('ability',views.AbilityViewSet,basename='ability')
router.register('stat',views.StatViewSet,basename='stat')
router.register('pokemon-shape',views.PokemonShapeViewSet,basename='pokemon-shape')
router.register('growth-rate',views.GrowthRateViewSet,basename='growth-rate')
router.register('pokemon-color',views.PokemonColorViewSet,basename='pokemon-color')
router.register('egg-group',views.EggGroupViewSet,basename='egg-group')
router.register('pokemon-species',views.PokemonSpeciesViewSet,basename='pokemon-species')
router.register('pokemon',views.PokemonViewSet,basename='pokemon')




urlpatterns = [
path('',include(router.urls)),

]