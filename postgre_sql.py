#
# CREATE TABLE employees (
# id SERIAL PRIMARY KEY, -- Первичный ключ
# name VARCHAR(100) NOT NULL, -- Имя сотрудника
# age INTEGER CHECK (age >= 18), -- Возраст с ограничением
# department VARCHAR(50), -- Отдел
# salary NUMERIC(10, 2) -- Зарплата с двумя десятичными знаками
# );


# Оконные функции

# ROW_NUMBER()
# назначает уникальный номер каждой строке в пределах
# заданного окна, основанного на ORDER BY. Это полезно для создания
# уникальных идентификаторов для строк в разных группах.


# Получение уникального номера для каждого сотрудника в пределах их отдела.

# SELECT name, department_id, salary,
# ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_num
# FROM employees;


# Получим ранг сотрудников на основе их зарплат в каждом отделе.

# SELECT name, department_id, salary,
# RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_rank
# FROM employees;


# Получим плотный ранг сотрудников на основе их зарплат.

# SELECT name, department_id, salary,
# DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dense_rank
# FROM employees;


# Создадим кумулятивную сумму зарплат всех сотрудников.

# SELECT name, salary,
# SUM(salary) OVER (ORDER BY salary) AS cumulative_salary
# FROM employees;


# Рассчитать общую прибыль для каждого сотрудника, складывая зарплату и премию.
# Если премия NULL, нужно заменить её значением 0.

# SELECT
#   name,
#   salary,
#   COALESCE(bonus, 0) AS bonus,
#   salary + COALESCE(bonus, 0) AS total_income
# FROM
#   employees;
