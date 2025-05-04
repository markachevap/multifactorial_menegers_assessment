# Установка Python и зависимостей
sudo apt update
sudo apt install -y python3-pip python3-venv postgresql libpq-dev

# Создание виртуального окружения
python3 -m venv venv
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Настройка базы данных
sudo -u postgres psql -c "CREATE DATABASE manager_evaluation;"
sudo -u postgres psql -c "CREATE USER django_user WITH PASSWORD 'strong_password';"
sudo -u postgres psql -c "ALTER USER django_user WITH SUPERUSER;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE manager_evaluation TO django_user;"

# Миграции
python backend/manage.py migrate
python backend/manage.py collectstatic

# Создание суперпользователя
echo "Не пугайтесь, сейчас нужно создать своего пользователя (email можно выдумать, главное запомните все данные)"
python manage.py createsuperuser

echo "Установка завершена. Запустите сервер:"
echo "source venv/bin/activate && python manage.py runserver"