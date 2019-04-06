import bs4

from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

import json
from collections import Counter

loc_list = []
intern_list = []

for i in range(2):  # Number of pages plus one
    page_url = "https://internshala.com/internships".format(i)
    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    containers = page_soup.findAll("div", {"class": "internship_meta"})
    all_details = []
    for container in containers:
        intern_details = {}
        initial = container.find("div",{"class":"table-cell"})
        internship = str(container.h4['title'])
        intern_details["internship"] = internship
        role = initial.find("a",{"class":"link_display_like_text"})
        organisation = str(role['title'])
        intern_details["organisation"] = organisation
        details = container.find("div",{"class":"individual_internship_details"})
        stipend = details.div.find("td",{"class" : "stipend_container_table_cell"}).text
        intern_details["stipend"] = stipend.strip()
        location = details.find("a",{"class" : "location_link"}).text
        intern_details["location"] = location
        start_date = details.find("div",{"id" : "start-date-first"}).text
        intern_details["start_date"] = start_date
        duration = container.find("table",{"class" : "table"}).tbody.select("td")[1].text
        intern_details["duration"] = duration
        posted_on = container.find("table",{"class" : "table"}).tbody.select("td")[3].text
        intern_details["posted_on"] = posted_on
        last_date_to_apply = container.find("table",{"class" : "table"}).tbody.select("td")[4].text
        intern_details["last_date_to_apply"] = last_date_to_apply
        all_details.append(intern_details)
#print(all_details)
with open('data/details.json','w') as f:
    json.dump(all_details,f)

