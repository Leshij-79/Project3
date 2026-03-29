from django.urls import path

from users.apps import UsersConfig
from users.views import CustomUserCreateView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", CustomUserCreateView.as_view(), name="register"),
    # path("", ProductListView.as_view(), name="product_list"),
    # path("contacts/", ContactsFormView.as_view(), name="contacts"),
    # path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    # path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    # path("product_create/", ProductCreateView.as_view(), name="product_create"),
    # path("product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
]
