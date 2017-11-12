from django.shortcuts import render

from blog import models


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {"articles": articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, "blog/article.html", {"article": article})


def edit_article(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, "blog/edit_article.html", {"article": article})


def save_edit_article(request):
    id = request.POST.get("id");
    content = request.POST.get("content");
    title = request.POST.get("title");
    article = models.Article.objects.get(pk=id)
    article.content = content
    article.title = title
    models.Article.objects.filter(pk=article.id).update(content=article.content, title=article.title)
    return render(request, "blog/article.html", {"article": article})


def new_article(request):
    return render(request, "blog/save_article.html")


def save_new_article(request):
    content = request.POST.get("content")
    title = request.POST.get("title")
    article = models.Article.objects.create(content=content, title=title)
    return render(request, "blog/article.html", {"article": article})


def delete_article(request, article_id):
    models.Article.objects.filter(pk=article_id).delete()
    articles = models.Article.objects.all();
    return render(request, "blog/index.html", {"articles": articles})
