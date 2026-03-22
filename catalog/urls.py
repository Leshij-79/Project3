from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactsFormView, ProductDetailView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactsFormView.as_view(), name="contacts"),
    path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),

]
