from django.contrib import admin
from django.urls import path, include

from .forms import user
from .views import home, services, visit, thanks, register, profile, LoginUser

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('', include('django.contrib.auth.urls')),
    path('accounts/login/', LoginUser.as_view(), name='login'),
    path('register/', register.as_view(), name='register'),
    path('visit/', visit, name='visit'),
    path('services/', services, name='services'),
    path('thanks/', thanks, name='thanks_page'),
    path('profile', profile.as_view(), name='profile')
]
