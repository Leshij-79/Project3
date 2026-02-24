from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Тест кастомной команды"

    def handle(self, *args, **options):
        Category.objects.all().delete()

        categories = [
            {"name": "Категория 1", "description": "Описание категории 1"},
            {"name": "Категория 2", "description": "Описание категории 2"},
            {"name": "Категория 3", "description": "Описание категории 3"},
            {"name": "Категория 4", "description": "Описание категории 4"},
        ]
        categories_id = []
        for category_data in categories:
            category, created = Category.objects.get_or_create(**category_data)
            if created:
                categories_id.append(category.id)
                self.stdout.write(self.style.SUCCESS(f'Категория - {category_data["name"]} - создана'))
            else:
                self.stdout.write(self.style.WARNING(f'Категория - {category_data["name"]} - существует'))

        products = [
            {"name": "Товар 1", "description": "Описание товара 1", "category_id": categories_id[0], "price": 100},
            {"name": "Товар 2", "description": "Описание товара 2", "category_id": categories_id[0], "price": 200},
            {"name": "Товар 3", "description": "Описание товара 3", "category_id": categories_id[1], "price": 300},
            {"name": "Товар 4", "description": "Описание товара 4", "category_id": categories_id[1], "price": 400},
            {"name": "Товар 5", "description": "Описание товара 5", "category_id": categories_id[2], "price": 500},
            {"name": "Товар 6", "description": "Описание товара 6", "category_id": categories_id[2], "price": 600},
            {"name": "Товар 7", "description": "Описание товара 7", "category_id": categories_id[3], "price": 700},
            {"name": "Товар 8", "description": "Описание товара 8", "category_id": categories_id[3], "price": 800},
            {"name": "Товар 9", "description": "Описание товара 9", "category_id": categories_id[3], "price": 900},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Товар - {product_data["name"]} - создан'))
            else:
                self.stdout.write(self.style.WARNING(f'Товар - {product_data["name"]} - существует'))
