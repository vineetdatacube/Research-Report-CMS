from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from reports.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]