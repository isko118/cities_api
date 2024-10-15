
# Cities API

Cities API — это приложение на основе FastAPI, которое позволяет пользователям добавлять, удалять и получать информацию о городах из базы данных, а также находить два ближайших города по заданным координатам (широта и долгота).

## Возможности

- Добавление городов в базу данных
- Удаление городов по ID
- Получение списка городов
- Поиск двух ближайших городов по координатам (широта/долгота)
- Автоматическое получение координат города с помощью внешних API (например, OpenWeatherMap)

---

## Установка и запуск проекта

1. Клонируйте репозиторий и перейдите в директорию проекта:
   ```bash
   git clone https://github.com/your-repo/cities-api.git
   cd cities-api
   ```

2. Установите и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Для macOS/Linux
   venv\Scripts\activate    # Для Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Создайте файл `.env` в директории `app/` и добавьте в него ваш API-ключ от OpenWeatherMap:
   ```
   OPENWEATHERMAP_API_KEY=ваш_ключ
   ```

   Для получения API-ключа зарегистрируйтесь на [OpenWeatherMap](https://openweathermap.org/), создайте новый API-ключ и вставьте его в `.env` файл.

5. Запустите сервер:
   ```bash
   uvicorn app.main:app --reload
   ```

   Приложение будет доступно по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

6. Перейдите на [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs), чтобы получить доступ к Swagger UI

---

## Примеры использования через Swagger UI

### 1. Добавление нового города
- Откройте [Swagger UI](http://127.0.0.1:8000/docs)
- Найдите `POST /cities`
- Нажмите "Try it out" и введите название города, например, `"Moscow"`, затем нажмите "Execute".
- Это добавит город и автоматически получит его координаты с помощью внешнего API.

### 2. Удаление города
- Откройте [Swagger UI](http://127.0.0.1:8000/docs)
- Найдите `DELETE /cities/{city_id}`
- Введите `city_id` города, который вы хотите удалить, и нажмите "Execute".

### 3. Получение списка городов
- Откройте [Swagger UI](http://127.0.0.1:8000/docs)
- Найдите `GET /cities`
- Нажмите "Try it out", затем "Execute", чтобы получить список всех городов.

### 4. Поиск ближайших городов по координатам
- Откройте [Swagger UI](http://127.0.0.1:8000/docs)
- Найдите `GET /nearest_cities`
- Введите координаты широты и долготы, затем нажмите "Execute", чтобы получить два ближайших города.

---

## Используемые технологии

- ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi) 
- ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite)
- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python)
- ![Uvicorn](https://img.shields.io/badge/Uvicorn-009688?style=flat-square&logo=uvicorn)

