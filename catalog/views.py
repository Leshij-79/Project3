from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, FormView, ListView, UpdateView

from catalog.forms import ProductCUForm, ProductDetailForm, ProductCUMForm
from catalog.models import Product


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
    permission_required = 'catalog.can_delete_products'

    def handle_no_permission(self):
        return HttpResponseForbidden('У вас нет прав на удаление!')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductCUForm
    template_name = "product_cu.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user

        if user ==  self.object.owner:
            return ProductCUForm
        if user.has_perms(['catalog.can_unpublish_product',]):
            return ProductCUMForm

        raise PermissionDenied


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
