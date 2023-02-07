from django import forms


class SpellsFormulario(forms.Form):

    nombre = forms.CharField()
    nivel = forms.IntegerField()
    escuela = forms.CharField()

class MonstersFormulario(forms.Form):

    nombre = forms.CharField()
    nivel_desafio = forms.IntegerField()
    terreno = forms.CharField()

class WeaponsFormulario(forms.Form):

    nombre = forms.CharField()
    tipo = forms.CharField()
    versatil = forms.BooleanField()


