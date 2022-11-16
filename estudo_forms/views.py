from django.shortcuts import render

from estudo_forms.forms import AlunoForm

# Create your views here.
def form_aluno(request):
    form = AlunoForm
    return render(request, 'form.html',{'form':form})