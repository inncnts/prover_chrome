import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Perhatikan kita mengimpor 'Service' secara eksplisit
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

# --- KONFIGURASI ---
URL = "https://onprover.orochi.network"
REFRESH_INTERVAL_SECONDS = 15 * 60

CHROME_DRIVER_PATH = "E:\\drivers\\chromedriver.exe"

print("Mempersiapkan dan menginisialisasi browser Chrome (Mode Manual)...")
try:
    service = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    print("Browser siap digunakan.")
except Exception as e:
    print(f"Gagal menginisialisasi browser: {e}")
    print("Pastikan path di CHROME_DRIVER_PATH sudah benar dan menunjuk ke file chromedriver.exe.")
    exit()

def refresh_and_prove():
    try:
        print(f"Membuka halaman: {URL}")
        driver.get(URL)
        
        print("Menunggu halaman termuat (memberi jeda 20 detik)...")
        time.sleep(20)

        print("Mencari tombol 'Proving' menggunakan XPath...")
        prove_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/main/div/div/div[1]/div[1]/div[2]/button')

        print("Tombol ditemukan! Mencoba untuk mengklik...")
        prove_button.click()
        print(f"BERHASIL! Proses 'Proving' berhasil dijalankan pada: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    except NoSuchElementException:
        print("--- PERINGATAN ---")
        print("Tombol 'Proving' tidak dapat ditemukan.")
        print("Kemungkinan penyebab: Anda belum login, atau halaman belum termuat sempurna.")
        print("Script akan tetap menunggu dan mencoba lagi pada siklus berikutnya.")
    except Exception as e:
        print(f"--- ERROR ---")
        print(f"Terjadi kesalahan yang tidak terduga: {e}")

# --- LOOP UTAMA SCRIPT ---
try:
    while True:
        refresh_and_prove()
        
        print("-" * 50)
        print(f"Proses siklus ini selesai. Menunggu selama {REFRESH_INTERVAL_SECONDS / 60} menit...")
        print(f"Waktu tidur dimulai pada: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Proses selanjutnya akan dimulai sekitar pukul: {time.strftime('%H:%M:%S', time.localtime(time.time() + REFRESH_INTERVAL_SECONDS))}")
        print("-" * 50)
        time.sleep(REFRESH_INTERVAL_SECONDS)

except KeyboardInterrupt:
    print("\nScript dihentikan secara manual oleh pengguna.")

finally:
    print("Menutup browser...")
    driver.quit()
    print("Selesai.")
