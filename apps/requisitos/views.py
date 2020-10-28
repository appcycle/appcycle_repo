from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from apps.requisitos.forms import CadastrarRequisitos
from apps.requisitos.models import Requisito
from apps.projeto.models import Projeto


@method_decorator(login_required, name='dispatch')
class RequisitoCreate(CreateView):
    model = Requisito
    form_class = CadastrarRequisitos

    def get_form_kwargs(self):
        kwargs = super(RequisitoCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(RequisitoCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class RequisitoList(ListView):
    paginate_by = 10
    model = Requisito

    def get_queryset(self):
        usuarioLogado = self.request.user
        return Requisito.objects.filter(user=usuarioLogado)