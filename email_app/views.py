from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.core.signing import Signer


from .models import Profile
# Create your views here.


class UpdateProfile(UserPassesTestMixin, UpdateView):
    model = Profile
    fields = '__all__'
    template_name = 'email_app.register.html'

    def test_func(self):
        return self.get_object().user_id == self.request.user


class ProfileDetail(UserPassesTestMixin, DetailView):
    model = Profile

    def test_func(self):
        return self.get_object().user_id == self.request.user


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'email_app/login.html'
    success_url = '/'


def activate(request, token):
    signer = Signer()
    username = signer.unsign(token) # admin4:yyN_C36jUt1AoznGMbBQm2yPjHGgFimHGaqUKITDt_c
    user = User.objects.get(username=username) # get_or_404
    user.is_active = True
    user.save()
    return HttpResponse('Пользователь активирован')
