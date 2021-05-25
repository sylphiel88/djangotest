from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('projects', views.projects, name='projects'),
    path('werdegang', views.werdegang, name='werdegang'),
    path('werdegang/schule', views.schule, name='schule'),
    path('werdegang/hobbies', views.hobbies, name='hobbies'),
    path('aquarium', views.aqindex, name='aquarium'),
    path('aquarium/aqbewe', views.aqbewe, name='aqbewe'),
    path('aquarium/aquarium1', views.aquarium1, name='aquarium1'),
    path('aquarium/aquarium2', views.aquarium2, name='aquarium2'),
    path('aquarium/aquarium3', views.aquarium3, name='aquarium3'),
    path('aquarium/technik', views.technik, name='technik'),
    path('aquarium/gallery', views.gallery, name='gallery')
]