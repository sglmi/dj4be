from django.shortcuts import render
from django.views.generic import ListView
from .models import Article


class ArticleListView(ListView):
    # model
    model = Article
    # tempalte
    template_name = "article_list.html"
    # context object (variable refernce to the articles)
    context_object_name = "articles"
