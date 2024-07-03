from selenium import webdriver
import json
import json
import uuid
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


def log_to_web(var):
    
    #získání hesla 
    password = getpass.getpass()

    driver = webdriver.Chrome()
    driver.get(var["login_url"])

    time.sleep(1)
    driver.refresh()


    elem = driver.find_element(By.ID, "floatingInput")
    elem.clear()
    elem.send_keys(var["login"])
    elem.send_keys(Keys.RETURN)

    elem = driver.find_element(By.ID, "floatingPassword")
    elem.clear()
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)
    return driver


def read_facilitytype_id(my_facilitytype):
    # Load facility type data
    facility_type_id = None
    with open("data/data_facilitytype.json", "r", encoding="utf-8") as facilitytype_file:
        facilitytype_data = json.load(facilitytype_file)
        for facilitytype in facilitytype_data.get("facilitytypes", []):
            if facilitytype["name_en"] == my_facilitytype:
                facility_type_id = facilitytype["id"]
                break
    return facility_type_id


def area_scrape(driver, area_index, var):
    url_to_scrape = var["area-url"] + str(area_index)
    print(url_to_scrape)

    # Load external IDs to check if the URL was already scraped
    external_ids_file = "data/externalids.json"
    if os.path.exists(external_ids_file):
        with open(external_ids_file, "r", encoding="utf-8") as ext_file:
            external_ids = json.load(ext_file)
    else:
        external_ids = []

    # Check if the URL is already in the external IDs
    existing_entry = next((entry for entry in external_ids if entry["url"] == url_to_scrape), None)

    if existing_entry:
        print(f"Area URL {url_to_scrape} already scraped. Checking buildings for updates...")
        area_id = existing_entry["id"]
    else:
        driver.get(url_to_scrape)
        
        # Make uuid for area
        area_id = str(uuid.uuid4())

        # Finds name of area
        header_h1 = driver.find_element(By.XPATH, "//header//h1[1]")
        first_a_in_h1 = header_h1.find_element(By.XPATH, ".//a")
        href_value = first_a_in_h1.get_attribute("text")
        print(href_value)
        
        # Load facility type id
        facility_type_id = read_facilitytype_id("area")
        entry_of_area = {
            "id": area_id,
            "facilitytype_id": facility_type_id,
            "master_facility_id": None,
            "name": href_value,
            "name_en": "",
            "group_id": None,
            "geometry": "",
            "geolocation": ""
        }

        # Load existing data from the JSON areas file and append the new entry
        areas_file = "data/data_areas.json"
        if os.path.exists(areas_file):
            with open(areas_file, "r", encoding="utf-8") as areas_file_r:
                existing_data = json.load(areas_file_r)
            if not isinstance(existing_data, list):
                existing_data = []
            existing_data.append(entry_of_area)
        else:
            existing_data = [entry_of_area]

        with open(areas_file, "w", encoding="utf-8") as areas_file_w:
            json_data = json.dumps(existing_data, ensure_ascii=False, indent=4)
            areas_file_w.write(json_data)

        # Update external IDs with the new URL and ID
        external_ids.append({"id": area_id, "url": url_to_scrape})

        with open(external_ids_file, "w", encoding="utf-8") as ext_file_w:
            json.dump(external_ids, ext_file_w, ensure_ascii=False, indent=4)

    # Ensure the driver navigates to the area URL to scrape buildings
    driver.get(url_to_scrape)
    # Always scrape buildings to check for updates
    driver = buildings_scrape(area_id, driver)
    
    return driver


def buildings_scrape(area_id, driver):
    facility_type_id = read_facilitytype_id("building")
    elem = driver.find_element(By.ID, "ArealObjektCard")
    data = []
    lines = elem.text.split('\n')
    i = 1

    external_ids_file = "data/externalids.json"
    if os.path.exists(external_ids_file):
        with open(external_ids_file, "r", encoding="utf-8") as ext_file:
            external_ids = json.load(ext_file)
    else:
        external_ids = []

    for line in lines[1:]:  # Exclude the first line
        # Construct the building URL (modify as needed based on actual URL structure)
        building_url = f"{area_id}-building-{i}"

        # Check if the building URL is already in the external IDs
        if any(entry["url"] == building_url for entry in external_ids):
            print(f"Building URL {building_url} already scraped. Checking rooms for updates...")
            i += 1
            continue

        unique_id = str(uuid.uuid4())
        driver = rooms_scrape(unique_id, driver, i)
        entry = {
            "id": unique_id,
            "name": line,
            "facilitytype_id": facility_type_id,
            "master_facility_id": area_id,
            "name_en": "",
            "group_id": None,
            "geometry": "",
            "geolocation": ""
        }
        data.append(entry)

        # Update external IDs with the new URL and ID
        external_ids.append({"id": unique_id, "url": building_url})

        i += 1

    write_to_json(data, "data/data_buildings.json")

    with open(external_ids_file, "w", encoding="utf-8") as ext_file_w:
        json.dump(external_ids, ext_file_w, ensure_ascii=False, indent=4)

    return driver


def rooms_scrape(building_id, driver, building_index):
    facility_type_id_room = read_facilitytype_id("classroom")
    facility_type_id_floor = read_facilitytype_id("floor")
    # Initialize lists to store rooms and floors data
    rooms_data = []
    floors_data = []

    # Find the desired <a> element
    a_element = driver.find_element(By.CSS_SELECTOR, "#ArealObjektCard > div > div:nth-child(2) > div > div:nth-child(" + str(building_index) + ") > div > a")
    # Get the href attribute value
    href_value = a_element.get_attribute("href")

    # Print the href value
    print("Href value:", href_value)

    driver.get(href_value)

    # Find all room elements
    room_elements = driver.find_elements(By.XPATH, "//div[@id='ObjektMistnosts']//div[contains(@id, 'Mistnost_')]")

    current_floor_id = None
    current_floor_name = None

    # Load existing external IDs
    external_ids_file = "data/externalids.json"
    if os.path.exists(external_ids_file):
        with open(external_ids_file, "r", encoding="utf-8") as ext_file:
            external_ids = json.load(ext_file)
    else:
        external_ids = []

    for room_element in room_elements:
        room_name = room_element.text.strip()  # Extract room name

        # Split room name into floor and room
        floor_room_parts = room_name.split(" / ", 1)
        floor = floor_room_parts[0]
        room = floor_room_parts[1]

        # Generate URLs for floor and room (modify as needed based on actual URL structure)
        floor_url = f"{building_id}-floor-{floor}"
        room_url = f"{building_id}-{floor}-room-{room}"

        if floor != current_floor_name:
            # Check if the floor URL is already in the external IDs
            if any(entry["url"] == floor_url for entry in external_ids):
                current_floor_id = next(entry["id"] for entry in external_ids if entry["url"] == floor_url)
                current_floor_name = floor
                print(f"Floor URL {floor_url} already scraped. Checking rooms for updates...")
            else:
                # Generate UUID for floor
                floor_id = str(uuid.uuid4())
                current_floor_id = floor_id
                current_floor_name = floor

                # Create floor entry
                floor_entry = {
                    "id": floor_id,
                    "facilitytype_id": facility_type_id_floor,
                    "master_facility_id": building_id,
                    "name": floor,
                    "name_en": "",
                    "group_id": None,
                    "geometry": "",
                    "geolocation": ""
                }
                floors_data.append(floor_entry)

                # Update external IDs with the new floor URL and ID
                external_ids.append({"id": floor_id, "url": floor_url})
        # Check if the room URL is already in the external IDs
        if any(entry["url"] == room_url for entry in external_ids):
            print(f"Room URL {room_url} already scraped. Skipping...")
            continue

        # Add room to the main list
        room_id = str(uuid.uuid4())
        room_entry = {
            "id": room_id,
            "facilitytype_id": facility_type_id_room,
            "master_facility_id": current_floor_id,
            "name": room,
            "name_en": "",
            "group_id": None,
            "geometry": "",
            "geolocation": ""
        }
        rooms_data.append(room_entry)

        # Update external IDs with the new room URL and ID
        external_ids.append({"id": room_id, "url": room_url})
    # Serialize floors data to JSON and write it to a file
    write_to_json(floors_data, "data/data_floors.json")

    # Serialize rooms data to JSON and write it to a file
    write_to_json(rooms_data, "data/data_rooms.json")

    # Update external IDs file
    with open(external_ids_file, "w", encoding="utf-8") as ext_file_w:
        json.dump(external_ids, ext_file_w, ensure_ascii=False, indent=4)

    driver.back()
    return driver



def write_to_json(facility_data,path):
    # Serialize facility data to JSON
    facility_json_data = json.dumps(facility_data, ensure_ascii=False,indent=4) 
   
    # Load existing data from the JSON file and appends them to file
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as json_file:
            existing_data = json.load(json_file)
        if path=="data_areas.json":
            existing_data.append(facility_data)
        else:
            existing_data.extend(facility_data)
        # Write JSON to a file or use it as needed
        with open(path, "w", encoding="utf-8") as json_file:
            json_data = json.dumps(existing_data, ensure_ascii=False,indent=4)

            json_file.write(json_data) 
    else :
         # Write JSON to a file or use it as needed
        with open(path, "w", encoding="utf-8") as json_file:
            json_file.write(facility_json_data) 


def scrape():
    with open("env-var.json", 'r', encoding="utf-8") as file:
        var = json.load(file)
    driver=log_to_web(var)
    for i in range(1,39): #for i in range(1,39):
        driver=area_scrape(driver,i,var)

    try:
        print("Scrape done")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the WebDriver
        driver.quit()