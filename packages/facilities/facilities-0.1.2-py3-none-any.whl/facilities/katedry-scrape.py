from selenium import webdriver
import json
import requests

import getpass
import time
from selenium.webdriver.support import expected_conditions as EC

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
driver.get(var["login-url"])

time.sleep(3)


elem = driver.find_element(By.ID, "floatingInput")
elem.clear()
elem.send_keys(var["login"])
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.ID, "floatingPassword")
elem.clear()
elem.send_keys(password)
elem.send_keys(Keys.RETURN)


driver.get(var["katedry-url"])
response = requests.get(var["katedry-url"])


try:
        # Get the entire HTML content of the page
        page_html = driver.page_source
        # Extract text content from the HTML
        page_text = extract_text_from_html(page_html)
        # Save the text content as JSON
        data = {'text': page_text}
        with open('data/data1.json', 'w') as file:
            json.dump(data, file, indent=4)
        print("Text data saved as JSON.")
except Exception as e:
        print("An error occurred:", e)
finally:
        # Close the WebDriver
        driver.quit()



# Zavření prohlížeče 
driver.quit()

# Zde můžete zpracovat JSON data dle potřeby
#parsed_json = json.loads(json_data)
#print(parsed_json)