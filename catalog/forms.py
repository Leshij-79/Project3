from django import forms
from django.forms import BooleanField, ValidationError

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductDetailForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = (
            "created_at",
            "updated_at",
            "number_views",
        )


class ProductCUForm(StyleFormMixin, forms.ModelForm):
    STOPWORDS = (
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    )

    class Meta:
        model = Product
        exclude = (
            "created_at",
            "updated_at",
            "number_views",
            "ispublication",
            "owner",
        )

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise ValidationError("Цена не должна быть отрицательной")
        return price

    def clean_name(self):
        name = self.cleaned_data.get("name")
        for stopword in self.STOPWORDS:
            if stopword in name.lower():
                raise ValidationError("В названии продукта есть стоп-слово")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        for stopword in self.STOPWORDS:
            if stopword in description.lower():
                raise ValidationError("В описании продукта есть стоп-слово")
        return description


class ProductCUMForm(StyleFormMixin, forms.ModelForm):
    STOPWORDS = (
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    )

    class Meta:
        model = Product
        exclude = (
            "created_at",
            "updated_at",
            "number_views",
        )

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise ValidationError("Цена не должна быть отрицательной")
        return price

    def clean_name(self):
        name = self.cleaned_data.get("name")
        for stopword in self.STOPWORDS:
            if stopword in name.lower():
                raise ValidationError("В названии продукта есть стоп-слово")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        for stopword in self.STOPWORDS:
            if stopword in description.lower():
                raise ValidationError("В описании продукта есть стоп-слово")
        return description
