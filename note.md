# สร้าง python environment สำหรับพัฒนา (python 3.12.x)
python -m venv .venv

# active environment
.venv\Scripts\activate

# ติดตั้ง dependencies ที่จำเป็น
pip install -r requirements.txt

# สร้าง project (core ของโปรเจค)
django-admin startproject license_management .

# สร้าง app ของโปรเจค ในที่นี้จะสร้าง api
python manage.py startapp api


# สร้าง database 
python manage.py makemigrations
python manage.py migrate


# รัน server
python manage.py runserver 0.0.0.0:8080