from catalog.models import Product


class CatalogServices:

    @staticmethod
    def all_products(category_id):
        products = Product.objects.filter(category_id=category_id)

        if not products.exists():
            return None

        return products
