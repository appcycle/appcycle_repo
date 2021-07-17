from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import ListView

from apps.criarusuario.forms import SignUpForm

from apps.cadastro.models import CadastroCliente


@login_required
def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            qtde_usuarios = CadastroCliente.objects.first().qtde_usuarios
            if (get_user_model().objects.all().count() <= qtde_usuarios):
                form.save()
              #  username = form.cleaned_data.get('username')
              #  raw_password = form.cleaned_data.get('password1')
             #  user = authenticate(username=username, password=raw_password)
    return render(request, 'criarusuario/signup.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ListUsuariosRegistrados(ListView):
    paginate_by = 10
    model = get_user_model()
    ordering = ['-id']
