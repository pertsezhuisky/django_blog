#Процесс запуска
1. Клонируйте репозиторий на свою локальную машину:
```
    git init
    git clone https://github.com/pertsezhuisky/django_blog.git
```

2. Создайте и активируйте виртуальную среду (venv):
```
    python3 -m venv venv
    source venv/bin/activate
```

3. Установите зависимости:

Для prod'a:
```
    pip install -r requirements/prod/requirements.txt
```

Для dev'a:
```
    pip install -r requirements/dev/requirements.txt
```

4. Созадайте файл .env:
```
    touch .env
```
Задайте параметры: DEPLOY, EMAIL, EMAIL_PASSWORD, SECRET_KEY, DJANGO_DEBUG.

5. Перейдите в папку проекта:
```
    cd myblog
```

6. Запустите проект:
```
    python3 manage.py runserver
```

Готово! Теперь вы можете использовать проект в режиме разработки.
