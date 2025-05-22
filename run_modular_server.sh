#!/bin/bash

# 1. Buat venv kalau belum ada
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# 2. Activate venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. cd ke modular_project
cd modular_project

# 5. Migrations
python manage.py makemigrations
python manage.py migrate

# 6. Run server
python manage.py runserver 0.0.0.0:8000