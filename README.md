## 🛒 GlowCart - Django E-Commerce Web Application GlowCart is a full-stack e-commerce web application built using Django. It allows users to browse products, add items to a shopping cart, and manage orders with a simple and responsive UI. --- ## 🚀 Features - 🛍️ Product listing with images and pricing - 🛒 Session-based shopping cart system - ➕ Add / ❌ Remove items from cart - 💰 Auto-calculated cart total - 🔐 User authentication (login/logout) - 🧑‍💼 Admin dashboard for product management (CRUD) - 📦 Product image upload support - 🎨 Responsive UI using Bootstrap --- ## 🛠️ Tech Stack - Backend: Django (Python) - Frontend: HTML, CSS, Bootstrap - Database: SQLite / MySQL (configurable) - Authentication: Django built-in auth system --- ## 📁 Project Structure djangoapp/ Paulinaproject/ templates/ static/ manage.py --- ## ⚙️ Installation & Setup
bash
# Clone repository
git clone https://github.com/au922121106005/glowcart-ecommerce.git

# Move into project
cd glowcart-ecommerce

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```
