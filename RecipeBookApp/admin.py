from django.contrib import admin
from .models import Creator, Dish, Recipe, Comments

admin.site.register(Creator)
admin.site.register(Dish)
admin.site.register(Recipe)
admin.site.register(Comments)