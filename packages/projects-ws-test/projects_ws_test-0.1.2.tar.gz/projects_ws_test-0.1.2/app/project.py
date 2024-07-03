# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import re
import datetime
from urllib.parse import urlparse
from .save_data_json import save_data_to_json, update_project_types, update_project_categories, update_external_id, update_users, update_group, update_memberships, load_project_data
from bs4 import BeautifulSoup
import uuid

import json

CACHE_FILE = 'cache.json'
CACHE_FILE_MEMBERS = 'cachemembers.json'
CACHE_DIR = 'pagecache'

cache_file = os.path.join(CACHE_DIR, CACHE_FILE)
cache_file_members = os.path.join(CACHE_DIR,CACHE_FILE_MEMBERS)

# Ensure the directory exists
os.makedirs(CACHE_DIR, exist_ok=True)

def load_cache(cache_file):
    try:
        with open(cache_file, 'r', encoding='utf-8') as file:
            cache = json.load(file)
    except FileNotFoundError:
        cache = []
    return set(cache)

def load_cache_mem(cache_file):
    try:
        with open(cache_file, 'r', encoding='utf-8') as file:
            cache = json.load(file)
    except FileNotFoundError:
        cache = {}
    return cache


def save_cache(cache):
    with open(cache_file, 'w', encoding='utf-8') as file:
        json.dump(list(cache), file, ensure_ascii=False, indent=2)

def save_cache_mem(cache):
    with open(cache_file_members, 'w', encoding='utf-8') as file:
        json.dump(cache, file, ensure_ascii=False, indent=2)

# end page uz nescrapne
def find_projects(driver, start_page=1, end_page=38):
    cache = load_cache(cache_file)  # Load cache at the start
    try:
        # Wait for the projects link to become clickable
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='https://vav.unob.cz/menu/projects']"))
        )
        # Click on the projects link
        element.click()

        # Navigate to the start page, invincible iterator :)
        for _ in range(1, start_page):
            try:
                link = driver.find_element(By.XPATH, "//a[@rel='next']")
                click_url = link.get_attribute('href')
                driver.find_element(By.XPATH, "//span[@class='nav nav-next']").click()
                # Update driver
                driver.get(click_url)
            except IndexError:
                print("Next link not found. Start page is beyond the last page.")
                return

        all_projects_data = []
        page_num = start_page

        # invincible iterator :)
        for _ in range(start_page, end_page):
            urls = urls_from_page(driver)
            print("\npage num:", page_num)
            # Data from projects
            projects_data_vector = extract_data_from_urls(driver, urls, cache)

            # Filter out blank projects, add if solver != ''
            non_blank_projects = [project for project in projects_data_vector if project['name'] != '' or project.get('name_en') != '']
            all_projects_data.extend(non_blank_projects)

            link = driver.find_elements(By.XPATH, "//a[@rel='next']")
            # Get the href attribute from the first matching <a> tag
            click_url = link[0].get_attribute('href')

            driver.find_element(By.XPATH, "//span[@class='nav nav-next']").click()

            # Update driver
            page_num += 1
            driver.get(click_url)

        # Save all project data here 
        save_data_to_json(all_projects_data)
        extract_data_from_users(driver)
        
        
    except Exception as e:
        print(f"Error occurred: {e}")
        
    finally:
        save_cache(cache)  # Save cache at the end
        #pass

def urls_from_page(driver):
    urls = []
    links = driver.find_elements(By.XPATH, '//a[@class="list"]')
    # Extract urls from page
    for link in links:
            url = link.get_attribute("href")  # Get the href attribute of each <a> tag
            if url:  # Check if the URL is not None or empty
                urls.append(url)

    return urls

def is_czech(text):
    # Regular expression to match Czech characters
    czech_pattern = r'[áčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]'
    return bool(re.search(czech_pattern, text))

def remove_special_characters(text):
    # Regular expression to match any character that is not alphanumeric, space, hyphen, or underscore
    pattern = r'[^a-zA-Z0-9\s\-_\.?!áčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ()–"]'
    # Substitute the matched characters with an empty string
    cleaned_string = re.sub(pattern, '', text)
    return cleaned_string

def parse_date(date_text):
    if "/ neuvedeno" in date_text:
        # If "/ neuvedeno" is present, return today's date
        return datetime.datetime.today()
    elif "neuvedeno" in date_text:
        # If "neuvedeno" is present, set the date to the first day of the month
        return datetime.datetime.strptime(date_text.split(" / ")[0], "%Y").replace(day=1, month=1)
    else:
        # If a specific date is provided, parse it accordingly
        return datetime.datetime.strptime(date_text, "%Y / %m")


def extract_data_from_urls(driver, urls, cache):
    projects = []
    cachemembers = load_cache_mem(cache_file_members)
    for url in urls:
        if url in cache:
            #print(f"Skipping already processed URL: {url}")
            continue
        driver.get(url)
        html = driver.page_source
        analyze_project(projects, url, html, cachemembers)
        driver.back()
        cache.add(url)  # Add URL to cache after processing
    return projects

def extract_data_from_users(driver):
    membersdict = load_cache_mem(cache_file_members)
    if not isinstance(membersdict, dict):
        raise ValueError("cachemembers must be a dictionary")
    
    project_map = load_project_data(filename="data/systemdata.json")
    
    for project_name, urls in membersdict.items():
        for url in urls:
            try:
                driver.get(url)
                html = driver.page_source
                if len(html.strip()) == 0:
                    print(f"Error: Received empty HTML content for URL {url}")
                    continue
                extract_data_from_solver(html, url, project_name, project_map)
            except Exception as e:
                print(f"Error occurred while processing URL {url}: {e}")

def extract_project_name(text):
    text = text.replace("\\", "").replace("\"", "")
    match = re.search(r'^(.*?)\s*(?:<br\s*/?>|\n)\s*(.*?)$', text, re.DOTALL)
    if match:
        part1 = match.group(1).strip()
        part2 = match.group(2).strip()
        if is_czech(part1):
            return remove_special_characters(part1), remove_special_characters(part2)
        else:
            return remove_special_characters(part2), remove_special_characters(part1)
    else:
        if is_czech(text):
            return remove_special_characters(text), ""
        else:
            return "", remove_special_characters(text)
        
def analyze_project(projects, url, html, cachemembers):
    soup = BeautifulSoup(html, 'html.parser')
        
    # Extract project name element
    project_name_element = soup.find('td', text="Název projektu/záměru")
    project_name_text = project_name_element.find_next_sibling('td').get_text(separator=' ').strip() if project_name_element else "Unnamed Project"
    project_name, project_name_en = extract_project_name(project_name_text)
    # Generate a unique ID for the project
    project_inner_id = str(uuid.uuid4())
    project_outer_id = str(urlparse(url).path.split('/')[-1])
    update_external_id(project_inner_id,project_outer_id,"abc0aecc-63e3-4e56-8402-c391214ab1e2")

    project_category_element = soup.find('td', text="Kategorie")
    project_category_text = project_category_element.find_next_sibling('td').get_text().strip() if project_category_element else "Unknown"
    project_category_id = update_project_categories(project_category_text)

    # Generate a unique ID for the project
    project_type_element = soup.find('td', text="Poskytovatel")
    project_type_text = project_type_element.find_next_sibling('td').get_text().strip() if project_type_element else "Unknown"
    project_type_id = update_project_types(project_type_text, project_category_id)

    # Find start year element
    start_year_element = soup.find('td', text="Zahájení rok / měsíc")
    start_year_text = start_year_element.find_next_sibling('td').get_text().strip() if start_year_element else "Unknown"

    # Parse start date as datetime
    start_date = parse_date(start_year_text)
        
    # Find end year element
    end_year_element = soup.find('td', text="Ukončení rok / měsíc")
    end_year_text = end_year_element.find_next_sibling('td').get_text().strip() if end_year_element else "Unknown"

    # Parse end date as datetime
    end_date = parse_date(end_year_text)

    project_solver_elements = soup.find_all('td', text=lambda text: text and ("Řešitel" in text or "Odpovědný řešitel" in text))
    links = []

    
        # Loop through all 'project_solver_elements' and extract URLs
    for project_solver_element in project_solver_elements:
        condition = project_solver_element.get_text()
        if condition == "Řešitelé nejsou uvedeni.":
            group_id = "unknown"
        else:    
            group_id = "unknown"    
            results = soup.find_all('table', class_='stripped list')

            for table in results:
                tds = table.find_all('td', class_='left-align')
                for td in tds:
                    a_tags = td.find_all('a')
                    for a_tag in a_tags:
                        member_url = a_tag.get('href')
                        if project_name == "":
                          project = project_name_en
                        else:
                            project = project_name

                        if project not in cachemembers:
                            cachemembers[project] = []
                        
                        if member_url not in cachemembers[project]:
                            cachemembers[project].append(member_url)
                            save_cache_mem(cachemembers)  # Save the cache dictionary to file
                            links.append((member_url, project))
                            
        
        group_id=update_group(project_name, project_name_en)

        project_data = {"id": project_inner_id, "name": project_name,"name_en": project_name_en,"projecttype_id": project_type_id, 
                        "startdate": start_date.isoformat(), "enddate": end_date.isoformat(), "group_id":group_id}
        
        
    #lze vracet project_data a append výše
    projects.append(project_data)   


# pak dat to jineho souboru, napr. utils
def extract_data_from_solver(html, url, project_name, project_map):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Check if there are any <h1> tags and print their count
    h1_tags = soup.find_all('h1')

    h1_tag = h1_tags[1]

    # Extract the full text from the <h1> tag
    firstname = h1_tag.text.split()[1]
    surname = h1_tag.text.split()[0] if len(h1_tag.text.split()[0]) > 1 else ""
    
    # Solver email
    solver_email_element = soup.find('td', text="Email")
    solver_email = solver_email_element.find_next_sibling('td').get_text().strip() if solver_email_element and solver_email_element.find_next_sibling('td').get_text().strip() else "Unknown"
    

    
    uco_element = soup.find('td', text="UČO")
    solver_uco = uco_element.find_next_sibling('td').get_text().strip() if uco_element else "Unknown"
    
    solver_workplace_element = soup.find('td', text="Pracoviště")
    solver_workplace = solver_workplace_element.find_next_sibling('td').get_text().strip() if solver_workplace_element and solver_workplace_element.find_next_sibling('td').get_text().strip() else "Unknown"

    workplace_parts = solver_workplace.split()
    solver_workplace = workplace_parts[0]
    # fakulta 
    #solver_fac = ''.join(workplace_parts[1]) if len(workplace_parts) > 1 else ""

    solver_inner_id=update_users(firstname, surname ,solver_email)

    update_memberships(project_map, project_name, solver_inner_id)
    
    update_external_id(solver_inner_id,solver_uco,"abc0aecc-63e3-4e56-8402-c391214ab1e2")