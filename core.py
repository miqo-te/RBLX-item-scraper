import time, datetime, sys, os, json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import requests

def log_price(price):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(os.path.join(sys.path[0], settings['log_file']), 'a') as f:
        f.write(f'{timestamp}: R$ {price}\n')

def send_notification(price):
    if price <= settings['min_price']:
        message = f"<@{settings['discord_user_id']}> **SUCCESS:** Price reached __**R$ {price}**__.\n{settings['target']}"
        data = {
            "content": message
        }
        response = requests.post(settings['webhook_url'], json=data)
        if response.status_code == 204:
            print("\u001b[32mNotification sent to Discord webhook successfully.\u001b[0m")
            sys.stdout.flush()
        return True

def print_error_message(message):
    print("\033[31m{}\033[0m".format(message))
    sys.stdout.flush()

# Load settings from JSON file
with open(os.path.join(sys.path[0], 'settings.json')) as f:
    settings = json.load(f)

retry_attempts = 0
while retry_attempts < settings['max_retry_attempts']:
    success = False # The default state of success should be False, because we haven't succeeded yet.
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(settings['target'])
    time.sleep(settings['retry_delay'])

    try:
        soup = BeautifulSoup(driver.page_source, "lxml")
        elements = soup.find_all("span", class_="text-robux-lg")
        desired_element = None
        for element in elements:
            if "disabled" not in element["class"]:
                desired_element = element
                break

        if desired_element:
            price = int(desired_element.text)
            driver.quit()
            print(f"Current price: R$ {price}")
            log_price(price)
            if send_notification(price):
                driver.quit()
                sys.exit(0)
            
            # Reset retry attempts to 0
            retry_attempts = 0
            success = True

            # Delay
            time.sleep(settings['scrape_delay'])
    except NoSuchElementException:
        pass

    if retry_attempts < settings['max_retry_attempts'] and success == False:
        driver.quit()
        retry_attempts += 1
        print(f"Page got stuck loading. Retry attempt {retry_attempts}...")
        time.sleep(2)  # Wait for 2 seconds before the next attempt

error_message = f"Desired element not found after {settings['max_retry_attempts']} retry attempts of {settings['retry_delay']} seconds each."
print_error_message(error_message)
log_price(error_message)
