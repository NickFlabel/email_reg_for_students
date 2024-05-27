from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.core.signing import Signer

# Create your views here.


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'email_app/register.html'


def activate(request, token):
    signer = Signer()
    username = signer.unsign(token)
    user = User.objects.get(username=username) # get_or_404
    user.is_active = True
    user.save()
    return HttpResponse('Пользователь активирован')
