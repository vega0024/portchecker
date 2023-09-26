import socket
import time
from colorama import init, Fore, Style
from datetime import datetime


def print_green(text):
    print(Fore.GREEN + text + Style.RESET_ALL)


def print_red(text):
    print(Fore.RED + text + Style.RESET_ALL)


init()

target_ip = input("Enter target IP address: ")
port = int(input("Enter port number: "))

print(f"Testing connection to {target_ip}:{port} >> v24")

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        sock.connect((target_ip, port))
        timestamp = datetime.now().strftime("%H:%M:%S")
        print_green(f"{timestamp} - The port {port} is open on {target_ip}.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except (socket.timeout, ConnectionRefusedError):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print_red(f"{timestamp} - The port {port} is closed on {target_ip}.")
    finally:
        sock.close()

    time.sleep(1)
