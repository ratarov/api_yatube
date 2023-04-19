## Описание проекта
Django-проект написан в рамках курса Яндекс.Практикум.

## Запуск проекта
1. Клонировать репозиторий с github
```
git clone https://github.com/ratarov/api_yatube
```
2. Перейти в папку с проектом
```
cd api_final_yatube
```
3. Установить и активировать виртуальное окружение
```
python3 -m venv venv
```
```
source venv/bin/activate
```
4. Установить зависимости из requirements.txt
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
5. Выполнить миграции
```
python3 manage.py migrate
```
6. Запустить проект 
```
python3 manage.py runserver
```
Документацию со всеми эндпоинтами и примерами можно посмотреть по адресу
```
http://127.0.0.1:8000/redoc/
```
