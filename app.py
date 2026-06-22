from flask import Flask

from config import Config
from extensions import db, login_manager
from models import Product
from routes.auth import auth_bp
from routes.main import main_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()
        seed_products()

    return app


def seed_products():
    """Seed or sync product catalog in the database."""
    catalog = [
        {
            "name": "Godrej Chilling paste",
            "description": "Cooling mint formula for lasting freshness and daily oral care.",
            "price": 149.0,
            "rating": 4.6,
            "eco_rating": 4.7,
            "image": "product1.svg",
        },
        {
            "name": "Godrej Herbal Paste",
            "description": "Ayurvedic blend with neem and clove for stronger gums and lasting freshness.",
            "price": 249.0,
            "rating": 4.8,
            "eco_rating": 4.9,
            "image": "product2.svg",
        },
        {
            "name": "Godrej Neem paste",
            "description": "Natural neem extract for antibacterial protection and healthier gums.",
            "price": 200.0,
            "rating": 4.5,
            "eco_rating": 4.6,
            "image": "product3.svg",
        },
        {
            "name": "Godrej Children Paste",
            "description": "Fluoride-free, kid-safe toothpaste with fruity flavor and recyclable tube.",
            "price": 249.0,
            "rating": 4.7,
            "eco_rating": 5.0,
            "image": "product4.svg",
        },
        {
            "name": "Godrej Brush for Adult",
            "description": "Ergonomic soft-bristle brush designed for effective adult oral care.",
            "price": 150.0,
            "rating": 4.4,
            "eco_rating": 4.5,
            "image": "product5.svg",
        },
        {
            "name": "Godrej Brush for Children",
            "description": "Small, gentle brush with easy grip for safe children's brushing.",
            "price": 99.0,
            "rating": 4.6,
            "eco_rating": 4.4,
            "image": "product6.svg",
        },
        {
            "name": "Godrej Mouth Wash For Adult",
            "description": "Antibacterial mouth wash for 12-hour fresh breath protection.",
            "price": 500.0,
            "rating": 4.5,
            "eco_rating": 4.6,
            "image": "product7.svg",
        },
        {
            "name": "Godrej Mouth Wash For Children",
            "description": "Alcohol-free mouth wash gentle enough for daily kids' use.",
            "price": 230.0,
            "rating": 4.9,
            "eco_rating": 5.0,
            "image": "product8.svg",
        },
    ]

    existing = Product.query.order_by(Product.id).all()

    if not existing:
        db.session.add_all([Product(**item) for item in catalog])
    else:
        for index, item in enumerate(catalog):
            if index < len(existing):
                product = existing[index]
                product.name = item["name"]
                product.description = item["description"]
                product.price = item["price"]
                product.rating = item["rating"]
                product.eco_rating = item["eco_rating"]
                product.image = item["image"]

    db.session.commit()


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
