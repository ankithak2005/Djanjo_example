from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
    return HttpResponse("Welcome to the blog home page #")

def post_details(request,id):
    return HttpResponse(f"This is the blog post number {id}")

def index(request):
    return render(request,'blog/index.html')

def resume(request):
    return render(request,'blog/resume.html')

def post_details_in_html(request,post_id):
    context={
        'post_id':post_id,
        'title':f'Blog Post #{post_id}',
        'author':'Ankitha',
    }
    return render(request,'blog/postdetails.html',context)

def indexhtml(request):
    return render(request,'blog/indexnew.html')

def dbaccess(request,p_id):
    post=Post.objects.get(id=p_id)
    return render(request,'blog/dbacc.html',{'post': post})