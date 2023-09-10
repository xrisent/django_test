from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Article, STATUS_CHOICES
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
from webapp.validate import article_validate
from webapp.forms import ArticleForm



def index_view(request):
    articles = Article.objects.order_by('-created_at')
    context = {'articles':articles}
    return render(request, 'index.html', context)


def article_view(request, pk):
    # try:
    #     pk = request.GET.get('pk')
    #     article = Article.objects.get(pk=pk)
        
    # except Article.DoesNotExist:
    #     return HttpResponseNotFound('Страница не найдена')
    
    # return render(request, 'article_view.html', {'article':article})
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_view.html', {'article':article, 'statuses': STATUS_CHOICES})


def create_article(request):
    if request.method == 'GET':
        form = ArticleForm()

        return render(request, 'create.html', {'form':form})
    
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            author = form.cleaned_data.get('author')
            content = form.cleaned_data.get('content')
            new_article = Article.objects.create(title=title, author=author, content=content,)
            return redirect('article_view', pk=new_article.pk)
        return render(request, 'create.html', {'form':form, 'statuses':STATUS_CHOICES})
            # errors = article_validate(title, author, content)
        # context = {'article':new_article}
        # return HttpResponseRedirect(reverse('article_view', kwargs={'pk': new_article.pk}))
        # return render(request, 'article_view.html', context)
        # return HttpResponseRedirect(f'/article/{new_article.pk}')
        # if errors:
            
        # new_article.save()
        

def update_article(request, pk):
    # article = get_object_or_404(Article, pk=pk)
    # if request.method == 'GET':
    #     return render(request, 'update.html', {'article': article, 'statuses': STATUS_CHOICES})
    # else:
    #     article.title = request.POST.get('title')
    #     article.content = request.POST.get('content')
    #     article.author = request.POST.get('author')
    #     article.status = request.POST.get('status')
    #     article.save()
    #     return redirect('article_view', pk=article.pk)
    form = ArticleForm()
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'update.html', {'form': form})
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.title = form.cleaned_data.get('title')
            article.author = form.cleaned_data.get('author')
            article.content = form.cleaned_data.get('content')
            article.save
            return redirect('article_view', pk=article.pk)
        return render(request, 'update.html', {'form':form})

    
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('index')