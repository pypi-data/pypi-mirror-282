from selenium import webdriver
import json
import os
import getpass
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def extract_text_from_html(html_content):
    # Use BeautifulSoup to parse HTML and extract text content
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find all text elements
    text_elements = soup.find_all(text=True)
    # Filter out any empty or whitespace-only strings
    text_elements = [text.strip() for text in text_elements if text.strip()]
    return text_elements
cesta='env-var.json'
with open(cesta, 'r') as file:
    var = json.load(file)
#získání hesla 
password = getpass.getpass()

driver = webdriver.Chrome()
driver.get(var["rozvrh-url"])

time.sleep(1)
#alert = Alert(driver)
#alert.dismiss()
#time.sleep(1)
driver.refresh()

elem = driver.find_element(By.ID, "floatingInput")
elem.clear()
elem.send_keys(var["login"])
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.ID, "floatingPassword")
elem.clear()
elem.send_keys(password)
elem.send_keys(Keys.RETURN)


# driver.get(var["rozvrh-url"])
# response = requests.get(var["rozvrh-url"])


try:
        # Get the entire HTML content of the page
        page_html = driver.page_source
        # Extract text content from the HTML
        page_text = extract_text_from_html(page_html)
        # Create a directory if it doesn't exist
        if not os.path.exists('data'):
            os.makedirs('data')
        # Save the text content as JSON
        data = {'text': page_text}
        with open('data/raw_data.json', 'w') as file:
            json.dump(data, file, indent=4)
        print("Text data saved as JSON.")
except Exception as e:
        print("An error occurred:", e)
finally:
        # Close the WebDriver
        driver.quit()



# Zavření prohlížeče 
driver.quit()


