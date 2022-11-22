from django.contrib import messages
from django.shortcuts import redirect, render
from estudo_forms.forms import AlunoForm

# Create your views here.
def form_aluno(request):
    form = AlunoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid:
            aluno = form.save(commit = False)
            aluno.save()
            messages.success(request, 'Cadastro realizado com sucesso!')        
            return redirect('form-aluno')
        else:
            messages.error(request, 'Erro ao realizar cadastro.')
            return redirect('form-aluno')
    else:
        form = AlunoForm()

    return render(request, 'form.html',{'form':form})