"""
Build a local DuckDB database from the Instacart CSV files.

Usage (from the project root):
    python build_db.py

Expects the 6 Kaggle CSV files in data/raw/ and creates data/instacart.duckdb.
"""
from pathlib import Path
import duckdb

RAW = Path("data/raw")
DB = Path("data/instacart.duckdb")

TABLES = {
    "orders": "orders.csv",
    "order_products_prior": "order_products__prior.csv",
    "order_products_train": "order_products__train.csv",
    "products": "products.csv",
    "aisles": "aisles.csv",
    "departments": "departments.csv",
}

missing = [f for f in TABLES.values() if not (RAW / f).exists()]
if missing:
    raise SystemExit(f"Missing files in {RAW}/: {', '.join(missing)}")

con = duckdb.connect(str(DB))
for table, file in TABLES.items():
    path = (RAW / file).as_posix()
    con.execute(f"CREATE OR REPLACE TABLE {table} AS SELECT * FROM read_csv_auto('{path}', header=true)")
    n = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    print(f"{table:<22} {n:>12,} rows")

# Convenience view: all products of all orders that have product details
con.execute("""
    CREATE OR REPLACE VIEW order_products AS
    SELECT *, 'prior' AS source FROM order_products_prior
    UNION ALL
    SELECT *, 'train' AS source FROM order_products_train
""")
con.close()
print(f"\nDone -> {DB}")
