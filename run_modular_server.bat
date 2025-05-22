@echo off
SETLOCAL

:: 1. Cek dan buat virtual environment jika belum ada
IF NOT EXIST "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

:: 2. Activate virtual environment
call venv\Scripts\activate.bat

:: 3. Install dependencies
pip install -r requirements.txt

:: 4. cd ke modular_project
cd modular_project

:: 5. migration
py manage.py makemigrations
py manage.py migrate

:: 6. Run Django development server
py manage.py runserver 0.0.0.0:8000
