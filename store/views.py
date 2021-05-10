from django.shortcuts import render, redirect
from .models import Category, Product


def home(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }
    return render(request, 'store/home.html', context)


def categories(request, category_id):

    category = Category.objects.get(id=category_id)

    all_products = Product.objects.all()

    products = []

    for i in all_products:
        if i.category.id == int(category_id):
            products.append(i)

    context = {
        "category": category,
        "products": products
    }
    return render(request, 'store/categories.html', context)


def ind_products(request, product_id):
    product = Product.objects.get(id=product_id)

    context = {
        "product": product
    }
    return render(request, 'store/individual_products.html', context)


def add_cart(request):
    products_in_cart = []
    cart_ids = request.session.get("cart_items", [])
    if request.method == "POST":
        item_id = request.POST["product_id"]
        cart_ids.append(item_id)

    for i in cart_ids:
        product = Product.objects.get(id=int(i))

        counter = cart_ids.count(i)

        product_in_cart = {
            "id": product.id,
            "name": product.product_name,
            "price": product.price_with_vat,
            "counter": counter
        }

        products_in_cart.append(product_in_cart)

    request.session["cart_items"] = cart_ids

    context = {
        "products_in_cart": products_in_cart,
    }

    return render(request, "store/cart.html", context)


def remove_from_cart(request):
    cart_ids = request.session.get("cart_items", [])
    if request.method == "POST":
        item_id = request.POST["id"]

    for i in cart_ids:
        if i == item_id:
            cart_ids.remove(i)

    request.session["cart_items"] = cart_ids

    return redirect("add_cart")
