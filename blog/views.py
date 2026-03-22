from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "blog_list.html"

    def get_queryset(self):
        return Blog.objects.filter(ispublication=True)


class BlogDetailView(DetailView):
    model = Blog
    # fields = ["heading", "content", "photo_blog",]
    template_name = "blog_detail.html"
    success_url = reverse_lazy("blog:blog_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = [
        "heading",
        "content",
        "photo_blog",
    ]
    template_name = "blog_create.html"
    success_url = reverse_lazy("blog:blog_list")


class BlogDeleteView(DeleteView):
    model = Blog
    # fields = ["heading", "content", "photo_blog",]
    template_name = "blog_delete.html"
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = [
        "heading",
        "content",
        "photo_blog",
    ]
    template_name = "blog_update.html"
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])
