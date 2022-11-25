from django.urls import path 
from .views import *

urlpatterns = [
    path('', redirect_form_aluno, name='root'),
    path('/forms', form_aluno, name='form-aluno')
]
