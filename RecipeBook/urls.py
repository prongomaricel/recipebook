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


    url(r'^(\d+)/addDish$', views.AddDish, name='addDish'),

    url(r'^(\d+)/Recipe$', views.ViewRecipe, name='ViewRecipe'),



    url(r'^(\d+)/addDish/addRecipe$', views.AddRecipe, name='AddRecipe'),



    url(r'^(\d+)/s$', views.ViewList2, name='ViewList2'),

    url(r'^(\d+)/profile$', views.Profile, name='Profile'),



    url(r'^(\d+)/addDish/addRecipe1$', views.AddRecipe1, name='AddRecipe1'),

    url('admin/', admin.site.urls),
]