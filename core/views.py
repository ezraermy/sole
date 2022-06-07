from django.shortcuts import get_object_or_404, render
from store.models import Category, Product

# Create your views here.
def frontpage(request):
    products = Product.objects.filter(is_featured=True)

    context = {
        'products': products,
    }
    return render(request, 'frontpage.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

