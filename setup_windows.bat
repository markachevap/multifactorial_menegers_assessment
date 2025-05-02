@echo off
REM Установка системы оценки менеджеров на Windows

echo Установка необходимых компонентов...
winget install -e --id Python.Python.3.11
winget install -e --id PostgreSQL.pgAdmin
winget install -e --id Git.Git

echo Ожидайте завершения установки...
timeout /t 10

echo Настройка переменных среды...
setx PATH "%PATH%;C:\Program Files\PostgreSQL\13\bin;C:\Program Files\Git\bin" /M

echo Клонирование репозитория...
git clone https://github.com/markachevap/multifactorial_menegers_assessment.git
cd multifactorial_menegers_assessment

echo Создание виртуального окружения...
python -m venv venv
call venv\Scripts\activate.bat

echo Установка зависимостей...
pip install -r requirements.txt

echo Настройка базы данных PostgreSQL...
psql -U postgres -c "CREATE DATABASE manager_evaluation;"
psql -U postgres -c "CREATE USER django_user WITH PASSWORD 'really_STRONG_password';"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE manager_evaluation TO django_user;"

echo Применение миграций...
python manage.py migrate
python manage.py collectstatic

echo Создание суперпользователя...
echo Не пугайтесь, сейчас нужно создать своего пользователя (email можно выдумать, главное запомните все данные)
python manage.py createsuperuser

echo Установка завершена!
echo Для запуска сервера выполните:
echo venv\Scripts\activate.bat
echo python manage.py runserver

pause