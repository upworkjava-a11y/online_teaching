from django.conf import settings

from .leetcode_sql import LEETCODE_SCHEMA_SQL, LEETCODE_SEED_SQL

CUSTOMERS_SCHEMA = """
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT,
    registration_date DATE
);
"""

TRANSACTIONS_SCHEMA = """
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_type TEXT NOT NULL
);
"""

PRODUCTS_SCHEMA = """
CREATE TABLE IF NOT EXISTS shop_products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    price NUMERIC(12, 2) NOT NULL
);
"""

ORDERS_SCHEMA = """
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    order_date DATE NOT NULL
);
"""

SEED_SQL = """
DELETE FROM orders;
DELETE FROM transactions;
DELETE FROM shop_products;
DELETE FROM customers;

INSERT INTO customers (id, name, city, registration_date) VALUES
(1, 'Ali Valiyev', 'Toshkent', '2023-01-12'),
(2, 'Malika Karimova', 'Samarqand', '2023-03-04'),
(3, 'Javohir Saidov', 'Buxoro', '2023-05-21'),
(4, 'Dilnoza Yusupova', 'Toshkent', '2024-01-08'),
(5, 'Sardor Ergashev', 'Andijon', '2024-02-17');

INSERT INTO transactions (id, customer_id, amount, transaction_date, transaction_type) VALUES
(1, 1, 120000, '2024-03-01', 'debit'),
(2, 1, 45000, '2024-03-04', 'debit'),
(3, 1, 80000, '2024-03-10', 'credit'),
(4, 1, 15000, '2024-03-12', 'debit'),
(5, 1, 22000, '2024-03-18', 'debit'),
(6, 1, 31000, '2024-03-22', 'debit'),
(7, 2, 50000, '2024-03-02', 'debit'),
(8, 2, 70000, '2024-03-11', 'credit'),
(9, 3, 150000, '2024-03-05', 'debit'),
(10, 3, 20000, '2024-03-19', 'debit'),
(11, 4, 90000, '2024-03-07', 'debit'),
(12, 5, 10000, '2024-03-09', 'credit');

INSERT INTO shop_products (id, name, category, price) VALUES
(1, 'Noutbuk', 'electronics', 8500000),
(2, 'Sichqoncha', 'electronics', 120000),
(3, 'Daftar', 'stationery', 15000),
(4, 'Ruchka', 'stationery', 5000),
(5, 'Monitor', 'electronics', 2100000);

INSERT INTO orders (id, customer_id, product_id, quantity, order_date) VALUES
(1, 1, 1, 1, '2024-03-01'),
(2, 1, 3, 5, '2024-03-04'),
(3, 2, 2, 2, '2024-03-02'),
(4, 3, 5, 1, '2024-03-05'),
(5, 4, 4, 10, '2024-03-07'),
(6, 1, 2, 1, '2024-03-18');
"""

SAMPLE_PREVIEW = {
    "customers": {
        "columns": ["id", "name", "city", "registration_date"],
        "rows": [
            [1, "Ali Valiyev", "Toshkent", "2023-01-12"],
            [2, "Malika Karimova", "Samarqand", "2023-03-04"],
            [3, "Javohir Saidov", "Buxoro", "2023-05-21"],
        ],
    },
    "transactions": {
        "columns": ["id", "customer_id", "amount", "transaction_date", "transaction_type"],
        "rows": [
            [1, 1, 120000, "2024-03-01", "debit"],
            [2, 1, 45000, "2024-03-04", "debit"],
            [7, 2, 50000, "2024-03-02", "debit"],
        ],
    },
    "products": {
        "columns": ["id", "name", "category", "price"],
        "rows": [
            [1, "Noutbuk", "electronics", 8500000],
            [3, "Daftar", "stationery", 15000],
        ],
    },
    "orders": {
        "columns": ["id", "customer_id", "product_id", "quantity", "order_date"],
        "rows": [
            [1, 1, 1, 1, "2024-03-01"],
            [2, 1, 3, 5, "2024-03-04"],
        ],
    },
}


def seed_sandbox_database() -> None:
    cfg = settings.SANDBOX_DATABASE
    statements = [
        CUSTOMERS_SCHEMA,
        TRANSACTIONS_SCHEMA,
        PRODUCTS_SCHEMA,
        ORDERS_SCHEMA,
        SEED_SQL,
        LEETCODE_SCHEMA_SQL,
        LEETCODE_SEED_SQL,
    ]
    if cfg.get("ENGINE") == "sqlite" or not cfg.get("HOST"):
        import sqlite3
        from pathlib import Path

        Path(cfg["NAME"]).parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(cfg["NAME"])
        try:
            for statement in statements:
                conn.executescript(statement)
            conn.commit()
        finally:
            conn.close()
        return

    import psycopg

    with psycopg.connect(
        dbname=cfg["NAME"],
        user=cfg["ADMIN_USER"],
        password=cfg["ADMIN_PASSWORD"],
        host=cfg["HOST"],
        port=cfg["PORT"],
        autocommit=True,
    ) as conn:
        with conn.cursor() as cursor:
            for statement in statements:
                cursor.execute(statement)
            cursor.execute("GRANT SELECT ON ALL TABLES IN SCHEMA public TO %s" % _quote_ident(cfg["USER"]))


def _quote_ident(name: str) -> str:
    return '"' + name.replace('"', "") + '"'
