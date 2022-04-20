from django.urls import include, path
from users.views import dashboard, register

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('oauth/', include('social_django.urls')),
    path('dashboard', dashboard, name='dashboard'),
    path('register', register, name='register'),
]
