# E-commerce
This is a simple and stylish E-Commerce web application built using Python Flask and SQLite,
designed for product browsing, cart management, checkout, and order tracking.

🚀 Features

🖼️ Product catalog with images, prices, descriptions
🔍 Search and filter by category
🛒 Add to cart and view cart
✅ Checkout and view order history
➕ Add new products (admin feature)
💡 Flash messages for user feedback
📱 Responsive and stylish UI using Bootstrap

🧰 Tech Stack
Layer	       Technology
Backend	     Python, Flask
Frontend	   HTML, CSS, Bootstrap 5
Database	   SQLite + SQLAlchemy ORM
Templates	   Jinja2
Deployment	 (Optional) GitHub + Render/Vercel/Fly.io

FOLDER STRUCTURE
├── app.py                  # Main application file
├── models.py               # SQLAlchemy models (Product, Order)
├── extensions.py           # Database setup
├── templates/              # HTML templates (Jinja2)
│   ├── base.html
│   ├── home.html
│   ├── products.html
│   ├── cart.html
│   ├── add_product.html
│   ├── orders.html
│   └── ...
├── static/                 # Static files (CSS, Images)
│   ├── style.css
│   └── product images...
├── insert_products.py      # Script to seed products
└── README.md               # Project documentation

INSTALLATION
# 1. Clone the repository
git clone https://github.com/your-username/ecommerce-flask-app.git
cd ecommerce-flask-app

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py

Usage
Visit /add to add new products
Browse /products to view and filter items
Add items to cart, checkout, and view order history
All data is stored in a local SQLite database

To-Do / Future Improvements
User Authentication (Login/Register)
Admin dashboard
Image upload instead of URL
Payment gateway integration
Real-time order notifications
