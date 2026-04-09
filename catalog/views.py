from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, DeleteView, DetailView, FormView, ListView, UpdateView

from catalog.forms import ProductCUForm, ProductCUMForm, ProductDetailForm
from catalog.models import Product
from catalog.services import CatalogServices


@method_decorator(cache_page(60), name="dispatch")
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    form_class = ProductDetailForm
    template_name = "product_detail.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"

    def get_queryset(self):
        queryset = cache.get('my_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('my_queryset', queryset, 60)
        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCUForm
    template_name = "product_cu.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_delete.html"
    success_url = reverse_lazy("catalog:product_list")
    permission_required = "catalog.can_delete_products"

    def delete_view(self, object_id):
        obj = get_object_or_404(Product, id=object_id)

        if not self.request.user.groups.filter(name="moderators").exists() or self.object.owner != self.request.user:
            return HttpResponseForbidden("У вас нет прав для удаления этого объекта.")

        obj.delete()

        return redirect("catalog:product_list")

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас нет прав на удаление!")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductCUForm
    template_name = "product_cu.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user

        if user == self.object.owner:
            return ProductCUForm
        if user.has_perms(
            [
                "catalog.can_unpublish_product",
            ]
        ):
            return ProductCUMForm

        raise PermissionDenied


class CategoryListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "category_list.html"
    context_object_name = "all_products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_id = self.object.category
        context["all_products"] = CatalogServices.all_products(category_id)

        return context




class ContactsFormView(FormView):
    template_name = "contacts.html"
    success_url = reverse_lazy("catalog:contacts")

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        HttpResponseRedirect(
            f"{name}, благодарим за обращение! Ваше сообщение {message} получено. "
            f"С вами свяжутся по номеру {phone}"
        )
        return render(request, "contacts.html")
