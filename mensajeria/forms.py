from django import forms
from .models import FilesExcel, FotoPerfil

class SubirArchivo(forms.ModelForm):
	class Meta:
		model = FilesExcel
		fields = ('filename', 'docfile')

class SubirFoto(forms.ModelForm):
    class Meta:
        model = FotoPerfil
        fields = ('name', 'foto')
    