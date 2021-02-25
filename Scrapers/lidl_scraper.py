import json
import time
import pdb
import re
import traceback

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from selenium.common import exceptions

driver = webdriver.Chrome('../chromedriver.exe')
driver.get("https://www.lidl.com/stores")
chain = {"name": "Lidl", "stores": []}
default_delay = 0.5

locations = driver.find_elements_by_class_name("store-search-card")
for location in locations:
    url = location.find_element_by_tag_name("a").get_attribute("href")
    remote_id = re.sub("[^0-9]", "", url)
    address = location.find_element_by_class_name(
        "address").text.replace("\n", ", ")
    phone = None

    store = {"address": address, "phone": phone, "id": remote_id}
    chain["stores"].append(store)
    print("Added", store)

with open("../Outputs/lidl.json", "w") as f:
    json.dump(chain, f, indent=2)
print("Done")
