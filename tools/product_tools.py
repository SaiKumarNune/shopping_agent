import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "database" / "store.db"


def get_average_rating(product_id: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    result = cursor.execute(
        """
        SELECT AVG(rating)
        FROM reviews
        WHERE product_id = ?
        """,
        (product_id,)
    ).fetchone()

    conn.close()

    return round(result[0], 2) if result[0] else 0


def search_products(query: str, max_price: float | None = None):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    search_term = f"%{query.lower()}%"

    rows = cursor.execute(
        """
        SELECT *
        FROM products
        WHERE LOWER(name) LIKE ?
           OR LOWER(category) LIKE ?
           OR LOWER(description) LIKE ?
        """,
        (search_term, search_term, search_term)
    ).fetchall()

    products = []

    for row in rows:
        product = dict(row)

        if max_price is None or product["price"] <= max_price:
            product["average_rating"] = get_average_rating(product["id"])
            products.append(product)

    conn.close()

    return products