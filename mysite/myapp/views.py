from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordContextMixin, LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .admin import user
from .models import Visit, User

from .forms import UserCreationForm, VisitForm


class LoginUser(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class register(View):
    template_name = 'registration/register.html'
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

def thanks(request):
    return render(request, 'myapp/thanks.html')


class VisitCreate(CreateView):
    model = Visit
    template_name = 'myapp/visit.html'
    form_class = VisitForm
    success_url = '/profile'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


def services(request):
    return render(request, 'myapp/services.html')


def home(request):
    return render(request, 'myapp/content.html')


class profile(LoginRequiredMixin, View):
    model = user
    template_name = 'myapp/profile.html'
    context_object_name = 'profile'
    def get(self, request):
        template_name = 'myapp/profile.html'
        extra_context = {'title': 'Відомості'}
        visit = Visit.objects.filter(user=self.request.user)
        return render(request, template_name, {'visit': visit})