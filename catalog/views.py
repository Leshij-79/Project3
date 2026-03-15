from django.contrib import messages
from django import forms
from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic import FormView
from catalog.models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    success_url = reverse_lazy('catalog:product_list')


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"


class ContactsFormView(FormView):
    template_name = "contacts.html"
    success_url = reverse_lazy('catalog:contacts')


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

        # if request.method == "POST":
        #     name = request.POST.get("name")
        #     phone = request.POST.get("phone")
        #     message = request.POST.get("message")
        #     return HttpResponseRedirect(
        #         f"{name}, благодарим за обращение! Ваше сообщение {message} получено. "
        #         f"С вами свяжутся по номеру {phone}"
        #     )
        #
        # return render(request, "contacts.html")


# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         return HttpResponse(
#             f"{name}, благодарим за обращение! Ваше сообщение {message} получено. "
#             f"С вами свяжутся по номеру {phone}"
#         )
#
#     return render(request, "contacts.html")
