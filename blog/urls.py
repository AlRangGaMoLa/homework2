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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name = "blog"),#url이 ''이면 blog 함수를 실행 시켜라. 이름은 blog다.
    path('detail/<int:blog_id>/', views.detail, name = "detail"),#나는 blog_id도 같이 받을꺼다.
    path('new/',views.new, name="new"),
    path('create/',views.create, name="create"),#함수 실행이 주 목적임
]
