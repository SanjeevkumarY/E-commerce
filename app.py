from flask import Flask, render_template, redirect, url_for, request, flash, session
from extensions import db
from models import Product, Order

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Needed for session and flash messages

# Initialize DB
db.init_app(app)

# Create DB tables if not exist
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def show_products():
    all_products = Product.query.all()
    return render_template('products.html', products=all_products)

@app.route('/category/<category_name>')
def filter_by_category(category_name):
    filtered_products = Product.query.filter_by(category=category_name).all()
    return render_template('products.html', products=filtered_products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        description = request.form['description']
        image = request.form['image']
        category = request.form.get('category', 'General')

        new_product = Product(name=name, price=price, description=description, image=image, category=category)
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!')
        return redirect(url_for('add_product'))

    return render_template('add_product.html')

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    results = Product.query.filter(
        Product.name.ilike(f"%{query}%") | Product.description.ilike(f"%{query}%")
    ).all()
    return render_template('products.html', products=results, query=query)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    session.modified = True
    flash('Product added to cart!')
    return redirect(url_for('show_products'))

@app.route('/cart')
def cart():
    cart_items = []
    total = 0

    if 'cart' in session:
        for product_id in session['cart']:
            try:
                product_id = int(product_id)
                product = Product.query.get(product_id)
                if product:
                    cart_items.append(product)
                    total += product.price
            except Exception as e:
                print(f"Error in cart item: {e}")

    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/checkout')
def checkout():
    if 'cart' not in session or not session['cart']:
        flash('Your cart is empty.')
        return redirect(url_for('cart'))

    for product_id in session['cart']:
        try:
            product = Product.query.get(int(product_id))
            if product:
                order = Order(product_name=product.name, product_price=product.price)
                db.session.add(order)
        except Exception as e:
            print(f"Error saving order: {e}")

    db.session.commit()
    session['cart'] = []
    flash('✅ Your order has been placed successfully!')
    return redirect(url_for('home'))

@app.route('/orders')
def order_history():
    all_orders = Order.query.all()
    return render_template('order_history.html', orders=all_orders)

if __name__ == '__main__':
    app.run(debug=True)
