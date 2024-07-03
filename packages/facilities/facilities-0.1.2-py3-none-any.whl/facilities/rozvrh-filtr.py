# import json
# import codecs
# # Load the JSON data from the file
# with open('data/raw_data.json', 'r') as file:
#     data = json.load(file)

# # Extract the text content
# text_list = data.get('text', [])

# # If the text list is not empty, get the first element (assuming it contains the JSON string)
# if text_list:
#     text = text_list[0]
    
#     # Parse the JSON string within the text
#     parsed_data = json.loads(text)

#     # Extract events from the parsed data
#     events = parsed_data.get('events', [])

#     # If events are found, print the first event
#     if events:
#         first_event = events[0]
        
#         # Decode Unicode escape sequences in classroom names
#         decoded_classroom_names = [codecs.decode(name, 'unicode_escape') for name in first_event.get('classroomsNames', [])]
        
#         # Update the first event with decoded classroom names
#         first_event['classroomsNames'] = decoded_classroom_names
        
#         print(first_event)
#     else:
#         print("No events found in the data.")
# else:
#     print("No text content found in the data.")

# # Initialize a list to store filtered data
# filtered_data = []

# # Iterate over each event and extract the required fields
# for event in events:
#     # Extract the required fields from the event
#     classroomsIds = event.get('classroomsIds', [])
#     classrooms_names = event.get('classroomsNames', [])
#     classrooms_areas_ids = event.get('classroomsAreasIds', [])
    
#     # Construct a dictionary with the filtered data
#     filtered_event_data = {
#         'classroomsIds': classroomsIds,
#         'classroomsNames': classrooms_names,
#         'classroomsAreasIds': classrooms_areas_ids
#     }
    
#     # Append the filtered event data to the list
#     filtered_data.append(filtered_event_data)

# # Write the filtered data to a new JSON file
# with open('data/filtered_data.json', 'w') as file:
#     json.dump(filtered_data, file, indent=4)

# print("Filtered data saved as JSON.")

# # Zde můžete zpracovat JSON data dle potřeby
# #parsed_json = json.loads(json_data)
# #print(parsed_json)





import json
import codecs

# Load the JSON data from the file
with open('data/raw_data.json', 'r') as file:
    data = json.load(file)

# Extract the text content
text_list = data.get('text', [])

# If the text list is not empty, get the first element (assuming it contains the JSON string)
if text_list:
    text = text_list[0]
    
    # Parse the JSON string within the text
    parsed_data = json.loads(text)

    # Extract events from the parsed data
    events = parsed_data.get('events', [])

    # If events are found, print the first event
    if events:
        first_event = events[0]
        
        # Decode Unicode escape sequences in classroom names
        decoded_classroom_names = [codecs.decode(name, 'unicode_escape') for name in first_event.get('classroomsNames', [])]
        
        # Update the first event with decoded classroom names
        first_event['classroomsNames'] = decoded_classroom_names
        
        print(first_event)
    else:
        print("No events found in the data.")
else:
    print("No text content found in the data.")

# Initialize a set to store unique classrooms
unique_classrooms = set()

# Initialize a list to store filtered data
filtered_data = []

# Iterate over each event and extract the required fields
for event in events:
    # Extract the required fields from the event
    classroomsIds = event.get('classroomsIds', [])
    classrooms_names = event.get('classroomsNames', [])
    classrooms_areas_ids = event.get('classroomsAreasIds', [])
    
    # Loop through the classrooms in the event
    for classroom_id, classroom_name, classroom_area_id in zip(classroomsIds, classrooms_names, classrooms_areas_ids):
        # Check if the classroom ID is already in the set
        if classroom_id not in unique_classrooms:
            # Add the classroom ID to the set
            unique_classrooms.add(classroom_id)
            
            # Construct a dictionary with the filtered data for the classroom
            classroom_data = {
                'classroomsIds': classroom_id,
                'classroomsNames': classroom_name,
                'classroomsAreasIds': classroom_area_id
            }
            
            # Append the filtered classroom data to the list
            filtered_data.append(classroom_data)

# Sort the filtered data by classroom ID in ascending order
filtered_data.sort(key=lambda x: x['classroomsIds'])

# Write the filtered data to a new JSON file
with open('data/filtered_data.json', 'w') as file:
    json.dump(filtered_data, file, indent=4)

print("Filtered data saved as JSON.")
