import json
import os
import numpy as np
import uuid
import re
from datetime import datetime 

# quick fix
class NumpyArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()  # Convert numpy array to list
        return json.JSONEncoder.default(self, obj)

def save_data_to_json(data_vectors):
    
    with open('data/systemdata.json', 'r', encoding='utf-8') as file:
        projects = json.load(file)

    projects['projects'].extend(data_vectors)

    with open('data/systemdata.json', 'w', encoding='utf-8') as file:
        json.dump(projects, file, ensure_ascii=False, indent=2)

    print(f"Data saved...")

def update_project_types(project_type_text, project_category_id):
    # Use regular expression to extract text inside parentheses
    match = re.search(r'\((.*?)\)', project_type_text)
    if match:
        extracted_text = match.group(1).replace(" ", "")
        # Load the existing project types from the JSON file
        with open('data/systemdata.json', 'r', encoding='utf-8') as file:
            project_types = json.load(file)

        # Check if the project type already exists
        existing_types = [ptype['name'] for ptype in project_types['projecttypes']]
        if extracted_text not in existing_types:
            # Generate a new UUID for the project type
            new_id = str(uuid.uuid4())

            # Add the new project type to the list
            new_project_type = {
                "id": new_id,
                "name": extracted_text,
                "name_en": extracted_text,
                "category_id": project_category_id
            }
            project_types['projecttypes'].append(new_project_type)

            # Save the updated project types back to the JSON file
            with open('data/systemdata.json', 'w', encoding='utf-8') as file:
                json.dump(project_types, file, ensure_ascii=False, indent=2)

            print(f"New project type '{extracted_text}' added with ID '{new_id}'.")
            return new_id  # Return the new ID
        else:
            # If the project type already exists, find its ID
            for ptype in project_types['projecttypes']:
                if ptype['name'] == extracted_text:
                    return ptype['id']

    # If no match found or project type is not added and not found, return None
    return None

def update_project_categories(project_category_text):

        extracted_text = project_category_text
        # Load the existing project types from the JSON file
        with open('data/systemdata.json', 'r', encoding='utf-8') as file:
            project_categories = json.load(file)

        # Check if the project type already exists
        existing_types = [ctype['name'] for ctype in project_categories['projectcategories']]
        if extracted_text not in existing_types:
            # Generate a new UUID for the project type
            new_id = str(uuid.uuid4())

            # Add the new project type to the list
            new_project_type = {
                "id": new_id,
                "name": extracted_text,
                "name_en": extracted_text,
            }
            project_categories['projectcategories'].append(new_project_type)

            # Save the updated project types back to the JSON file
            with open('data/systemdata.json', 'w', encoding='utf-8') as file:
                json.dump(project_categories, file, ensure_ascii=False, indent=2)

            print(f"New project category '{extracted_text}' added with ID '{new_id}'.")
            return new_id  # Return the new ID
        else:
            # If the project type already exists, find its ID
            for ctype in project_categories['projectcategories']:
                if ctype['name'] == extracted_text:
                    return ctype['id']

def filter_json_file_for_partial_string(filename, search_substring):
    filepath = os.path.join("data", filename)

    # Read the JSON file
    with open(filepath, 'r', encoding='utf-8') as json_file:
        data_dict = json.load(json_file)

    # Initialize lists to store matches
    matches = {}

    # Search for the specified substring in all data types
    for data_type, data_vector in data_dict.items():
        if isinstance(data_vector, list):  # Check if data_vector is a list
            data_matches = [item for item in data_vector if search_substring in str(item)]
            matches[data_type] = data_matches

    # Print matches found for each data type
    for data_type, data_matches in matches.items():
        print(f"Matches in {data_type} containing '{search_substring}':")
        for match in data_matches:
            print(match)



def update_external_id(inner_id, outer_id, external_type_id):
        # Load the existing project types from the JSON file
        with open('data/systemdata.json', 'r', encoding='utf-8') as file:
            external = json.load(file)

        # Check if the project type already exists
        existing_outer_id = [extype['outer_id'] for extype in external['externalids']]
        new_uuid = str(uuid.uuid4())
        if outer_id not in existing_outer_id:
            # Add the new project type to the list
            new_external_id = {
                "id": new_uuid,
                "inner_id": inner_id,
                "outer_id": outer_id,
                "typeid_id": external_type_id
            }
            external['externalids'].append(new_external_id)

            # Save the updated project types back to the JSON file
            with open('data/systemdata.json', 'w', encoding='utf-8') as file:
                json.dump(external, file, ensure_ascii=False, indent=2)

            #print(f"New external ID '{new_uuid}' added with outer ID '{outer_id}' from source '{external_type_id}'.")


def update_users(name, surname, email):
        # Load the existing users from the JSON file
        with open('data/systemdata.json', 'r', encoding='utf-8') as file:
            users = json.load(file)

        # Check if the user already exists
        existing_surname = [extype['surname'] for extype in users['users']]
        new_uuid = str(uuid.uuid4())
        
        if surname not in existing_surname:
            # Add the new user to the list
            new_external_id = {
                "id": new_uuid,
                "name": name,
                "surname": surname,
                "email": email
            }
            users['users'].append(new_external_id)

            # Save the updated user back to the JSON file
            with open('data/systemdata.json', 'w', encoding='utf-8') as file:
                json.dump(users, file, ensure_ascii=False, indent=2)

            # print(f"New user with ID '{new_uuid}' added with user name: '{name}' '{surname}'.")
            return new_uuid
        else:
            for user in users['users']:
                if user['surname'] == surname:
                    return user['id']

def update_group(name, name_en):
    # Load the existing group from the JSON file
    with open('data/systemdata.json', 'r', encoding='utf-8') as file:
        groups = json.load(file)

    # Check if the group already exists
    for group in groups['groups']:
        if (name and group['name'] == name) or (name_en and group['name_en'] == name_en):
            return group['id']

    valid = True
    lastchange = datetime.today().isoformat()
    new_uuid = str(uuid.uuid4())
    
     # If no matching group is found, create a new one
    new_external_id = {
        "id": new_uuid,
        "name": name if name else "",
        "name_en": name_en if name_en else "",
        "lastchange": lastchange,
        "valid": valid,
        "mastergroup_id": "",
        "grouptype_id": ""
    }
    groups['groups'].append(new_external_id)

    # Save the updated group back to the JSON file
    with open('data/systemdata.json', 'w', encoding='utf-8') as file:
        json.dump(groups, file, ensure_ascii=False, indent=2)

    #print(f"New group with ID '{new_uuid}' added with group name: '{name}'.")
    return new_uuid

def load_project_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    project_map = {}
    for project in data.get('projects', []):
        project_name = project['name'] if project['name'] else project['name_en']
        group_id = project['group_id']
        project_map[project_name] = group_id
    
    return project_map


# melo by fungovat
def update_memberships(project_map, project_name, userID):
        # Load the existing memberships from the JSON file
        with open('data/systemdata.json', 'r', encoding='utf-8') as file:
            memberships = json.load(file)

        # Check if the memberships already exists
        existing_user = [extype['user_id'] for extype in memberships['memberships']]
        new_uuid = str(uuid.uuid4())
        
        valid = True
        groupID = project_map[project_name]
        if userID not in existing_user:
            # Add the new memberships to the list
            new_external_id = {
                "id": new_uuid,
                "user_id": userID,
                "group_id": groupID,
                "valid": valid
            }
            memberships['memberships'].append(new_external_id)

            # Save the updated memberships back to the JSON file
            with open('data/systemdata.json', 'w', encoding='utf-8') as file:
                json.dump(memberships, file, ensure_ascii=False, indent=2)

