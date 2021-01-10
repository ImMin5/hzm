# hzm_site
kart

#django 
'''
$ docker run -it --rm \
    -p 8000:8000 \
    --link db \
    -e DJANGO_DB_HOST=db \
    -e DJANGO_DEBUG=True \
    --volume=$(pwd):/app/ \
    django-sample \
    ./manage.py runserver 0:8000
'''
