from django.shortcuts import render

from shared.models import Banner
from products.models import Category, Product
from gallery.models import Gallery

def home_page_view(request):
    context = {
        'banners': Banner.objects.filter(status=True).order_by('-id'),
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
        'gallery': Gallery.objects.all().order_by('-created_at'),  # ← is this here?
    }
    return render(request, 'index.html', context)