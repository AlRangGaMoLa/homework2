from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

from django.contrib.auth.models import User#user만드는 함수들 가져와
from django.contrib import auth
from django.core.paginator import Paginator# 여기 새로적음

# Create your views here.
def blog(request):#blog 함수임
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3) #한페이지안에 객체 3개씩 담겠따.
    page=request.GET.get('page')
    posts=paginator.get_page(page) 
    return render(request, 'blog.html', {'blogs':blogs, 'posts':posts})#python 변수를 html에서 쓸꺼야


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)#객체를 줘 어떤 클래스에 blog_id와 관련된 객체를
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    return render(request, 'new.html')#화면에 new.html을 띄워죠

def create(request):
    blog = Blog()
    blog.title = request.GET['title']#받은 변수 사용하기
    blog.body = request.GET['body']
    blog.pub_date = timezone.now()
    blog.save()
    return redirect('/blog/detail/'+str(blog.id))#해당되는 url을 시작해줘
