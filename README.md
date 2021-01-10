# hzm_site
kart

#django 실행 방법 
===
```
$ docker run -it --rm \
    -p 9999:9999 \
    --link hzm \
    -e DJANGO_DB_HOST=hzm_db \
    -e DJANGO_DEBUG=True \
    --volume=$(pwd):/app/ \
    django-hzm \
    ./manage.py runserver 0:9999
```
