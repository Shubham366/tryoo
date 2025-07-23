import pandas as pd
import os
import urllib.request
import numpy as np
from configurations.config import SessionLocal, Base, engine
from operations.save_products import save_products_in_chunks

Base.metadata.create_all(bind=engine)

#FETCHING_DATA
url = "https://tyroo-engineering-assesments.s3.us-west-2.amazonaws.com/Tyroo-dummy-data.csv.gz"
local_file = "Tyroo-dummy-data.csv.gz"

pd.set_option('display.max_columns', None)

try:
    if not os.path.exists(local_file):
        urllib.request.urlretrieve(url, local_file)
except Exception as e:
    print(f"Error downloading file: {e}")
    exit(1)

#READING_DATA AND CLEANING
df = pd.read_csv(local_file, compression='gzip')
print(df.columns)
print("Before: Rows =", df.shape[0], ", Columns =", df.shape[1])

df_unique = df.drop_duplicates()
print("After: Rows =", df.shape[0], ", Columns =", df.shape[1])
float_cols = [
    'price', 'current_price', 'promotion_price',
    'discount_percentage', 'rating_avg_value'
]
for col in float_cols:
    df_unique[col] = pd.to_numeric(df_unique[col], errors='coerce')

df_unique['availability'] = df_unique['availability'].astype(str)
df_unique['availability'] = df_unique['availability'].map(
    lambda x: '1' if str(x).lower() in ['in stock', 'yes', 'true', '1'] else '0'
)
df_unique['is_free_shipping'] = df_unique['is_free_shipping'].map(
    lambda x: '1' if str(x).lower() in ['true', '1', 'yes'] else '0'
)
for col in df_unique.columns:
    if pd.api.types.is_float_dtype(df_unique[col]):
        mean_val = df_unique[col].mean()
        df_unique[col].fillna(mean_val, inplace=True)
    else:
        mode = df_unique[col].mode()
        if not mode.empty:
            df_unique[col].fillna(mode[0], inplace=True)




#SAVING_CLEANED_DATA INTO DATABASE
save_products_in_chunks(df_unique, chunk_size=500)
print("Data saved to database in chunks.")


