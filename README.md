# Tyroo Backend Data Processing

## Overview

This project processes a large product dataset, cleans and transforms the data, and saves it into a SQLite3 database using SQLAlchemy ORM. The workflow is optimized for performance and reliability, including chunked database commits, error handling, and efficient data type conversions.

---

## Columns Used

The following columns from the dataset are used and mapped to the database:

- `product_id`
- `sku_id`
- `brand_name`
- `product_url`
- `product_big_img`
- `description`
- `price`
- `current_price`
- `promotion_price`
- `discount_percentage`
- `availability` (converted to boolean: 1 for True, 0 for False)
- `is_free_shipping` (converted to boolean: 1 for True, 0 for False)
- `rating_avg_value`
- `venture_category_name_local`
- `venture_category2_name_en`
- `seller_name`
- `business_area`
- `business_type`

---

## Columns Not Used

Some columns were excluded as they were not useful for the current analysis or were redundant, such as:

- Multiple image columns (`product_small_img`, `product_medium_img`, `image_url_2`, `image_url_3`, `image_url_4`, `image_url_5`)
- Deep links (`deeplink`)
- Seller URLs (`seller_url`)
- Commission rates (`platform_commission_rate`, `product_commission_rate`, `bonus_commission_rate`)
- Category columns with less relevance (`venture_category1_name_en`, `venture_category3_name_en`)
- Review and rating counts (`number_of_reviews`, `seller_rating`)
- Product name (`product_name`)

> **Note:** Principal Component Analysis (PCA) or other feature selection techniques can be used in the future to further determine the most useful columns for modeling or analytics.

---

## Data Cleaning & Transformation

- **Boolean Conversion:**  
  - `availability` and `is_free_shipping` are converted to boolean (0 for False, 1 for True) based on common truthy values (`'yes'`, `'true'`, `'1'`, etc.).
- **Null Value Handling:**  
  - For float columns, null values are replaced with the column's average (mean).
  - For non-float columns, null values are replaced with the mode (most frequent value) of the column.
- **Duplicate Handling:**  
  - Duplicate rows are dropped.
  - Duplicate `product_id` entries are skipped during database insertion.
- **Local File Caching:**  
  - The dataset is downloaded and saved locally only if not already present, to avoid unnecessary repeated downloads.

---

## Database

- **Database:** SQLite3 (`db.sqlite3`)
- **ORM:** SQLAlchemy
- **Chunked Inserts:** Data is inserted in chunks of 500 rows to optimize performance and reduce commit delays.
- **Error Handling:** All database operations are wrapped with error handling to ensure reliability.
- **Data addition:** Added only few datas due to git limit size file. After running main.py we will get approx 3 lakhs data in db.

---

## Requirements

All required Python modules and their versions are listed in `requirements.txt`.

---

## How to Run

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the main script:
    ```bash
    python main.py
    ```
3. The cleaned data will be saved to the SQLite database (`db.sqlite3`).

