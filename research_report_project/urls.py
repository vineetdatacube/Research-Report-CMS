from django.contrib.auth import views as auth_views

path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),