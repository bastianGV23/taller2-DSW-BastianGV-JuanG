from django import forms

from apps.rescate.models import perrito

class formServicio(forms.ModelForm):
    class Meta:
        model = perrito
        fields = [
            'nombrePerro',
            'razaP',
            'descripcion',
            'imagen',
            'estado',
        ]


        