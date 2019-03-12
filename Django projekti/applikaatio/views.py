from django.shortcuts import render
from .models import Post

# Create your views here.

posts = [
    {
        'author': 'Helangor',
        'title': 'Blogtest 1',
        'content': 'First post content',
        'date_posted': 'May 08, 1992'
    },
    {
        'author': 'Vaikiaa',
        'title': 'Blogtest 2',
        'content': 'Second post content',
        'date_posted': 'May 08, 2002'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'applikaatio/home.html', context)

def about(request):
    return render(request, 'applikaatio/about.html')
