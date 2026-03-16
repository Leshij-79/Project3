from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "blog_list.html"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"
    success_url = reverse_lazy('blog:blog_list')


class BlogCreateView(CreateView):
    model = Blog
    fields = ["heading", "content", "photo_blog",]
    template_name = "blog_create.html"
    success_url = reverse_lazy('blog:blog_list')


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog_delete.html"
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blog_update.html"
    success_url = reverse_lazy('blog:blog_detail')
