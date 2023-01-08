from django import forms
from estudo_forms.models import SEXO_CHOICES, Aluno, Minicurso


class AlunoForm(forms.ModelForm):
    
    class Meta:
        model = Aluno
        fields = ['nome','email','data_nascimento','sexo','curso','minicursos']

        widgets = {
            'nome':forms.TextInput(attrs={'placeholder':'Fulano da Silva Cicrano'}),
            'email':forms.TextInput(attrs={'placeholder':'fulano@tarara.com','required':True,'type':'email'}),
            'data_nascimento':forms.TimeInput(attrs={"type": "date"}),
            'minicursos': forms.CheckboxSelectMultiple(),
            'sexo':forms.RadioSelect(),
            
        }
