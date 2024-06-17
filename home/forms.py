from django import forms
from home.models import Alumno, Profesor, Especializacion, Curso

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class EspecializacionForm(forms.ModelForm):
    class Meta:
        model = Especializacion
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100, required=True)
