From python:3.6.5

WORKDIR /app

ADD ./requirements.txt /app/
ADD ./hzm_site /app/hzm_site/
ADD ./manage.py /app/

COPY . .

# 파이썬 버퍼링 없애기
ENV PYTHONUNBUFFERED=1

# Intsall dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

