from django.shortcuts import render
from .models import Post, BlogData
from django.utils import timezone

# Create your views here.
def home(request):
    blogdatas = BlogData.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/home.html', {'blogdatas':blogdatas})

def about(request):
    blogdatas = BlogData.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/about.html', {'blogdatas':blogdatas})

def blog_single(request):
    blogdatas = BlogData.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/blog_single.html', {'blogdatas':blogdatas})

def blog(request):
    blogdatas = BlogData.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/blog.html', {'blogdatas':blogdatas})

def contact(request):
    blogdatas = BlogData.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/contact.html', {'blogdatas':blogdatas})

def features(request):
    blogdatas = BlogData.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/features.html', {'blogdatas':blogdatas})

def portfolio(request):
    blogdatas = BlogData.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/portfolio.html', {'blogdatas':blogdatas})

def post_detail(request, pk):
    blogdata = BlogData.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_detail.html', {'blogdata':blogdata})

def titanic(request):
    # blogdata = BlogData.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/titanic_visual.html', {})
