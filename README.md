# When and what do online grocery customers reorder?

*SQL analysis of 3M+ online grocery orders, from the point of view of a delivery-slot grocer like Picnic.*

> **Status:** work in progress

## Business questions

1. **Delivery slots:** on which days and at what times do customers want to order, and how should capacity be planned?
2. **Shopping rhythm:** how often do customers come back, and how many follow a weekly pattern?
3. **Anchor products:** which products in a customer's first orders are linked to higher loyalty?
4. **Reorder behaviour:** which departments are reordered most, and what does that mean for buying fresh products and reducing waste?

## Key findings

*(to be filled in at the end: 3 findings with numbers + 1 chart)*

## Recommendations

*(to be filled in at the end)*

## Data

[Instacart Market Basket Analysis](https://www.kaggle.com/c/instacart-market-basket-analysis) (Kaggle): ~3.4M orders from ~206k users, ~50k products.
The data is anonymised and has no calendar dates: only day of week, hour of day and days since the previous order.

## Tools

SQL (DuckDB) · Python (pandas, matplotlib) · Jupyter

## How to run

```bash
pip install -r requirements.txt
# download the 6 CSV files from Kaggle into data/raw/
python build_db.py
jupyter lab
```

## Project structure

```
data/raw/        raw CSV files (not on GitHub)
sql/             final SQL queries, one file per question
notebooks/       analysis notebooks
figures/         charts used in this README
build_db.py      loads the CSVs into a DuckDB database
```
