from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(ListView):
    # model
    model = Article
    # tempalte
    template_name = "article_list.html"
    # context object (variable refernce to the articles)
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ("title", "body")
    template_name = "article_update.html"


class ArticleDeleteView(DeleteView):

    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")


class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_create.html"
    fields = ("title", "body", "author")
