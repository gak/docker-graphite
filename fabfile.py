from fabric.api import *

args = ' '.join([
    '-i',
    '-t',
    '-p 8125:8125/udp',
    '-v /data/graphite:/var/lib/graphite/storage'
])


def build():
    local('sudo docker build -t graphite .')


def start():
    local('sudo docker run {} -d graphite'.format(args))


def shell():
    local('sudo docker run {} graphite bash'.format(args))

