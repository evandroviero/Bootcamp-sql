import os
from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import load_dotenv 


load_dotenv()

db_name = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}")


query = """
SELECT distinct employee_id, ship_via
FROM orders
"""

with engine.connect() as connection:
    result = connection.execute(text(query)).mappings()  
    result_list = list(result) 
    df = pd.DataFrame(result_list)
    
print(df)