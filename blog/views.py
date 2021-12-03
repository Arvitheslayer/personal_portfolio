from django.shortcuts import render
from .models import All_blogs

def all_blogs(request):
    blogs = All_blogs.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs':blogs} )
