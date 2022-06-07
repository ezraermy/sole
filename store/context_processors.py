from .models import Category

def category_menu(request):
    categories = Category.objects.all()

    return{'category_menu': categories}