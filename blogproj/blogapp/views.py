from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request):
    blog_index = Blog.objects.all()
    return render(request, 'index.html', {'blog_index' : blog_index})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog' : blog})

def write(request):
    if request.method == "GET":
        return render(request, "write.html")
    
    blog = Blog.objects.create()
    blog.title = request.POST['title']
    blog.content = request.POST['content']
    blog.writer = request.POST['writer']
    blog.image = request.FILES['image']
    blog.save()

    return redirect('detail', blog.id)

def update(request, blog_id):
    if request.method == "GET":
        blog = get_object_or_404(Blog, pk = blog_id)
        return render(request, "update.html", {"blog":blog})

    blog = get_object_or_404(Blog, pk = blog_id)
    blog.content = request.POST['content']
    blog.writer = request.POST['writer']
    blog.image = request.FILES['image']
    blog.save()

    return redirect('detail', blog.id)

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('index')