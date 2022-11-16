from django import forms
from estudo_forms.models import SEXO_CHOICES, Aluno


class AlunoForm(forms.ModelForm):
    
    class Meta:
        model = Aluno
        fields = ['nome','email','data_nascimento','sexo','curso','minicursos']

        widgets = {
            'minicursos': forms.CheckboxSelectMultiple(),
            'sexo':forms.RadioSelect(),
            'data_nascimento':forms.TimeInput(attrs={"type": "date"}),
        }
