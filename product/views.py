from django.shortcuts import render
from django.http import HttpResponse, Http404
from .fake_db.products import FAKE_PRODUCT_DATABASE
# Create your views here.

def products(request):
    context = {
        "fake_db_poducts": FAKE_PRODUCT_DATABASE,
    }
    return render(request, 'product/product.html',context)


def product_details(request, id):
    result = list(filter(lambda x: (x['id'] == id), FAKE_PRODUCT_DATABASE))
    if result:
        context = {
            # "title": result[0],
            "item": result[0],
            # "fake_db_poducts": FAKE_PRODUCT_DATABASE,
        }
        return render(request, 'product/product_details.html', context)
    else:
        raise Http404("Product does not exist")