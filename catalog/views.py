from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView

from catalog.models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"


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
