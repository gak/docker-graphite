from fabric.api import *

args = ' '.join([
    '-i',
    '-t',
    '-p 127.0.0.1::80/tcp',
    '-p 127.0.0.1:8125:8125/udp',
#    '-p 127.0.0.1:2003:2003/udp',
#    '-p 127.0.0.1:2004:2004/udp',
#    '-p 127.0.0.1:7002:7002/udp',
    '-v /data/graphite:/var/lib/graphite/storage'
])


def build():
    local('sudo docker build -t graphite .')


def start():
    local('sudo docker run {} graphite'.format(args))


def shell():
    local('sudo docker run {} graphite bash'.format(args))

