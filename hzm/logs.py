import logging
import os
import datetime
import socket
kmh="kmh"

logger=0

'''
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[1]
    else :
        ip = request.META.get('REMOTE_ADDR')
    return ip
'''
PRIVATE_IPS_PREFIX = ('10.', '172.', '192.', )

def get_client_ip(request):
    """get the client ip from the request
    """
    remote_address = request.META.get('REMOTE_ADDR')
    # set the default value of the ip to be the REMOTE_ADDR if available
    # else None
    ip = remote_address
    # try to get the first non-proxy ip (not a private ip) from the
    # HTTP_X_FORWARDED_FOR
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        proxies = x_forwarded_for.split(',')
        # remove the private ips from the beginning
        while (len(proxies) > 0 and
                proxies[0].startswith(PRIVATE_IPS_PREFIX)):
            proxies.pop(0)
        # take the first ip which is not a private one (of a proxy)
        if len(proxies) > 0:
            ip = proxies[0]

    return ip

def create_logger(request,directory) :
    # 로그 생성
    ip=get_client_ip(request)
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
