from django.urls import path
from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]

register.filter('index', index)
 
from . import views
app_name = 'logs'
 
urlpatterns = [
	path('', views.marketplace_, name='marketplace_'),
    path('bye/', views.bye, name='bye'),
    path('auth/', views.auth, name='auth'),
    path('current/', views.currentNFT, name="current"),
    path('sole/', views.sole, name="sole")
]