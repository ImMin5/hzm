# hzm_site
카트라이더 클럽 관리 및 기록 페이지
+ http://minchan.synology.me:9999/
+ ~http://club-hzm.ga/~

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
pip install Django==3.6.4
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
메인 페이지 입니다 최신 게시물과 경기결과를 클릭하여 이동 할 수 있습니다.
<p align="center" style="color:gray">
  <img style="margin:50px 0 10px 0; width:50% height:50%" src="https://user-images.githubusercontent.com/38625842/109582315-48d5e480-7b41-11eb-8766-5b76bf012ff8.png" alt="mainpage" />
</p> 


### 클럽 화면
클럽화면입니다. 
클럽장의 이름, 클럽 회원수, 공지사항등을 확인 할 수 있습니다.
<p align="center" style="color:gray">
  <img style="margin:50px 0 10px 0" src="https://user-images.githubusercontent.com/38625842/109582460-8f2b4380-7b41-11eb-9fdc-202a09534f69.png" alt="club page" />
</p> 

클럽원 목록 버튼 클릭시 멤버현황과 친선전 승률을 알 수 있습니다.
<p align="center" style="color:gray">
  <img style="margin:50px 0 10px 0" src="https://user-images.githubusercontent.com/38625842/109585721-5f7f3a00-7b47-11eb-9d4e-b4699ee485e0.png" alt="club page" />
</p> 




### 개인기록 화면
개인 기록 화면 입니다.
맵 마다 개인 기록을 입력 할 수 있고 클럽 회원중 자신이 몇등 인지 알 수 있습니다.
<p align="center" style="color:gray">
  <img style="margin:50px 0 10px 0" src="https://user-images.githubusercontent.com/38625842/109582580-beda4b80-7b41-11eb-8fbe-8e98d954b15a.png"/>
</p>

### 마이룸
자신의 정보를 확인 할 수 있는 페이지 입니다.
닉네임변경과 비밀번호 변경을 할 수 있습니다.
<p align="center" style="color:gray">
  <img style="margin:50px 0 10px 0" src="https://user-images.githubusercontent.com/38625842/109583042-9868e000-7b42-11eb-8f4f-ca99a790a60f.png"/>
</p>

### 경기신청하기 화면
누구나 자유롭게 해당 클럽에 경기를 신청 할 수 있습니다.
날짜,시간,인원,신청자등을 필수적으로 적어줘야 합니다,
<p align="center" style="color:gray">
  <img style="margin:50px 0 10px 0" src="https://user-images.githubusercontent.com/38625842/109583171-cf3ef600-7b42-11eb-89a6-4dc4f9542e3f.png"/>
</p>



### 경기결과 화면
경기결과를 보여주는 게시판 입니다.
경기결과는 직접 입력해주어야 반영이 됩니다.
<p align="center" style="color:gray">
  <img style="margin:50px 0 10px 0" src="https://user-images.githubusercontent.com/38625842/109583215-e251c600-7b42-11eb-8a76-e7c237e666e5.png"/>
</p>


### 일정관리 화면
개인 일정을 관리하고 클럽원들과 공유 할 수 있는 페이지 입니다.
시간표를 보고 언제 서로 시간이 되는지 미리 적어두면 빠르게 확인가능 합니다.
<p align="center" style="color:gray">
  <img style="margin:50px 0 10px 0" src="https://user-images.githubusercontent.com/38625842/109583534-6441ef00-7b43-11eb-9d5f-1d4ca1f7c0df.png"/>
</p>


### 자유게시판 화면
자유게시판 입니다.
자유롭게 서로 의견을 주고 받을 수 있습니다. 댓글로 소통도 가능합니다.
<p align="center" style="color:gray">
  <img style="margin:50px 0 10px 0" src="hhttps://user-images.githubusercontent.com/38625842/109583624-8471ae00-7b43-11eb-984f-6a3ff779cdb3.png"/>
</p>
<p align="center" style="color:gray">
  <img style="margin:50px 0 10px 0" src="https://user-images.githubusercontent.com/38625842/109583672-9b180500-7b43-11eb-81f0-3f7a6eaf5ded.png"/>
</p>



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
