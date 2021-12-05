from django.shortcuts import render, get_object_or_404
from .models import All_blogs

def all_blogs(request):
    blogs = All_blogs.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs} )

def detail(request, blog_id):
    blog = get_object_or_404(All_blogs, pk=blog_id)
    return render(request, 'blog/detail.html', { 'blog': blog})
