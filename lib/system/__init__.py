from lib.interface import linha, cabecalho
import socket
import platform
import uuid


def get_mac_adress():
    mac_num = uuid.getnode()

    mac_hex = f"{mac_num:012x}"
    mac_string = ":".join(mac_hex[i:i+2] for i in range(0, 12, 2))

    return mac_string


def get_hostname():
    hostname = socket.gethostname()
    return hostname


def get_systemop():
    system_op = platform.system()
    return system_op

def get_IP():
    local_ip = socket.gethostbyname(get_hostname())
    return local_ip

def exibir_infos():
    cabecalho("NETWATCH V1")
    print(f"Hostname: {get_hostname()}")
    print(f"System: {get_systemop()}")
    print(f"IP Local: {get_IP()}")
    print(f"MAC: {get_mac_adress()}")