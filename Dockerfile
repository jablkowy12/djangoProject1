FROM python:3
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY . /code/
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#    command: python manage.py runserver 0.0.0.0:8000