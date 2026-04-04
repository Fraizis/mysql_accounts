# DCL


# GRANT — даёт разрешения пользователям или ролям
# (например, на просмотр, вставку, обновление или удаление данных).

# GRANT SELECT, INSERT ON employees TO Ankit-Roy


# REVOKE — отзывает разрешения, которые были ранее даны пользователю.

# REVOKE SELECT, INSERT ON employees FROM john_doe


# DENY — запрещает разрешения пользователям или ролям (например, на удаление данных).

# DENY DELETE ON employees TO user123


# вывести инфо о текущем пользователе

# SELECT CURRENT_USER();
# SELECT user();

# вывести список всех пользователей на сервере (с информацией о правах доступа)

# SELECT * FROM mysql.user;

# вывести права доступа текущего пользователя

# SHOW grants;

# вывести права доступа указанного пользователя

# SHOW grants FOR 'root'@'localhost';

# создать пользователя и указать ему пароль

# CREATE USER 'john_admin'@'localhost' IDENTIFIED BY '12345';
# CREATE USER 'max_tester'@'localhost' IDENTIFIED BY '12345';

# раздать пользователю максимальные права на всем сервере

# GRANT ALL PRIVILEGES ON *.* TO 'john_admin'@'localhost';
# проверить права
# SHOW grants FOR 'john_admin'@'localhost';

# создать пользователя без указания пароля

# CREATE USER 'alex_dev'@'localhost';

# задать пароль пользователю

# SET PASSWORD FOR 'alex_dev'@'localhost' = '12345';

# задать пользователю максимальные права на указанную БД

# GRANT ALL PRIVILEGES ON telegram.* TO 'alex_dev'@'localhost';

# проверить результат

# SHOW grants FOR 'alex_dev'@'localhost';

# задать пользователю указанный набор прав (DDL + DML) на указанной БД

# GRANT CREATE, ALTER, DROP, SELECT, UPDATE, INSERT, DELETE
# ON telegram.*
# TO 'max_tester'@'localhost';

# проверить

# SHOW grants FOR 'max_tester'@'localhost';

# забрать права на указанные команды у пользователя

# REVOKE CREATE, ALTER, DROP
# ON telegram.*
# FROM 'max_tester'@'localhost';

# проверить

# SHOW grants FOR 'max_tester'@'localhost';

# создать пользователя с необходимостью менять пароль раз в 180 дней и прочими ограничениями

# CREATE USER 'paul_manager'@'localhost'
# PASSWORD EXPIRE INTERVAL 180 DAY
# FAILED_LOGIN_ATTEMPTS 3
# PASSWORD_LOCK_TIME 2;

# сменить/задать пароль пользователю

# SET PASSWORD FOR 'paul_manager'@'localhost' = '12345';

# задать права доступа только на чтение для указанного пользователя

# GRANT SELECT ON telegram.* TO 'paul_manager'@'localhost';

# забрать все права у пользователя на указанную БД

# REVOKE ALL PRIVILEGES ON telegram.* FROM 'paul_manager'@'localhost';

# выдать права только на чтение и только на указанные поля

# GRANT SELECT(firstname, lastname) ON telegram.users TO 'paul_manager'@'localhost';

# удалить пользователя

# DROP USER 'paul_manager'@'localhost';


# создать роли

# CREATE ROLE '_admin';
# CREATE ROLE '_admin', '_developer', '_tester', '_manager';

# посмотреть определение таблицы user в БД mysql

# SHOW COLUMNS FROM mysql.user;

# вывести содержимое указанной таблицы

# SELECT * FROM mysql.user;

# раздать права ролям (по аналогии с пользователями в прошлом уроке)

# GRANT ALL privileges ON *.* TO '_admin';

# GRANT ALL privileges ON telegram.* TO '_developer';

# GRANT CREATE, ALTER, DROP, SELECT, UPDATE, INSERT, DELETE
# ON telegram.*
# TO '_tester';

# GRANT SELECT ON telegram.* TO '_manager';

# забрать права у пользователей

# REVOKE ALL ON *.*
# FROM
# 	`john_admin`@`localhost`,
# 	`alex_dev`@`localhost`,
# 	`max_tester`@`localhost`,
# 	`paul_manager`@`localhost`;

# проверить права пользователей

# SHOW GRANTS FOR `john_admin`@`localhost`;
# SHOW GRANTS FOR `alex_dev`@`localhost`;

# присвоить группы пользователям

# GRANT '_admin' TO `john_admin`@`localhost`;
# GRANT '_developer' TO `alex_dev`@`localhost`;
# GRANT '_tester' TO `max_tester`@`localhost`;
# GRANT '_manager' TO `paul_manager`@`localhost`;

# проверить роль текущего пользователя

# SELECT CURRENT_ROLE();

# установить роли по умолчанию (чтобы роль применялась автоматически для пользователей)

# SET DEFAULT ROLE ALL TO
# 	`john_admin`@`localhost`,
# 	`alex_dev`@`localhost`,
# 	`max_tester`@`localhost`,
# 	`paul_manager`@`localhost`;

# забрать роль у пользователя

# REVOKE '_manager' FROM `paul_manager`@`localhost`;

# создать нового менеджера

# CREATE USER 'anna_manager'@'localhost' IDENTIFIED BY '12345'
# PASSWORD EXPIRE INTERVAL 180 DAY
# FAILED_LOGIN_ATTEMPTS 3
# PASSWORD_LOCK_TIME 2;

# присвоить группу новому пользователю

# GRANT '_manager' TO `anna_manager`@`localhost`;

# установить роль по умолчанию для него

# SET DEFAULT ROLE ALL TO `anna_manager`@`localhost`;

# удалить роль

# DROP ROLE '_manager';


# # создание VIEW для менеджера

# DROP VIEW IF EXISTS telegram.v_telegram_user_names;
# CREATE VIEW v_telegram_user_names AS
# SELECT
#   firstname,
#   lastname
# FROM telegram.users;


# GRANT SELECT
# ON telegram.v_telegram_user_names
# TO '_manager';
