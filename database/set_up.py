import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "store.db"


def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS products")
    cursor.execute("DROP TABLE IF EXISTS reviews")

    cursor.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT NOT NULL,
            is_organic INTEGER NOT NULL,
            stock INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            rating REAL NOT NULL,
            review_text TEXT NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

    products = [
        ("Organic Wild Honey", "Honey", 12.99, "Pure organic wildflower honey with natural sweetness.", 1, 25),
        ("Raw Forest Honey", "Honey", 14.50, "Raw honey collected from forest farms, rich taste.", 1, 18),
        ("Classic Honey Bottle", "Honey", 8.99, "Affordable everyday honey for tea and breakfast.", 0, 40),
        ("Premium Manuka Honey", "Honey", 24.99, "High-quality manuka honey with strong flavor.", 1, 10),
        ("Organic Peanut Butter", "Peanut Butter", 9.99, "Creamy organic peanut butter with no added sugar.", 1, 30),
        ("Crunchy Peanut Butter", "Peanut Butter", 6.99, "Crunchy peanut butter with roasted peanuts.", 0, 35),
        ("Organic Green Tea", "Tea", 11.99, "Organic green tea leaves with fresh aroma.", 1, 50),
        ("Black Tea Pack", "Tea", 7.49, "Strong black tea for daily use.", 0, 45),
        ("Organic Almond Milk", "Milk", 13.99, "Plant-based organic almond milk.", 1, 20),
        ("Regular Whole Milk", "Milk", 4.99, "Fresh whole milk for daily consumption.", 0, 60),
        ("Organic Oats", "Oats", 10.50, "Healthy organic rolled oats.", 1, 28),
        ("Instant Oats", "Oats", 5.99, "Quick-cooking instant oats.", 0, 42),
    ]

    cursor.executemany("""
        INSERT INTO products 
        (name, category, price, description, is_organic, stock)
        VALUES (?, ?, ?, ?, ?, ?)
    """, products)

    reviews = [
        (1, 4.8, "Excellent honey. Very natural taste."),
        (1, 4.7, "Good quality and worth the price."),
        (2, 4.6, "Rich flavor and feels very pure."),
        (2, 4.5, "Nice raw honey, good for tea."),
        (3, 4.1, "Good budget honey."),
        (3, 4.0, "Decent taste for the price."),
        (4, 4.9, "Premium quality but expensive."),
        (4, 4.8, "Best honey I have tried."),
        (5, 4.7, "Healthy and creamy peanut butter."),
        (6, 4.2, "Good crunchy texture."),
        (7, 4.6, "Fresh and calming green tea."),
        (8, 4.0, "Strong tea, good value."),
        (9, 4.5, "Good almond milk, slightly expensive."),
        (10, 4.1, "Fresh regular milk."),
        (11, 4.6, "Great oats for breakfast."),
        (12, 4.0, "Quick and convenient oats."),
    ]

    cursor.executemany("""
        INSERT INTO reviews 
        (product_id, rating, review_text)
        VALUES (?, ?, ?)
    """, reviews)

    conn.commit()
    conn.close()

    print(f"Database created successfully at: {DB_PATH}")


if __name__ == "__main__":
    create_database()