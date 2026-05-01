# ================================
# SECTION 1: IMPORTS
# Import Django forms and Product model
# ================================
from django import forms
from .models import Product

# ================================
# SECTION 2: MODEL FORM
# Create a form based on Product model
# ================================
class ProductForm(forms.ModelForm):

    # ================================
    # SECTION 3: META CLASS
    # Connect this form with Product model
    # ================================
    class Meta:
        model = Product  # Link form to Product model

        # Fields to include in the form
        fields = ['name', 'price', 'image', 'description']






# # =========================================================
# # DJANGO FORMS (ModelForm)
# # =========================================================

# # 1. WHAT IS forms.py?

# # forms.py is used to create forms using Python instead of HTML.
# # Django can automatically generate form fields from models.

# # In this example:
# # We are creating a form to add Product (name + image)
# # ---------------------------------------------------------
# # 2. forms.py (CREATE THIS FILE INSIDE APP)
# # Location: SangeethaDjangoApp/forms.py

# from django import forms
# from .models import Product

# class ProductForm(forms.ModelForm):   # FORM CLASS

# ```
# class Meta:
#     model = Product              # Connects form to Product model
#     fields = ['name', 'image']   # Fields to show in form
# ```
# # ---------------------------------------------------------
# # 3. PURPOSE OF THIS FORM

# # - Creates input fields automatically
# # - Handles user input
# # - Validates data
# # - Saves data to database
# # ---------------------------------------------------------
# # 4. HOW THIS FORM IS USED (FLOW)

# # Step 1: User opens page
# # Step 2: Form is displayed
# # Step 3: User fills form
# # Step 4: Data sent to views.py
# # Step 5: Form validates and saves data
# # ---------------------------------------------------------
# # 5. views.py (USE THE FORM HERE)
# # Location: SangeethaDjangoApp/views.py

# from django.shortcuts import render, redirect
# from .forms import ProductForm

# def add_product(request):
# # POST is a type of HTTP request method used to send data from browser → server
# if request.method == 'POST':
#     form = ProductForm(request.POST, request.FILES)   # Get data + image
    
#     if form.is_valid():   # Validate form
#         form.save()       # Save to database
#         return redirect('product_list')   # Redirect after saving

# else:
#     form = ProductForm()   # Empty form for GET request

# return render(request, 'add_product.html', {'form': form})

# # {'form': form} is called context dictionary. “Send this form to HTML”
# # Left side ('form') = name used in HTML
# # Right side (form) = actual data from Python
# # ---------------------------------------------------------
# # 6. HTML TEMPLATE (REAL FORM)
# # Location: templates/add_product.html

# {% extends 'master.html' %}
# {% load static %}

# {% block content %}

# <h2>Add Product</h2>

# <form method="POST" enctype="multipart/form-data">
#     {% csrf_token %}

#     {{ form.as_p }}

#     <button type="submit">Add Product</button>
# </form>

# {% endblock %}



# {% comment %} 

# 1. method="POST"
#     Add data
#     Update data
#     Delete data
# Need protection from hackers so {% csrf_token %} is used

# 2. Normal form (without enctype)

# <form method="POST">
#     <input type="file">
# </form>

# Browser does not know how to send the file, So it ignores the file, Only text data is sent

# 3. With enctype (encoding type) 

# <form method="POST" enctype="multipart/form-data">
#     <input type="file">
# </form>

# enctype - attribute in HTML defines how form data is encoded before being sent to a server
# Browser understands: “This form has a file”, It sends the file properly to server 

# 4. {% csrf_token %} 
# CSRF = Cross-Site Request Forgery

# {% csrf_token %} is a hidden security code that ensures the form request is safe and not from a hacker.

# {% endcomment %}




# {% comment %} 

# # 1. WHAT IS {{ form.as_p }}

# # It is a Django template syntax used to display form fields in HTML.
# # It automatically converts Python form into HTML inputs.

# # Simple Meaning:
# # {{ form.as_p }} → Show form fields as HTML wrapped in <p> tags
# # ---------------------------------------------------------
# # 2. FROM WHERE DOES "form" COME?

# # It comes from views.py and is passed using context dictionary

# # views.py

# form = ProductForm()
# return render(request, 'add_product.html', {'form': form})

# # 'form' → name used in HTML
# # form → actual ProductForm object
# # ---------------------------------------------------------
# # 3. FROM WHERE DOES FORM STRUCTURE COME?

# # It comes from forms.py (ModelForm)

# from django import forms
# from .models import Product

# class ProductForm(forms.ModelForm):
# class Meta:
# model = Product
# fields = ['name', 'image']

# # Django reads model fields and creates form automatically
# # ---------------------------------------------------------
# # 4. WHAT DOES {{ form.as_p }} GENERATE?

# # Example output (auto-generated HTML)

# <p>
#     <label for="id_name">Name:</label>
#     <input type="text" name="name" required id="id_name">
# </p>

# <p>
#     <label for="id_image">Image:</label>
#     <input type="file" name="image" id="id_image">
# </p>
# # ---------------------------------------------------------
# # 5. WHY USE {{ form.as_p }} INSTEAD OF NORMAL HTML?

# # NORMAL HTML FORM (MANUAL)

# <input type="text" name="name">
# <input type="file" name="image">

# # Problems:

# # - No validation
# # - More coding
# # - Error-prone
# # - Manual handling required

# # DJANGO FORM (AUTOMATIC)
# {{ form.as_p }}

# # Benefits:
# # - Auto form creation
# # - Built-in validation
# # - Less code
# # - Easy to maintain
# # ---------------------------------------------------------
# # 6. OTHER DISPLAY OPTIONS

# # {{ form.as_p }}     → Wrap fields in <p>
# # {{ form.as_table }} → Wrap fields in <tr>
# # {{ form.as_ul }}    → Wrap fields in <li>
# # ---------------------------------------------------------
# # 8. FULL FLOW

# # models.py → defines fields
# # forms.py → creates form
# # views.py → sends form
# # template → displays form using {{ form.as_p }}
# # url.py -> creates path ---------------------------------------------------------
# # 9. FINAL ONE-LINE DEFINITION

# # {{ form.as_p }} automatically converts Django form into HTML input fields wrapped inside <p> tags. 

# {% endcomment %}



# # ---------------------------------------------------------

# # 8. HOW DJANGO PROCESSES THIS

# # 1. User opens page → empty form shown
# # 2. User fills form and clicks submit
# # 3. Data goes to views.py
# # 4. ProductForm(request.POST, request.FILES)
# # 5. form.is_valid() → checks data
# # 6. form.save() → saves to database
# # 7. Redirect to product list page
# # ---------------------------------------------------------