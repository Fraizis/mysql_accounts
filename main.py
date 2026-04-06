import sqlite3


mysql_uri = 'sql_test.db'

create_tables = """CREATE TABLE IF NOT EXISTS clients (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(200) NOT NULL,
	place_of_birth VARCHAR(200) NOT NULL,
	date_of_birth DATE NOT NULL,
	address VARCHAR(200) NOT NULL,
	passport VARCHAR(200) NOT NULL
);

    CREATE TABLE IF NOT EXISTS tarifs (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(100) NOT NULL,
	cost DECIMAL(10,2) NOT NULL
);

    CREATE TABLE IF NOT EXISTS product_type (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(20) NOT NULL,
	begin_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	end_date DATETIME,
	tarif_ref BIGINT UNSIGNED NOT NULL,

	FOREIGN KEY (tarif_ref) REFERENCES tarifs (id)
);

    CREATE TABLE IF NOT EXISTS products (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	product_type_id BIGINT UNSIGNED NOT NULL,
	name VARCHAR(200) NOT NULL,
	client_ref BIGINT UNSIGNED NOT NULL,
	open_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	close_date DATETIME,

	FOREIGN KEY (product_type_id) REFERENCES product_type (id),
	FOREIGN KEY (client_ref) REFERENCES clients (id)
);

    CREATE TABLE IF NOT EXISTS accounts (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(200) NOT NULL,
	saldo DECIMAL(10,2) DEFAULT 0,
	client_ref BIGINT UNSIGNED NOT NULL,
	open_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	close_date DATETIME,
	product_ref BIGINT UNSIGNED NOT NULL,
	acc_num CHAR(20) NOT NULL,

	FOREIGN KEY (client_ref) REFERENCES clients (id),
	FOREIGN KEY (product_ref) REFERENCES products (id)
);

    CREATE TABLE IF NOT EXISTS records (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	dt BIT(1) DEFAULT 0,
	acc_ref BIGINT UNSIGNED NOT NULL,
	oper_date DATETIME DEFAULT CURRENT_TIMESTAMP,
	`sum` DECIMAL(10,2) DEFAULT 0,

	FOREIGN KEY (acc_ref) REFERENCES accounts (id)
);
"""

insert_tables = """
INSERT INTO tarifs (name, cost)
VALUES 
    ('Тариф за выдачу кредита', 10), 
    ('Тариф за открытие счета', 10),
    ('Тариф за обслуживание карты', 10);
    
INSERT INTO product_type (name, tarif_ref) 
VALUES 
    ('кредит', 1),
    ('депозит', 2),
    ('карта', 2)
;

INSERT INTO clients (
	name,
	place_of_birth ,
	date_of_birth,
	address,
	passport
	)
VALUES 
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
	);
	
INSERT INTO products (
	product_type_id,
	name,
	client_ref
	) 
VALUES 
	(1, 'Кредитный договор с Сидоровым И.П.', 1),
	(2, 'Депозитный договор с Сидоровым И.П.', 1),
	(3, 'Карточный договор с Сидоровым И.П.', 1),
	(1, 'Кредитный договор с Сидоровым И.П.', 1),
	(2, 'Депозитный договор с Сидоровым И.П.', 1),
	(3, 'Карточный договор с Сидоровым И.П.', 1),
	(2, 'Депозитный договор с Иванов П.С.', 2),
	(2, 'Депозитный договор с Иванов П.С.', 2),
	(1, 'Кредитный договор с Иванов П.С.', 2)
;

INSERT INTO accounts (
	name,
	saldo,
	client_ref,
	product_ref,
	acc_num
	) 
VALUES 
	('Кредитный счет для Сидорова И.П.', -2000, 1,  1, '45502810401000100022'),
	('Депозитный счет для Сидорова И.П.', 6000, 1, 2, '42301810400000000001'),
	('Карточный счет для Сидорова И.П.', 8000, 1, 3, '40817810700000006001'),
	('Кредитный счет для Сидорова И.П.', -4000, 1,  4, '45502810401020030022'),
	('Депозитный счет для Сидорова И.П.', 5000, 1, 5, '42301810400000000001'),
	('Карточный счет для Сидорова И.П.', 11000, 1, 6, '40817810700000000001'),
	('Депозитный счет для Иванов П.С.', -3000, 2,  7, '45502810401020000022'),
	('Депозитный счет для Иванов П.С.', 5000, 2, 8, '42301810400050000001'),
	('Кредитный счет для Иванов П.С.', 15000, 2,  9, '45502810401020000022')
;

INSERT INTO records (
	dt,
	`sum`,
	acc_ref
	)
VALUES 
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
;
"""


def create_db_tables_insert():
    with sqlite3.connect(mysql_uri) as conn:
        cursor = conn.cursor()

        cursor.executescript(create_tables)
        cursor.executescript(insert_tables)

        conn.commit()


if __name__ == '__main__':
    create_db_tables_insert()
