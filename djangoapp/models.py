# ================================
# SECTION 1: IMPORTS
# Purpose: Import Django model base class
# ================================
from django.db import models

# ================================
# SECTION 2: PRODUCT MODEL
# Purpose: Define database structure for Product
# ================================
class Product(models.Model):

    # Product Name
    name = models.CharField(max_length=200)

    # Product Price
    price = models.IntegerField()

    # Product Image
    image = models.ImageField(upload_to="products/")

    # Product Description
    description = models.TextField()


    # ================================
    # SECTION 3: STRING METHOD
    # Purpose: Show product name in admin / shell
    # ================================
    def __str__(self):
        return self.name