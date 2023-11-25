from django.shortcuts import render
from django.views.generic import DetailView
from home_page.models import Product

# Create your views here.


class SingleProductDetailView(DetailView):
    template_name = "product.html"
    model = Product
    context_object_name = "product"
