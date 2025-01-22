"""
URL configuration for video_redirect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import video_page, redirect_page,about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v/<int:user_id>/<int:video_id>/<int:redirect_id>/', video_page, name='video_page'),
    path('redirect/', redirect_page, name='redirect_page'),
    path('', about),
]
