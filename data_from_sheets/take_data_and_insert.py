from datetime import date as dt
import time
import psycopg2
import requests

from typing import Any

from read_Google_sheets import read
from bot_telegram.bot import bot

data_central_bank: Any = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
VALUE_RUB: float = data_central_bank['Valute']['USD']['Value']
data_google_sheet: list = read()
data: list = data_google_sheet[1:]
all_id: list = []


def insert(*args: tuple) -> None:
    """
    Выполнение SQL-запроса для вставки данных в таблицу
    """
    pk, order, price_d, price_r, date = args
    try:
        insert_query = """ INSERT INTO page_orders (id, zakaz, price_d, price_r, date)
        VALUES (%s, %s, %s, %s, %s)"""
        item_tuple = (pk, order, price_d, price_r, date)
        cursor.execute(insert_query, item_tuple)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print("Запись успешно вставлена")


def update(*args: tuple) -> None:
    """
    Выполнение SQL-запроса для обновления таблицы
    """
    pk, order, price_d, price_r, date = args
    item_tuple = (order, price_d, price_r, date, pk)
    try:
        update_query = """UPDATE page_orders SET zakaz = %s, price_d = %s,
        price_r = %s, date = %s  WHERE id = %s"""
        cursor.execute(update_query, item_tuple)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print("Запись успешно изменена")


def delete(id: int) -> None:
    """
    Выполнение SQL-запроса для удаления таблицы
    """
    delete_query = f"""DELETE FROM page_orders WHERE id = {id}"""
    cursor.execute(delete_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Запись успешно удалена")


while True:
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      password="12qw",
                                      host="localhost",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()
        print("Запись пошла")
        
        for datum in data:
            pk, order, price_d, date = datum
            all_id.append(int(pk))
            price_d = float(price_d)
            price_r = round(price_d*VALUE_RUB, 2)
            cursor.execute(f"SELECT * from page_orders where id = {pk}")
            new_datum: tuple[str, str, float, float, str] = (pk,
                                                             order,
                                                             price_d,
                                                             price_r,
                                                             date)
            if cursor.fetchall() == []:
                insert(*new_datum)
            else:
                update(*new_datum)

        cursor.execute("SELECT * from page_orders")
        record = cursor.fetchall()
        today = dt.today()
        
        for datum in record:
            time_to_deliver = True if today >= datum[4] else False
            if time_to_deliver:
                bot(datum[1])
            if datum[0] in all_id:
                continue
            else:
                delete(datum[0])

    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

    print("Update...")
    time.sleep(1000)
