from django.contrib import admin
from .models import Group, Musician, Album

admin.site.register(Musician)
admin.site.register(Group)
admin.site.register(Album)
