# hzm_site
카트라이더 클럽 관리 및 기록 페이지
+ http://minchan.synology.me:9999/
+ http://club-hzm.ga/

## 목차

### [1.DEPENDENCY](#dependency)
### [2.사이트 미리보기](#사이트-미리보기)
### [3.실행방법](#실행방법)

#### Front End
 + Bootstrap

#### Backend
 + PostgreSQL 9.6.1
 + Django 3.6.4
 ```
pip install Django==3.1.4
 ```
 ```
pip install djangorestframework==3.11.1
 ```
```
pip install channels-redis==3.2.0
```
 + Redis latest version
```
pip install django-redis
```

## 2. 사이트 미리보기
### 메인페이지
![image](https://user-images.githubusercontent.com/38625842/109582315-48d5e480-7b41-11eb-8766-5b76bf012ff8.png)

### 클럽 화면
![image](https://user-images.githubusercontent.com/38625842/109582460-8f2b4380-7b41-11eb-9fdc-202a09534f69.png)

### 개인기록 화면
![image](https://user-images.githubusercontent.com/38625842/109582580-beda4b80-7b41-11eb-8fbe-8e98d954b15a.png)

### 마이룸
![image](https://user-images.githubusercontent.com/38625842/109583042-9868e000-7b42-11eb-8f4f-ca99a790a60f.png)

### 경기신청하기 화면
![image](https://user-images.githubusercontent.com/38625842/109583171-cf3ef600-7b42-11eb-89a6-4dc4f9542e3f.png)


### 경기결과 화면
[경기결과 화면] ![image](https://user-images.githubusercontent.com/38625842/109583215-e251c600-7b42-11eb-8a76-e7c237e666e5.png)

### 개인스케쥴 화면
![image](https://user-images.githubusercontent.com/38625842/109583534-6441ef00-7b43-11eb-9d5f-1d4ca1f7c0df.png)


### 자유게시판 화면
![image](https://user-images.githubusercontent.com/38625842/109583624-8471ae00-7b43-11eb-984f-6a3ff779cdb3.png)
![image](https://user-images.githubusercontent.com/38625842/109583672-9b180500-7b43-11eb-81f0-3f7a6eaf5ded.png)


## 3.실행방법
### postgresql 컨테이너 실행
```
$sudo docker run -it --rm \
    --name hzm_db \
    -e POSTGRES_DB=project_hzm \
    -e POSTGRES_USER=hzm_admin \
    -e POSTGRES_PASSWORD=password \
    --volume=$(pwd)/docker/data:/var/lib/postgresql/data \
    postgres:9.6.1
 ```

### 도커 장고 이미지 빌드 
```
$ docker build -t django-sample .
```

### django 실행 방법 
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
### redis 실행방법
```
$ sudo docker run -it --rm \
    --name hzm_chat
    -p 6379:6379 \
    --network hzm-net -d \
    redis redis-server \
    --appendonly yes
```
