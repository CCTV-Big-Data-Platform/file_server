# file_server
server for get file from android

cd file_server

python3 -m venv env // 가상환경 설치
source env/bin/activate //가상환경 시작
pip install django
pip install djangorestframework

python manage.py runserver 0.0.0.0:5900
