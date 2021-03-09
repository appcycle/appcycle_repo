from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from apps.changelog.models import Changelog

@method_decorator(login_required, name='dispatch')
class ChangelogList(ListView):
    paginate_by = 5
    model = Changelog
    ordering = ['-id']


