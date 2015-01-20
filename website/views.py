from django.shortcuts import render

# Create your views here.
from website.models import Article


def index(request):
    return render(request, 'website/index.html')

def musings(request):
    return render(request, 'website/musings.html', {'articles' : Article.most_recent() })