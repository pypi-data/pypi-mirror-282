import json

def create():
    # Read data from JSON files
    with open("data/data_areas.json", "r",encoding="utf-8") as areas_file:
        areas_data = json.load(areas_file)
    
    with open("data/data_buildings.json", "r",encoding="utf-8") as buildings_file:
        buildings_data = json.load(buildings_file)
    
    with open("data/data_floors.json", "r",encoding="utf-8") as floors_file:
        floors_data = json.load(floors_file)
    
    with open("data/data_rooms.json", "r",encoding="utf-8") as rooms_file:
        rooms_data = json.load(rooms_file)
    
    with open("data/data_facilitytype.json", "r",encoding="utf-8") as facilitytype_file:
        facilitytype_data = json.load(facilitytype_file)
    
    # Prepare facilities data
    facilities = []
    for area in areas_data:
        facility = {
            "id": area["id"],
            "facilitytype_id": area["facilitytype_id"],
            "master_facility_id": None,
            "name": area["name"],
            "name_en": area["name_en"],
            "group_id": None,
            "geometry": "",
            "geolocation": ""
        }
        facilities.append(facility)
    
    for building in buildings_data:
        facility = {
            "id": building["id"],
            "facilitytype_id": building["facilitytype_id"],
            "master_facility_id": building["master_facility_id"],
            "name": building["name"],
            "name_en": building["name_en"],
            "group_id": None,
            "geometry": "",
            "geolocation": ""
        }
        facilities.append(facility)
    
    for floor in floors_data:
        facility = {
            "id": floor["id"],
            "facilitytype_id": floor["facilitytype_id"],
            "master_facility_id": floor["master_facility_id"],
            "name": floor["name"],
            "name_en": floor.get("name_en", ""),
            "group_id": None,
            "geometry": "",
            "geolocation": ""
        }
        facilities.append(facility)
    
    for room in rooms_data:
        facility = {
            "id": room["id"],
            "facilitytype_id": room["facilitytype_id"],
            "master_facility_id": room["master_facility_id"],
            "name": room["name"],
            "name_en": room.get("name_en", ""),
            "group_id": None,
            "geometry": "",
            "geolocation": ""
        }
        facilities.append(facility)
    
    # Prepare facility types data
    facilitytypes = facilitytype_data["facilitytypes"]
    
    # Create systemdata dictionary
    systemdata = {
        "facilities": facilities,
        "facilitytypes": facilitytypes
    }
    
    # Write systemdata to JSON file
    with open("data/systemdata.json", "w",encoding="utf-8") as systemdata_file:
        json.dump(systemdata, systemdata_file,ensure_ascii=False, indent=4)
        
    print("systemdata.json created successfully")