from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import BlogPost
from .forms import CreatBlogForm

# First View in django

# Create an structure to store data
# data will be stored in database

# we have to know how to query the database
# we can update or modify the final output
# we have to know how to show the data to the end user


def home(request):
    search_param = request.GET.get("query")
    author_param = request.GET.get("author")

    blogs = BlogPost.objects.all().order_by("-title")

    if search_param:
        blogs = blogs.filter(
            title__icontains=search_param, body__icontains=search_param)
    if author_param:
        blogs = blogs.filter(authors__first_name__icontains=author_param) | blogs.filter(
            authors__last_name__icontains=author_param)

    total_count = blogs.count()
    return render(request, 'home.html', {"my_blogs": blogs, "total_count": total_count})


def blog_detail(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    return render(request, 'blog_detail.html', {"blog": blog})

# CRUD
# Create a url for new blog
# Create a form to add blog fields
# submit data from html page to the view
# Receive data in  the view and store it in database.


def create_blog(request):
    if request.method == "POST":
        form = CreatBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    form = CreatBlogForm()
    return render(request, 'create_blog.html', {"form": form})


def edit_blog(request, pk):
    blog = BlogPost.objects.get(id=pk)

    if request.method == "POST":
        form = CreatBlogForm(request.POST, request.FILES, instance=blog)
        form.save()
        return HttpResponseRedirect("/")

    form = CreatBlogForm(instance=blog)
    return render(request, 'edit_blog.html', {"form": form})


def delete_blog(request, pk):
    blog = BlogPost.objects.get(id=pk)

    if request.method == "POST":
        blog.delete()
        messages.error(request, 'Your blog post deleted successfully.')
        return HttpResponseRedirect("/")

    return render(request, 'delete_blog.html', {"blog": blog})
