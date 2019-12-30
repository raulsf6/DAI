from django import forms
from .models import Group, Musician, Album

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'style', 'creation_date')

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ('group', 'name', 'birthday', 'main_instrument', 'birthplace_latitude', 'birthplace_longitude')

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('group', 'title', 'distributor', 'release_Date')
