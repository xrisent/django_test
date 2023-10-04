from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import *


def CreateArticle(request):
    if request.method == 'GET':
        return render(request, 'create.html', {'form': CreateForm})
    else:
        form = CreateForm(request.POST)
        form.save()
        return redirect('home')

def home(request):
    return render(request, 'home.html')

User = get_user_model()

class GetUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer

class GetArticleView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = GetArticleSerializer

class GetUserView_one(generics.ListAPIView):
    queryset = User.objects.filter(id=1)
    serializer_class = GetUserSerializer