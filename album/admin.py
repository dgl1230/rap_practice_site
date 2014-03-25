from django.contrib import admin
from album.models import Album, Rapper

class AlbumAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ('name', 'rapper', 'coast')
	search_fields = ['name']

class RapperAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Album, AlbumAdmin)
admin.site.register(Rapper, RapperAdmin)