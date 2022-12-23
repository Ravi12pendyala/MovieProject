from django.contrib import admin
from MovieApp.models import Movies

#Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    list_display=['releasedate','moviename', 'hero','heroin','rating'];

admin.site.register(Movies,MoviesAdmin);