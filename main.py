

db_create = """
CREATE DATABASE IF NOT EXISTS schift;
"""

tables_create = """
USE schift;

CREATE TABLE IF NOT EXISTS accounts (
id SERIAL,
name VARCHAR(100) NOT NULL,
saldo DECIMAL(10,2) DEFAULT 0,
client_ref INT UNSIGNED NOT NULL,
open_date


)

"""
