from django.urls import path, include
from .views import SignUpView
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', SignUpView.as_view(), name = 'signup'),

]