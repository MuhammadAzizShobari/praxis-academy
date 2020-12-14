Setting environment for MariaDB 10.4

C:\WINDOWS\system32>cd c:\xampp\mysql\bin
The system cannot find the path specified.

C:\WINDOWS\system32>cd ..

C:\Windows>cd ..

C:\>cd c:\xampp\mysql\bin
The system cannot find the path specified.

C:\>cd \xampp\mysql\bin
The system cannot find the path specified.

C:\>cd xamppp\mysql\bin

C:\xamppp\mysql\bin>mysql -uroot -p
Enter password:
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)

C:\xamppp\mysql\bin>mysql -uroot -p
Enter password:
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)

C:\xamppp\mysql\bin>mysql -uroot
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)

C:\xamppp\mysql\bin>mysql -u root -proot
Warning: Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 5.5.5-10.4.12-MariaDB mariadb.org binary distribution

Copyright (c) 2000, 2014, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> select user, host from mysql.user
    -> end;
+------+-----------------+
| User | Host            |
+------+-----------------+
| root | 127.0.0.1       |
| root | ::1             |
| root | desktop-2n35ppk |
| root | localhost       |
+------+-----------------+
4 rows in set (0.37 sec)

mysql> select user, host from mysql.user;
+------+-----------------+
| User | Host            |
+------+-----------------+
| root | 127.0.0.1       |
| root | ::1             |
| root | desktop-2n35ppk |
| root | localhost       |
+------+-----------------+
4 rows in set (0.00 sec)

mysql> create user 'aziz'@'localhost';
Query OK, 0 rows affected (0.11 sec)

mysql> create database sekolah;
Query OK, 1 row affected (0.08 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sekolah            |
| test               |
+--------------------+
5 rows in set (0.08 sec)

mysql> use sekolah database;
Database changed
mysql> create database mahasiswa;
Query OK, 1 row affected (0.00 sec)

mysql> use mahasiswa;
Database changed
mysql> create table mhs (
    -> nim integer not null primary key,
    -> nama varchar (50),
    -> sks interger
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'interger
)' at line 4
mysql> create table mhs (
    -> Nim interger not null primary key,
    -> Nama varchar (25),
    -> SKS interger
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'interger not null primary key,
Nama varchar (25),
SKS interger
)' at line 2
mysql> );create table mhs (nama varchar(30),nim interger not null primary key, umur int(2), alamat varchar(50));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ')' at line 1
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'interger not null primary key, umur int(2), alamat varchar(50))' at line 1
mysql> );create table mhs (nama varchar(30), umur int(2), alamat varchar(50));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ')' at line 1
Query OK, 0 rows affected (0.28 sec)

mysql> desc mhs;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| nama   | varchar(30) | YES  |     | NULL    |       |
| umur   | int(2)      | YES  |     | NULL    |       |
| alamat | varchar(50) | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
3 rows in set (0.06 sec)

mysql> INSERT INTO mhs('rizki', '99', 'gunung kidul', 'arwanda isman', '98', 'lord kazuma', '20');
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ''rizki', '99', 'gunung kidul', 'arwanda isman', '98', 'lord kazuma', '20')' at line 1
mysql> INSERT INTO mhs VALUES ('rizki', '99', 'gunung kidul', 'arwanda isman', '98', 'lord kazuma', '20');
ERROR 1136 (21S01): Column count doesn't match value count at row 1
mysql> INSERT INTO mhs VALUES ('rizki', '99', 'gunung kidul');
Query OK, 1 row affected (0.13 sec)

mysql> INSERT INTO mhs VALUES ('riska', '98', 'sleman');
Query OK, 1 row affected (0.11 sec)

mysql> INSERT INTO mhs VALUES ('rizke', '97', 'isekai');
Query OK, 1 row affected (0.18 sec)

mysql> SELECT * FROM mhs;
+-------+------+--------------+
| nama  | umur | alamat       |
+-------+------+--------------+
| rizki |   99 | gunung kidul |
| riska |   98 | sleman       |
| rizke |   97 | isekai       |
+-------+------+--------------+
3 rows in set (0.00 sec)

mysql>