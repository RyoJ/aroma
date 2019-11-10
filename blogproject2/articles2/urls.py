from django.urls import path
from .views import ArticleListView, ArticleCreatetView

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles.list'),
    path('create/', ArticleCreatetView.as_view(), name='articles.create'),
]