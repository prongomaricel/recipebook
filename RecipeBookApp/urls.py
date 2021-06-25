from django.conf.urls import url
from RecipeBookApp import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.RecipeBook, name='RecipeBook'),
    url(r'^(\d+)/$', views.ViewList, name='viewlist'),
    url(r'^newlist_url$', views.NewList, name='newlist'),

    url(r'^contact$', views.Contact, name='Contact'),
    url(r'^about$', views.About, name='About'),
    url(r'^home$', views.RecipeBook, name='RecipeBook'),
    url(r'^recipes$', views.Recipes, name='Recipes'),


    
    url(r'^(\d+)/Recipe$', views.ViewList2, name='ViewList2'),
    url(r'^(\d+)/addDish$', views.AddDish, name='addDish'),


    # url(r'^(\d+)/Dishes$', views.Dishes, name='Dishes'),
    # url(r'^(\d+)/Output$', views.Output, name='Output'),


    # url(r'^(\d+)/Dishes$', views.Dishes, name='Dishes'),
    # url(r'^(\d+)/Output$', views.Output, name='Output'),


    url(r'^(\d+)/profile$', views.Profile, name='Profile'),


    url('admin/', admin.site.urls),
]