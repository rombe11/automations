from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time

# === Settings ===
CONTACT_NAMES = ["Noam Pollisse"]
MESSAGE_TEMPLATE = (
    f"Hi {CONTACT_NAMES[0]},\n"
    "Please enter the link:\n"
    f"{https://rombe11.github.io/automations/}"
)

options = Options()
options.add_argument(r"user-data-dir=C:\Users\rombu\AppData\Local\Google\Chrome\User Data\BotProfile")
options.add_argument("--profile-directory=Default") 
driver = webdriver.Chrome(options=options)

driver.get("https://web.whatsapp.com")

def send_message():
    for contact in CONTACT_NAMES:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        search_box.clear()
        search_box.send_keys(contact)
        time.sleep(2)
        search_box.send_keys("\n")

        print(f"[*] Sending message to {contact}...")
        message_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )
        message_box.send_keys(MESSAGE_TEMPLATE.format(name=contact))
        message_box.send_keys("\n")
        print(f"Message sent to {contact}")

schedule.every(1).minutes.do(send_message)

print("[*] Bot is running... Press CTRL+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)
