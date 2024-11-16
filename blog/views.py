from django.shortcuts import render
from .models import Post
def post_list(request):
    posts = Post.published.all()
    return render(request,
        'blog/post/list.html',
        {'posts': posts})
from django.shortcuts import render
from django.contrib.auth.models import User  # Импортируем модель User

def user_list(request):
    users = User.objects.all()  # Получаем список всех пользователей
    return render(request, 'user_list.html', {'users': users})

# Create your views here.
