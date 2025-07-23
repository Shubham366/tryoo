from configurations.config import SessionLocal, Base, engine
from schema.product_info import Product

def save_products_in_chunks(df, chunk_size=500):
    product_ids = set()
    for start in range(0, len(df), chunk_size):
        end = start + chunk_size
        chunk = df.iloc[start:end]
        session = SessionLocal()
        products = []
        for _, row in chunk.iterrows():
            product_id = row['product_id']
            if product_id in product_ids:
                print(f"Skipping duplicate product_id: {product_id}")
                continue
            product_ids.add(product_id)
            products.append(
                Product(
                    product_id=row['product_id'],
                    sku_id=row['sku_id'],
                    brand_name=row['brand_name'],
                    product_url=row['product_url'],
                    product_big_img=row['product_big_img'],
                    description=row['description'],
                    price=row['price'],
                    current_price=row['current_price'],
                    promotion_price=row['promotion_price'],
                    discount_percentage=row['discount_percentage'],
                    availability=row['availability'],
                    is_free_shipping=row['is_free_shipping'],
                    rating_avg_value=row['rating_avg_value'],
                    venture_category_name_local=row['venture_category_name_local'],
                    venture_category2_name_en=row['venture_category2_name_en'],
                    seller_name=row['seller_name'],
                    business_area=row['business_area'],
                    business_type=row['business_type']
                )
            )
        try:
            session.add_all(products)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error saving chunk: {e}")
        finally:
            session.close()


