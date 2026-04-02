# Pyverst1

Небольшое веб-приложение на Python, которое:
- читает данные о винах из Excel-файла (`wine.xlsx`)
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
pip install pandas jinja2 openpyxl argparse
```

---

### 4. Подготовить файлы

В папке проекта должны быть:

- wine.xlsx
- template.html
- main.py

---

## 📊 Формат данных

Файл `wine.xlsx` должен содержать таблицу следующего вида:

| Название | Категория | Цена | Описание |
|----------|----------|------|----------|
| Вино     | Красное  | 1200 | Мягкий вкус с нотами ягод |
| Вино     | Белое    | 1500 | Свежий фруктовый аромат   |
| Вино     | Красное  | 1800 | Насыщенный вкус           |

Можно использовать файл `wine.xlsx` из репозитория как образец и заменить данные своими.

Важно:
- названия колонок должны совпадать точно  
- используется колонка **"Категория"** для группировки  

---

### 5. Запуск
```bash
python main.py
```

Также можно указать свой файл с данными:

```bash
python main.py --wine-file my_wines.xlsx
```

Или через переменную окружения:

**Linux / macOS**
```bash
export WINE_FILE=my_wines.xlsx
python main.py
```

**Windows**
```bash
set WINE_FILE=my_wines.xlsx
python main.py
```

---

### 6. Открыть в браузере

http://localhost:8000

---

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
