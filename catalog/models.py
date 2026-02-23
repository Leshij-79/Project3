from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Катеория',
        unique=True,
        help_text='Наименование категории товаров',
    )
    description = models.TextField(
        blank=True,
        help_text='Описание категории товаров',
    )

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Товар',
        unique=True,
        help_text='Название товара',
    )
    description = models.TextField(
        blank=True,
        help_text='Описание товара',
    )
    photo_product = models.ImageField(
        blank=True,
        upload_to='photo/',
        verbose_name='Фотография товара',
    )
    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,
        related_name='products',
    )
    price = models.FloatField(
        default=0,
        verbose_name='Цена',
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата занесения',
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name='Дата изменения',
    )




    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']
