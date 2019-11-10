from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.utils import timezone

from .models import Article
from .forms import ArticleForm
"""
class ArticleListView(TemplateView):
    template_name = "articles/articles_list.html"

class ArticleCreatetView(TemplateView):
    template_name = "articles/articles_create.html"

"""
class ArticleListView(ListView):
    template_name = "articles/articles_list.html"
    model = Article
    def get_queryset(self):
        return Article.objects.order_by('-id')

class ArticleCreatetView(CreateView):
    template_name = "articles/articles_create.html"
    model = Article
    form_class = ArticleForm
    success_url = '/articles/'