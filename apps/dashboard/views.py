from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.projeto.models import Projeto


@login_required
def home(request):
    return render(request, 'dashboard/dashboard.html')

#Sem filtro de usuario
# def home(request):
# resumo_projetos = Projeto.objects.all()
# return render (request, 'dashboard/dashboard.html', {'Proj': resumo_projetos})


@login_required
def changelog(request):
    return render(request, 'dashboard/changelog.html')




