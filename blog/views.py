from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'NIT AP',
        'title': 'registration',
        'content': 'please update your profile ',
        'date_posted': 'May 17, 2018'
    },
    {
        'author': 'NIT AP',
        'title': 'contact',
        'content':'please contact admin if any issuses occur',
        'date_posted': 'May 18, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request,'blog/about.html',{'title':'about'})