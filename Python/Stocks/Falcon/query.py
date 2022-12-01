sql_create_stock_table = """ 
CREATE TABLE IF NOT EXISTS stock (
    id integer PRIMARY KEY,
    stock_code text NOT NULL,
    c_name text NOT NULL,
    time text NOT NULL,
    price text NOT NULL,
    min_value text,
    max_value text,
    volume text
);
"""
sql_create_fii_table = """
CREATE TABLE IF NOT EXISTS fii (
    id integer PRIMARY KEY,
    fii_code text NOT NULL,
    c_name text NOT NULL,
    time text NOT NULL,
    price REAL NOT NULL,
    min_value REAL,
    max_value REAL
);
"""

table_list = [sql_create_stock_table, sql_create_fii_table]