# hzm_site
카트라이더 클럽 관리 및 기록 페이지

# postgresql 컨테이너 실행
```
$sudo docker run -it --rm \
    --name hzm_db \
    -e POSTGRES_DB=project_hzm \
    -e POSTGRES_USER=hzm_admin \
    -e POSTGRES_PASSWORD=password \
    --volume=$(pwd)/docker/data:/var/lib/postgresql/data \
    postgres:9.6.1
 ```

#도커 장고 이미지 빌드 
===
```
$ docker build -t django-sample .
```

#django 실행 방법 
===
```
$sudo docker run -it --rm \
    --name hzm_site \
    -p 9999:9999 \
    --link hzm_db \
    -e DJANGO_DB_HOST=hzm_db \
    -e DJANGO_DEBUG=True \
    --volume=$(pwd):/app/ \
    django-hzm \
    ./manage.py runserver 0:9999
```
#redis 실행방법
===
₩₩₩
$ sudo docker run --it --rm \
    --name hzm_chat
    -p 6379:6379 \
    --network redis-net -d \
    redis redis-server \
    --appendonly yes
₩₩₩
