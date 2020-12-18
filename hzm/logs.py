import logging
import os
import datetime
import socket
<<<<<<< HEAD
from ipware import get_client_ip
=======
>>>>>>> 79dbbc54e18da1f09cd5129b25361386f4517c1c
kmh="kmh"

logger=0

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def create_logger(request,directory) :
    # 로그 생성
<<<<<<< HEAD
    ip = get_client_ip(request)
=======
    ip=socket.gethostbyname(socket.getfqdn())
>>>>>>> 79dbbc54e18da1f09cd5129b25361386f4517c1c
    logger= logging.getLogger(ip)
    # Check handler exists
    
    if len(logger.handlers) > 0:
        logger.handlers.clear()

    # 로그의 출력 기준 설정
    logger.setLevel(logging.INFO)
    
    # log 출력 형식
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # log 출력
    #stream_handler = logging.StreamHandler()
    #stream_handler.setFormatter(formatter)
    #logger.addHandler(stream_handler)


    # log를 파일에 출력
    file_handler = logging.FileHandler(directory)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

#로그폴더 만드는 함수
def create_dir() :
    try:
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y/%m/%d')
        directory = "LOG/"+nowDate
        if not os.path.exists(directory) :
            os.makedirs(os.path.join(directory))
            return directory
        return directory
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")


def log_start(request,directory,msg) :
    
    logger = create_logger(request,directory)
    logger.info(msg)
