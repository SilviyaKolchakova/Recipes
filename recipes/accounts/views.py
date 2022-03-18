from django import forms
from django.contrib.auth import forms as auth_forms, login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render

from accounts.models import RecipesUser


class UserRegisterForm(auth_forms.UserCreationForm):
    # first_name = forms.CharField(max_length=25)

    class Meta:
        model = RecipesUser
        fields = ('email',)


class UserRegisterView(views.CreateView):
    form_class = UserRegisterForm
    model = RecipesUser
    template_name = 'register.html'
    success_url = reverse_lazy('show index')

    def form_valid(self, form):
        result = super().form_valid(form)
        # user => self.object
        # request => self.request
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        next = self.request.GET.get('next', None)
        if next:
            return next
        return reverse_lazy('show index')