# ================================
# SECTION 1: IMPORTS
# Purpose: Import required Django tools
# ================================
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout

from .models import Product
from .forms import ProductForm

# ================================
# SECTION 2: PUBLIC PAGES
# Purpose: Basic pages (no logic)
# ================================
def home(request):
    return render(request, 'home.html')

# ================================
# SECTION 3: PRODUCT LIST (USER)
# Purpose: Display all products
# ================================
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

# ================================
# SECTION 4: ADMIN CRUD
# Purpose: Add, Edit, Delete products
# ================================
@staff_member_required
def crud_updates(request):

    # =======================
    # ADD PRODUCT
    # =======================
    if request.method == 'POST' and 'add_product' in request.POST:
        add_form = ProductForm(request.POST, request.FILES)

        if add_form.is_valid():
            add_form.save()
            messages.success(request, "Product added successfully!")
            return redirect('crud_updates')
        else:
            messages.error(request, "Error adding product. Check inputs.")

    else:
        add_form = ProductForm()

    # =======================
    # LIST PRODUCTS
    # =======================
    products = Product.objects.all()

    # =======================
    # EDIT PRODUCT
    # =======================
    edit_product = None
    edit_form = None

    edit_id = request.GET.get('edit_id')
    if edit_id:
        edit_product = get_object_or_404(Product, id=edit_id)

        if request.method == 'POST' and 'edit_product' in request.POST:
            edit_form = ProductForm(request.POST, request.FILES, instance=edit_product)

            if edit_form.is_valid():
                edit_form.save()
                messages.success(request, "Product updated successfully!")
                return redirect('crud_updates')
            else:
                messages.error(request, "Error updating product.")

        else:
            edit_form = ProductForm(instance=edit_product)

    # =======================
    # DELETE PRODUCT
    # =======================
    delete_id = request.GET.get('delete_id')

    if delete_id:
        try:
            product = Product.objects.get(id=delete_id)
            product.delete()
            messages.success(request, "Product deleted successfully!")
            return redirect('crud_updates')
        except Product.DoesNotExist:
            messages.error(request, "Product not found.")


    return render(request, 'crud_updates.html', {
        'products': products,
        'add_form': add_form,
        'edit_form': edit_form,
        'edit_product': edit_product,
    })

# ================================
# SECTION 5: CART LOGIC
# Purpose: Add and display cart items
# ================================

# ADD TO CART
def add_to_cart(request, id):

    # Get cart from session
    cart = request.session.get('cart', [])

    # Add product ID
    cart.append(id)

    # Save back to session
    request.session['cart'] = cart

    messages.success(request, "Product added to cart!")

    return redirect('cart')

def remove_from_cart(request, id):

    cart = request.session.get('cart', [])

    if id in cart:
        cart.remove(id)

    request.session['cart'] = cart

    messages.success(request, "Product removed from cart!")

    return redirect('cart')

# VIEW CART
def cart(request):

    # Get cart from session
    cart = request.session.get('cart', [])

    # Fetch products
    products = Product.objects.filter(id__in=cart)

    # Calculate total price
    total_price = sum(product.price for product in products)

    return render(request, 'cart.html', {
        'products': products,
        'total_price': total_price
    })

# ================================
# SIMPLE CODE EXPLANATION
# ================================


# request.method - Tells how request is sent (GET or POST)
# GET - Used to retrieve data (no changes)
# POST - Used to send data (add/update/delete)
# request.POST - Contains form data submitted by user
# request.FILES - Contains uploaded files (images)
# is_valid() - Validates form data before saving
# save() - Saves data into database
# redirect('crud_updates') - Redirects to URL named 'crud_updates'


# ---------------------------------


# Login
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")

    return render(request, 'login.html')

# LOGOUT
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')





def order_success(request):
    # Clear cart after order (important!)
    request.session['cart'] = []

    return render(request, 'order_success.html')







# ================================
# EXPLANATION
# ================================


# ================================
# SECTION 1: IMPORTS
# ================================
# This section imports all required Django modules and project files.

# django.shortcuts →
# Contains helper functions for common tasks like rendering pages,
# redirecting users, and fetching objects easily.

# render → Used to display HTML templates
# redirect → Used to navigate to another URL
# get_object_or_404 → Fetch object or return 404 error if not found

# ---------------------------------

# django.contrib →
# Built-in Django package that provides extra features like
# authentication, admin panel, messages framework, etc.

# Authentication = Identity check
# Login → Authentication
# (Checking who you are)
# Authentication → “Are you really this user?”

# Authorization = Permission check
# Access admin page → Authorization
# (Checking what you are allowed to access)
# Authorization → “What can you do after logging in?”

# django.contrib.messages →
# Used to display success/error notification messages to users

# ---------------------------------
# Decorator = Function that modifies another function

# Decorator → Adds extra behavior
# Works like a wrapper around a function

# Login required → Decorator
# Admin-only access → Decorator
# Permission check → Decorator

# django.contrib.admin.views.decorators → Contains decorators related to admin access control

# ---------------------------------

# staff_member_required → Decorator that allows only admin (staff) users to access a view

# ---------------------------------

# Product → Model representing product data stored in the database

# ProductForm → Form used to create and update product details

# ================================

# SECTION 2: PUBLIC PAGES
# home() → opens home page
# user_login() → opens login page
# These functions only display pages, no extra work.

# ================================

# SECTION 3: PRODUCT LIST
# Fetch all products → Pass to template → Display to user

# Product.objects.all() → get all products

# Open page → Function runs
# Get all products → From database
# Send data → HTML page
# Display products → User sees output

# ================================

# SECTION 4: ADMIN (CRUD)
# Only admin can access

# ADD PRODUCT
# - Takes form data + image
# - Checks if correct
# - Saves data
# - Shows message
# - Reloads page
# - If error → shows error
# - If page is opened normally → empty form is shown

# request.method → check GET or POST
# POST → send data
# GET → open page
# request.POST → Contains form data submitted by user
# request.FILES → Contains uploaded file - image data
# is_valid() → Validates form data before saving
# save() → store in database
# redirect('crud_updates') - Redirects to URL named 'crud_updates'

# ---------------------------------

# SHOW PRODUCTS
# Gets all products for admin page

# Product.objects.all() - Fetch all records from Product table
# Product.objects.get(id=...) - Fetch single product by ID
# Product.DoesNotExist - Error when product not found in database
# filter(id__in=cart) - Fetch multiple products whose IDs are in list
# session - Temporary storage for each user (like cart data)

# ---------------------------------

# EDIT PRODUCT
# Checks if a product is selected for editing
# - Shows old data in form
# - Updates with new data
# - Shows success message
# - Saves and reloads
# If not submitted:
# - Shows form with old data already filled

# request.GET.get('edit_id') → get product id
# instance → update existing data

# request.session.get('cart', []) - Get cart data, default = empty list
# request.session['cart'] = cart - Save updated cart back to session
# decorator (@staff_member_required) - Adds restriction/extra behavior to function
# instance=edit_product - Used to update existing data instead of creating new
# request.GET.get('edit_id') - Get value from URL (query parameter)
# ---------------------------------

# DELETE PRODUCT
# - Checks if delete request is given
# - Finds that product
# - Deletes product
# - Shows success message
# - If not found → error message

# delete() → Removes object from database
# try-except → Used to handle errors safely


# FINAL RETURN
# Sends products, add form, edit form to page
# Page will display everything

# Sends products + forms to page

# context {'products': products} → Sends data from views → template(HTML)

# ---------------------------------

# SECTION 5: CART

# ADD TO CART
# - Gets current cart data
# - Adds selected product
# - Saves updated cart
# - Shows success message
# - Redirects to cart page

# session → temporary storage
# request.session.get() → get cart
# request.session['cart'] → save cart


# VIEW CART
# - Gets product ids from cart
# - Fetches those products
# - Sends them to cart page
# - Page displays selected products

# filter(id__in=cart) → get multiple products


# ---------------------------------

# FINAL FLOW

# 1. User views products
# 2. Admin manages products (add/edit/delete)
# 3. User adds products to cart
# 4. Cart stores data temporarily
# 5. Cart page shows selected products

# ---------------------------------

# KEYWORDS (VERY IMPORTANT)

# ORM (Object Relational Mapping)
# Django way to interact with database using Python

# CRUD
# Create → Add data
# Read → View data
# Update → Edit data
# Delete → Remove data

# session-based cart
# Cart stored temporarily per user using session

# form handling
# Collect → Validate → Save user input

# =========================================================
# SHORT MEMORY TRICKS
# =========================================================

# render → show page
# redirect → go page
# POST → send data
# GET → get data
# session → temporary storage
# ORM → database access
# instance → update existing
# filter → multiple data
# get → single data
# messages → alerts