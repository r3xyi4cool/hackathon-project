# Godrej Toothpaste Smart Marketplace

**Care Beyond Clean** — A modern, fully responsive e-commerce website built with Flask, SQLite, HTML, CSS, and JavaScript.

## Features

- User registration and login with password hashing (Werkzeug)
- Product catalog with ratings and eco ratings
- Shopping cart stored in SQLite
- Checkout with address form
- Order history on profile page
- Responsive design with sticky navbar and mobile hamburger menu
- Jinja template inheritance

## Project Structure

```
hackathon-project/
├── app.py                 # Application entry point
├── config.py              # Configuration settings
├── extensions.py          # Flask extensions (db, login_manager)
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── routes/
│   ├── auth.py            # Login, register, logout
│   └── main.py            # Home, products, cart, checkout, profile
├── templates/
│   ├── base.html          # Base layout (navbar, footer)
│   ├── index.html         # Home page
│   ├── partials/          # Reusable template components
│   └── ...                # Other page templates
└── static/
    ├── css/style.css      # Main stylesheet
    ├── js/main.js         # JavaScript (menu, animations)
    └── images/            # SVG product and section images
```

## Installation

### Prerequisites

- Python 3.10 or higher (Python 3.13 requires SQLAlchemy 2.0.36+)
- pip

### Steps

1. **Navigate to the project folder:**

   ```bash
   cd hackathon-project
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - **Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD):**
     ```cmd
     venv\Scripts\activate.bat
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**

   ```bash
   python app.py
   ```

6. **Open in browser:**

   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Demo Flow (Hackathon)

1. Browse featured products on the home page
2. Register a new account
3. Log in and add products to cart
4. Go to Cart → update quantities → Checkout
5. Enter shipping address and place order
6. View order history on Profile page

## Tech Stack

| Layer    | Technology                          |
|----------|-------------------------------------|
| Backend  | Flask, SQLite, Flask-SQLAlchemy     |
| Auth     | Flask-Login, Werkzeug password hash |
| Frontend | HTML, CSS, JavaScript               |
| Templates| Jinja2                              |

## Color Palette

- Background: `#F4F4F4`
- Primary: `#00B7B5`
- Secondary: `#018790`
- Accent: `#005461`
