
"""
COMPREHENSIVE PYTHON DJANGO GUIDE
================================
This guide covers fundamental to advanced Django concepts with practical examples.
Each section demonstrates different aspects of Django web development.
"""

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import path
from django.views import View
from django.db import models
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
import json

# ===========================
# SECTION 1: BASIC DJANGO APP
# ===========================
"""
Creating a basic Django application with views.
"""
print("\n=== Basic Django Setup ===")

# Basic Function-Based View
def home(request):
    return HttpResponse('Hello, Django!')

# ===========================
# SECTION 2: URL PATTERNS
# ===========================
"""
Defining URL patterns and routing in Django.
"""
print("\n=== URL Patterns ===")

urlpatterns = [
    path('', home, name='home'),
    path('user/<str:username>/', user_profile, name='profile'),
    path('api/data/', handle_data, name='data'),
]

# ===========================
# SECTION 3: MODELS
# ===========================
"""
Defining database models in Django.
"""
print("\n=== Models ===")

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# ===========================
# SECTION 4: VIEWS
# ===========================
"""
Different types of views in Django.
"""
print("\n=== Views ===")

# Function-based view
def user_profile(request, username):
    try:
        user = User.objects.get(username=username)
        posts = Post.objects.filter(user=user)
        context = {'user': user, 'posts': posts}
        return render(request, 'profile.html', context)
    except User.DoesNotExist:
        return HttpResponse('User not found', status=404)

# Class-based view
class PostView(View):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            return JsonResponse({
                'title': post.title,
                'content': post.content,
                'author': post.user.username
            })
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)

# ===========================
# SECTION 5: FORMS
# ===========================
"""
Creating and handling forms in Django.
"""
print("\n=== Forms ===")

from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long")
        return title

# ===========================
# SECTION 6: AUTHENTICATION
# ===========================
"""
User authentication and authorization.
"""
print("\n=== Authentication ===")

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# ===========================
# SECTION 7: API VIEWS
# ===========================
"""
Creating API endpoints.
"""
print("\n=== API Views ===")

def handle_data(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        data = serialize('json', posts)
        return HttpResponse(data, content_type='application/json')
    elif request.method == 'POST':
        data = json.loads(request.body)
        post = Post.objects.create(
            user=request.user,
            title=data['title'],
            content=data['content']
        )
        return JsonResponse({
            'id': post.id,
            'title': post.title,
            'content': post.content
        })

# ===========================
# SECTION 8: MIDDLEWARE
# ===========================
"""
Custom middleware implementation.
"""
print("\n=== Middleware ===")

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        import time
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        response['X-Request-Duration'] = str(duration)
        return response

# ===========================
# SECTION 9: TEMPLATE TAGS
# ===========================
"""
Custom template tags and filters.
"""
print("\n=== Template Tags ===")

from django import template
register = template.Library()

@register.filter
def shorten_text(value, length=50):
    if len(value) <= length:
        return value
    return value[:length] + '...'

@register.simple_tag
def get_recent_posts(user, count=5):
    return Post.objects.filter(user=user)[:count]

# ===========================
# SECTION 10: SIGNALS
# ===========================
"""
Django signals for model events.
"""
print("\n=== Signals ===")

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Post)
def handle_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"New post created: {instance.title}")
