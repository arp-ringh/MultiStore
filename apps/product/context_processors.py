from apps.product.models import Category, Subcategory


def bulk_categories(request):
    categories = Category.objects.all()

    return {'bulk_categories': categories}

def bulk_subcategories(request):
    subcategories = Subcategory.objects.all()

    return {'bulk_subcategories': subcategories}
