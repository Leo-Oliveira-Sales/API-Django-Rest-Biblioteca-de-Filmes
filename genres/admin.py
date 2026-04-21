from django.contrib import admin
from genres.models import Genre


# Registando o models Genre no admin do Django
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
