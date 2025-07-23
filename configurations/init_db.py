from sqlalchemy import create_engine
from schema.product_info import Base

DATABASE_URL = "sqlite:///db.sqlite3"

def init_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    print("Database and tables created.")

if __name__ == "__main__":
    init_db()

    
    