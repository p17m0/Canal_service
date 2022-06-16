import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="12qw",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")
    cursor = connection.cursor()
    create_table_query = '''CREATE TABLE test
                          (id INT PRIMARY KEY     NOT NULL,
                          zakaz           TEXT    NOT NULL,
                          price_d         REAL,
                          price_r         REAL,
                          date         DATE); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
