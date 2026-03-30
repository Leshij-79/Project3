from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (ContactsFormView, ProductCreateView, ProductDeleteView, ProductDetailView, ProductListView,
                           ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactsFormView.as_view(), name="contacts"),
    path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
]
