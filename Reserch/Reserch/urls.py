from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('Date.urls')),
]
