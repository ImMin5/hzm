From python:3.6.5

WORKDIR /app
ADD ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


ADD ./hzm_site /app/hzm_site/
ADD ./manage.py /app/

CMD ["python", "manage.py", "runserver", "0:9999"]
