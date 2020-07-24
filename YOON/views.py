from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.utils import timezone
from .form import BlogForm,GuestForm

def home(request):
    blogs= Blog.objects.all()
    return render(request, 'home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog})

def edit(request,blog_id):
    edit_blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'edit.html',{'blog':edit_blog})

def new(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.save()
            return redirect('home')

    else:
        form = BlogForm()
        return render(request, 'new.html', {'form':form})

def update(request,blog_id):
    update_blog = get_object_or_404(Blog, pk=blog_id)
    update_blog.title = request.POST['title']
    update_blog.pub_date = timezone.datetime.now()
    update_blog.body = request.POST['body']
    update_blog.save()
    return redirect('detail',update_blog.id)

def delete(request,blog_id):
    delete_blog = get_object_or_404(Blog,pk = blog_id)
    delete_blog.delete()
    return redirect('home')


def guest(request):
    guests= Guest.objects.all()
    return render(request, 'guestbook.html',{'guests':guests})

def new_guest(request):
    if request.method == 'POST':
        form = GuestForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.save()
            return redirect('guest')

    else:
        form = GuestForm()
        return render(request, 'new_guest.html', {'form':form})

