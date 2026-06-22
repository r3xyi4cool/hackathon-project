from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from extensions import db
from models import CartItem, Order, Product

main_bp = Blueprint("main", __name__)

# Sample customer reviews for the home page
REVIEWS = [
    {
        "name": "Priya Sharma",
        "rating": 5,
        "review": "Love the eco-friendly packaging! My family has switched to Godrej toothpaste and we couldn't be happier.",
        "image": "review1.svg",
    },
    {
        "name": "Arjun Mehta",
        "rating": 5,
        "review": "Smart marketplace experience with fast delivery. The herbal variant is my daily go-to.",
        "image": "review2.svg",
    },
    {
        "name": "Sneha Reddy",
        "rating": 4,
        "review": "Affordable prices and sustainable products. The checkout process was smooth and secure.",
        "image": "review3.svg",
    },
    {
        "name": "Rahul Kapoor",
        "rating": 5,
        "review": "Excellent eco ratings on every product. Finally a brand that cares about the planet.",
        "image": "review4.svg",
    },
    {
        "name": "Ananya Iyer",
        "rating": 5,
        "review": "The charcoal toothpaste leaves my teeth feeling incredibly clean. Highly recommend!",
        "image": "review5.svg",
    },
    {
        "name": "Vikram Singh",
        "rating": 4,
        "review": "Great customer service and genuine products. Order tracking was transparent throughout.",
        "image": "review6.svg",
    },
    {
        "name": "Meera Joshi",
        "rating": 5,
        "review": "Sustainable smile care at its best. The website is beautiful and easy to navigate.",
        "image": "review7.svg",
    },
]


@main_bp.route("/")
def index():
    featured_products = Product.query.limit(6).all()
    return render_template("index.html", featured_products=featured_products, reviews=REVIEWS)


@main_bp.route("/products")
def products():
    all_products = Product.query.all()
    return render_template("products.html", products=all_products)


@main_bp.route("/about")
def about():
    return render_template("about.html")


@main_bp.route("/contact")
def contact():
    return render_template("contact.html")


@main_bp.route("/terms")
def terms():
    return render_template("terms.html")


@main_bp.route("/privacy")
def privacy():
    return render_template("privacy.html")


@main_bp.route("/add-to-cart/<int:product_id>", methods=["POST"])
@login_required
def add_to_cart(product_id):
    product = db.session.get(Product, product_id)
    if not product:
        flash("Product not found.", "error")
        return redirect(request.referrer or url_for("main.products"))

    cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = CartItem(user_id=current_user.id, product_id=product_id, quantity=1)
        db.session.add(cart_item)

    db.session.commit()
    flash(f"{product.name} added to cart!", "success")
    return redirect(request.referrer or url_for("main.cart"))


@main_bp.route("/cart")
@login_required
def cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template("cart.html", cart_items=cart_items, total=total)


@main_bp.route("/cart/update/<int:item_id>", methods=["POST"])
@login_required
def update_cart(item_id):
    cart_item = CartItem.query.filter_by(id=item_id, user_id=current_user.id).first()
    if not cart_item:
        flash("Cart item not found.", "error")
        return redirect(url_for("main.cart"))

    quantity = request.form.get("quantity", type=int, default=1)
    if quantity < 1:
        quantity = 1
    if quantity > 99:
        quantity = 99

    cart_item.quantity = quantity
    db.session.commit()
    flash("Cart updated.", "success")
    return redirect(url_for("main.cart"))


@main_bp.route("/cart/remove/<int:item_id>", methods=["POST"])
@login_required
def remove_from_cart(item_id):
    cart_item = CartItem.query.filter_by(id=item_id, user_id=current_user.id).first()
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        flash("Item removed from cart.", "info")
    return redirect(url_for("main.cart"))


@main_bp.route("/checkout", methods=["GET", "POST"])
@login_required
def checkout():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        flash("Your cart is empty.", "error")
        return redirect(url_for("main.cart"))

    total = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == "POST":
        address = request.form.get("address", "").strip()
        city = request.form.get("city", "").strip()
        state = request.form.get("state", "").strip()
        postal_code = request.form.get("postal_code", "").strip()

        if not all([address, city, state, postal_code]):
            flash("All address fields are required.", "error")
            return render_template("checkout.html", total=total)

        order = Order(
            total_price=total,
            user_id=current_user.id,
            address=address,
            city=city,
            state=state,
            postal_code=postal_code,
        )
        db.session.add(order)

        for item in cart_items:
            db.session.delete(item)

        db.session.commit()
        flash("Order placed successfully!", "success")
        return redirect(url_for("main.profile"))

    return render_template("checkout.html", total=total)


@main_bp.route("/profile")
@login_required
def profile():
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.order_date.desc()).all()
    return render_template("profile.html", orders=orders)
