from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.cart import  Cart
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart = Cart(request)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shops/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                    'cart': cart}
                  )


def product_detail(request, id, slug):
    cart = Cart(request)
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()

    return render(request,
                  'shops/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'cart': cart}
                  )