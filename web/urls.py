from django.urls import path
from web import views

urlpatterns = [
    path('create/', views.CreateArticle, name='create'),
    path('', views.home, name='home'),
    path('serializer/', views.GetUserView.as_view(), name='serializer'),
    path('article-serializer/', views.GetArticleView.as_view(), name='article-serializer'),
    path('ser/', views.GetUserView_one.as_view(), name='ser')
]