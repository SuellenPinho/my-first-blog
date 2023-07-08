from django.shortcuts import render
from django.utils import timezone
from .models import Post #Tanto views.py como models.py estão no mesmo diretório. Isto significa que podemos usar . e o nome do arquivo (sem py).

# Create your views here.

def post_list(request): 
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})