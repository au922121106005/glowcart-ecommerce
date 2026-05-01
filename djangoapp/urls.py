# ================================
# SECTION 1: IMPORTS
# Purpose: Import path and views
# ================================
from django.urls import path
from . import views

# ================================
# SECTION 2: URL PATTERNS
# Purpose: Map URLs to view functions
# ================================
urlpatterns = [

    # ================================
    # HOME PAGE
    # Purpose: Landing page of website
    # URL: /
    # ================================
    path('', views.home, name='home'),

    # ================================
    # PRODUCT LIST PAGE
    # Purpose: Display all products
    # URL: /products/
    # ================================
    path('products/', views.product_list, name='products'),

    # ================================
    # ADMIN CRUD PAGE
    # Purpose: Add, Edit, Delete products
    # URL: /crud/
    # ================================
    path('crud/', views.crud_updates, name='crud_updates'),

    # ================================
    # CART PAGE
    # Purpose: Show cart items
    # URL: /cart/
    # ================================
    path('cart/', views.cart, name='cart'),

    # ================================
    # LOGIN PAGE
    # Purpose: User login page
    # URL: /login/
    # ================================
    path('login/', views.user_login, name='login'),

    # ================================
    # LOGOUT PAGE
    # Purpose: User logout page
    # URL: /logout/
    # ================================
    path('logout/', views.user_logout, name='logout'),

    # ================================
    # ADD TO CART
    # Purpose: Add selected product to cart
    # URL: /add-to-cart/<id>/
    # ================================
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('order-success/', views.order_success, name='order_success'),


]

# # APP LEVEL URL
# # URL - Patterns