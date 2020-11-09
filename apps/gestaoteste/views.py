from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from apps.gestaoteste.forms import GestaodeTesteForm
from apps.gestaoteste.models import GestaoTeste


@method_decorator(login_required, name='dispatch')
class CTcreate (CreateView):
    model = GestaoTeste
    form_class = GestaodeTesteForm

    def get_form_kwargs(self):
        kwargs = super(CTcreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(CTcreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class CTview(ListView):
    paginate_by = 10
    model = GestaoTeste

    def get_queryset(self):
        usuarioLogado = self.request.user
        return GestaoTeste.objects.filter(user=usuarioLogado)
