# Canal_service

---

### Тестовое задание

---

#### Описание:

---

####  *Получение данных через Google API из Google Sheets, создание базы данных, загрузка в БД PostgreSQL данных.*
####    *Получение сообщения в телеграмм, если есть просроченная дата доставки. Представление данных через Django.*  


---


/data_from_sheets

- /bot_telegram  
- /kanalservice (Django project)
- create_db_PostgreSQL.py
- read_Google_sheets.py
- take_data_and_insert.py

---

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/p17m0/Canal_service
```

```
cd data_from_sheets/kanal_service
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```
Заполнить базу данных:

```
cd ..
python take_data_and_insert.py
```

Запустить проект:

```
cd kanal_service
python3 manage.py runserver
```
