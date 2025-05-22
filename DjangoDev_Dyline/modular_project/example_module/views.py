from .forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from modular_engine.models import ManagedModule

# AUTH
def is_manager(user):
    return user.groups.filter(name='manager').exists()
def is_user(user):
    return user.groups.filter(name='user').exists()
def is_public(user):
    return not user.is_authenticated or user.groups.filter(name='public').exists()

# READ (all roles)
def product_list(request):
    
    # If the module is not installed
    if not ManagedModule.objects.filter(app_name='example_module', installed=True).exists():
        # Return Error/404
        return render(request, "example_module/product_list.html", {'error_message': 'This module is not installed'})
    
    # If installed
    products = Product.objects.all()
    if not request.user.is_authenticated:
        role = "public"
    elif is_manager(request.user):
        role = "manager"
    elif is_user(request.user):
        role = "user"
    else:
        role = "public"
    return render(request, "example_module/product_list.html", {"products": products, "role": role})

# CREATE (user & manager)
@login_required
@user_passes_test(lambda u: is_manager(u) or is_user(u))
def product_create(request):
    if request.method == "POST":
        name = request.POST["name"]
        barcode = request.POST["barcode"]
        price = request.POST["price"]
        stock = request.POST["stock"]
        Product.objects.create(name=name, barcode=barcode, price=price, stock=stock)
        return redirect("product-list")
    else:
        form = ProductForm()
    return render(request, 'example_module/product_form.html', {'form': form, 'action': 'Add'})

# UPDATE (user & manager)
@login_required
@user_passes_test(lambda u: is_manager(u) or is_user(u))
def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        product.name = request.POST["name"]
        product.barcode = request.POST["barcode"]
        product.price = request.POST["price"]
        product.stock = request.POST["stock"]
        product.save()
        return redirect("product-list")
    else:
        form = ProductForm(instance=product)
    return render(request, 'example_module/product_form.html', {'form': form, 'action': 'Update'})

# DELETE (only manager)
@login_required
@user_passes_test(is_manager)
def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        # popup validation handled in template
        product.delete()
        return redirect("product-list")
    return render(request, "example_module/product_confirm_delete.html", {"product": product})

