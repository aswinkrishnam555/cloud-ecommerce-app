from flask import Blueprint, session, redirect, url_for, render_template
from flask_login import login_required, current_user
from app import db
from app.models import Product, Order, OrderItem

cart = Blueprint('cart', __name__)

@cart.route('/cart/add/<int:product_id>')
@login_required
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    session.modified = True
    return redirect(url_for('products.index'))

@cart.route('/cart')
@login_required
def view_cart():
    cart_items = []
    if 'cart' in session:
        for pid in session['cart']:
            product = Product.query.get(pid)
            if product:
                cart_items.append(product)
    return render_template('cart.html', cart_items=cart_items)