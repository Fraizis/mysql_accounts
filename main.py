from loguru import logger
from mysql import connector

from settings import user_data

clients = """
    CREATE TABLE IF NOT EXISTS clients (
        id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(200) NOT NULL,
        place_of_birth VARCHAR(200) NOT NULL,
        date_of_birth DATE NOT NULL,
        address VARCHAR(200) NOT NULL,
        passport VARCHAR(200) NOT NULL
);
"""

tarifs = """
CREATE TABLE IF NOT EXISTS tarifs (
        id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100) NOT NULL,
        cost DECIMAL(10,2) NOT NULL
);
"""
product_type = """
CREATE TABLE IF NOT EXISTS product_type (
        id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(20) NOT NULL,
        begin_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        end_date DATETIME,
        tarif_ref INT UNSIGNED NOT NULL,
    
        FOREIGN KEY (tarif_ref) REFERENCES tarifs (id)
);
"""

products = """
CREATE TABLE IF NOT EXISTS products (
        id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        product_type_id INT UNSIGNED NOT NULL,
        name VARCHAR(200) NOT NULL,
        client_ref INT UNSIGNED NOT NULL,
        open_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        close_date DATETIME,
    
        FOREIGN KEY (product_type_id) REFERENCES product_type (id),
        FOREIGN KEY (client_ref) REFERENCES clients (id)
);
"""

accounts = """
CREATE TABLE IF NOT EXISTS accounts (
        id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(200) NOT NULL,
        saldo DECIMAL(10,2) DEFAULT 0,
        client_ref INT UNSIGNED NOT NULL,
        open_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        close_date DATETIME,
        product_ref INT UNSIGNED NOT NULL,
        acc_num CHAR(20) NOT NULL,

        FOREIGN KEY (client_ref) REFERENCES clients (id),
        FOREIGN KEY (product_ref) REFERENCES products (id)
);
"""

records = """
CREATE TABLE IF NOT EXISTS records (
        id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        dt BIT(1) DEFAULT 0,
        acc_ref INT UNSIGNED NOT NULL,
        oper_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        `sum` DECIMAL(10,2) DEFAULT 0,
    
        FOREIGN KEY (acc_ref) REFERENCES accounts (id)
);
"""

insert_tarifs = """
INSERT INTO tarifs (name, cost)
VALUES (%s, %s); 
"""

val_tarifs = [
    ('Тариф за выдачу кредита', 10),
    ('Тариф за открытие счета', 10),
    ('Тариф за обслуживание карты', 10)
]

insert_product_type = """
INSERT INTO product_type (name, tarif_ref) 
VALUES (%s, %s);
"""

val_product_type = [
    ('кредит', 1),
    ('депозит', 2),
    ('карта', 2)
]

insert_clients = """
INSERT INTO clients (
	name,
	place_of_birth ,
	date_of_birth,
	address,
	passport
	)
VALUES (%s, %s, %s, %s, %s);
"""

val_clients = [
    (
        'Сидоров Иван Петрович',
        'Россия, Московская облать, г. Пушкин',
        '01.01.2001',
        'Россия, Московская облать, г. Пушкин, ул. Грибоедова, д. 5',
        '2222 555555, выдан ОВД г. Пушкин, 10.01.2015'
    ),
    (
        'Иванов Петр Сидорович',
        'Россия, Московская облать, г. Клин',
        '2001.01.01',
        'Россия, Московская облать, г. Клин, ул. Мясникова, д. 3',
        '4444 666666, выдан ОВД г. Клин, 10.01.2015'
    ),
    (
        'Петров Сидр Иванович',
        'Россия, Московская облать, г. Балашиха',
        '01.01.2001',
        'Россия, Московская облать, г. Балашиха, ул. Пушкина, д. 7',
        '4444 666666, выдан ОВД г. Клин, 10.01.2015'
    )
]

insert_products = """
INSERT INTO products (
	product_type_id,
	name,
	client_ref
	) 
VALUES (%s, %s, %s);
"""

val_products = [
    (1, 'Кредитный договор с Сидоровым И.П.', 1),
    (2, 'Депозитный договор с Сидоровым И.П.', 1),
    (3, 'Карточный договор с Сидоровым И.П.', 1),
    (1, 'Кредитный договор с Сидоровым И.П.', 1),
    (2, 'Депозитный договор с Сидоровым И.П.', 1),
    (3, 'Карточный договор с Сидоровым И.П.', 1),
    (2, 'Депозитный договор с Иванов П.С.', 2),
    (2, 'Депозитный договор с Иванов П.С.', 2),
    (1, 'Кредитный договор с Иванов П.С.', 2)
]

insert_accounts = """
INSERT INTO accounts (
	name,
	saldo,
	client_ref,
	product_ref,
	acc_num
	) 
VALUES (%s, %s, %s, %s, %s); 
"""

val_accounts = [
    ('Кредитный счет для Сидорова И.П.', -2000, 1, 1, '45502810401000100022'),
    ('Депозитный счет для Сидорова И.П.', 6000, 1, 2, '42301810400000000001'),
    ('Карточный счет для Сидорова И.П.', 8000, 1, 3, '40817810700000006001'),
    ('Кредитный счет для Сидорова И.П.', -4000, 1, 4, '45502810401020030022'),
    ('Депозитный счет для Сидорова И.П.', 5000, 1, 5, '42301810400000000001'),
    ('Карточный счет для Сидорова И.П.', 11000, 1, 6, '40817810700000000001'),
    ('Депозитный счет для Иванов П.С.', -3000, 2, 7, '45502810401020000022'),
    ('Депозитный счет для Иванов П.С.', 5000, 2, 8, '42301810400050000001'),
    ('Кредитный счет для Иванов П.С.', 15000, 2, 9, '45502810401020000022')
]

insert_records = """
INSERT INTO records (
	dt,
	`sum`,
	acc_ref
	)
VALUES (%s, %s, %s); 
"""

val_records = [
    (1, 5000, 1),
    (0, 1000, 1),
    (0, 2000, 1),
    (0, 3000, 1),
    (1, 5000, 1),
    (0, 3000, 1),
    (0, 10000, 2),
    (1, 1000, 2),
    (1, 2000, 2),
    (1, 5000, 2),
    (0, 6000, 2),
    (0, 120000, 3),
    (1, 1000, 3),
    (1, 2000, 3),
    (1, 5000, 3),
    (0, 5000, 9),
    (1, 5000, 9),
    (0, 7000, 9),
    (1, 5000, 9),
    (0, 5000, 7),
    (0, 10000, 7),
    (1, 7000, 7),
    (1, 12000, 7)
]


def mysql_connect():
    try:
        conn = connector.connect(**user_data)
        cur = conn.cursor()
        logger.success("Connected to database...")

        cur.execute("SELECT VERSION()")
        version = cur.fetchone()

        logger.info(f"MySQL Version: {version}")

        return conn

    except connector.Error as err:
        logger.error(f"Error: {err}")


def create_and_insert_tables(conn):
    try:
        cur = conn.cursor()

        tables = [clients, tarifs, product_type, products, accounts, records]

        insert_data = [
            insert_clients, insert_tarifs, insert_product_type,
            insert_products, insert_accounts, insert_records
        ]
        values = [
            val_clients, val_tarifs, val_product_type,
            val_products, val_accounts, val_records
        ]
        data = zip(insert_data, values)

        cur.execute(
            "SELECT 1 FROM information_schema.tables "
            "WHERE table_schema=%s AND table_name=%s LIMIT 1",
            (user_data['database'], 'clients')
        )

        tables_check = cur.fetchone()

        if tables_check is None:
            for table in tables:
                cur.execute(table)
                logger.success(f"Executed query: {table}")
        else:
            logger.info(f"Tables already exists")

        cur.execute(
            "SELECT 1 FROM clients "
            "WHERE id = 1"
        )

        vals_check = cur.fetchone()

        if vals_check is None:
            for i, v in data:
                cur.executemany(i, v)
                logger.success(f"Inserting data: {i}")
                logger.success(v)

            conn.commit()
        else:
            logger.info(f"Data already inserted to tables")

        cur.close()
        conn.close()

    except connector.Error as e:
        conn.rollback()
        logger.error(f"Error: {e}")


if __name__ == '__main__':
    conn = mysql_connect()
    create_and_insert_tables(conn)
