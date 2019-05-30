"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings#내 세팅을 가져와라
from django.conf.urls.static import static#url들을 가져와라

from . import views
urlpatterns = [
    path('blog/',include('blog.urls')),
    path('account/',include('account.urls')),
    path('admin/', admin.site.urls),
    path('',views.home2),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#새로운 static을 만들어라 경로는 media고 파일경로는 media 경로다
