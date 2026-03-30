# Pyverst1

Небольшое веб-приложение на Python, которое:
- читает данные о винах из Excel-файла (`wine3.xlsx`)
- группирует их по категориям
- генерирует HTML-страницу через шаблон (`Jinja2`)
- поднимает локальный HTTP-сервер для просмотра

---

##  Быстрый старт

### 1. Клонировать репозиторий
```bash
git clone https://github.com/Qmndrn/Pyverst1.git
cd Pyverst1
```

### 2. Создать виртуальное окружение
```bash
python -m venv venv
```

Активировать:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

---

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

Или:
```bash
pip install pandas jinja2 openpyxl
```

---

### 4. Подготовить файлы

В папке проекта должны быть:

- wine3.xlsx
- template.html
- main.py

---

### 5. Запуск
```bash
python main.py
```

### 6. Открыть в браузере

http://localhost:8000

---

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
