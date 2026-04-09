from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path("", cache_page(60)(BlogListView.as_view()), name="blog_list"),
    path("blog_create/", BlogCreateView.as_view(), name="blog_create"),
    path("blog_detail/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog_delete/<int:pk>/", BlogDeleteView.as_view(), name="blog_delete"),
    path("blog_update/<int:pk>/", BlogUpdateView.as_view(), name="blog_update"),
]
