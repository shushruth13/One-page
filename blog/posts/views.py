from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'index.html',)

# Create your views here.
