from django.db import models

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Катеория",
        unique=True,
        help_text="Наименование категории товаров",
    )
    description = models.TextField(
        blank=True,
        help_text="Описание категории товаров",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Товар",
        unique=True,
        help_text="Название товара",
    )
    description = models.TextField(
        blank=True,
        help_text="Описание товара",
    )
    photo_product = models.ImageField(
        blank=True,
        upload_to="photo/",
        verbose_name="Фотография товара",
        help_text="Фотография товара",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        help_text="Категория товара",
    )
    price = models.FloatField(
        default=0,
        verbose_name="Цена",
        help_text="Цена товара",
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата занесения",
        help_text="Дата занесения товара",
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата изменения",
        help_text="Дата изменения товара",
    )
    number_views = models.IntegerField(
        default=0, verbose_name="Количество просмотров", help_text="Количество просмотров"
    )
    ispublication = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Опубликовано",
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank = True,
        null = True,
        related_name="owners",
        help_text="Владелец продукта",
    )

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name"]
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
            ('can_delete_products', 'Can delete products'),
        ]
