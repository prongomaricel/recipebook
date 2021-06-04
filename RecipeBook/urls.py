from django.conf.urls import url
from RecipeBookApp import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.RecipeBook, name='RecipeBook'),
    url(r'^RecipeBookApp/(\d+)/$', views.ViewList, name='viewlist'),
    url(r'^RecipeBookApp/newlist_url$', views.NewList, name='newlist'),
    url(r'^RecipeBookApp/(\d+)/addDish$', views.AddDish, name='addDish'),
    url('admin/', admin.site.urls),
]