from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import random
import os

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

CHROMEDRIVER_PATH = "./msedgedriver.exe" 
# Start WebDriver
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Edge(service=service)

search_terms = [
    "how to make pasta",
    "what is ai",
    "who won the world cup",
    "best programming language 2025",
    "is it going to rain today",
    "elon musk latest news",
    "what is quantum computing",
    "beautiful places to travel",
    "how to sleep better",
    "mental health tips"
]

try:
    for i in range(10):  
     

     driver.execute_script("window.open('');")
    
     driver.switch_to.window(driver.window_handles[-1])
    
     driver.get("https://www.bing.com")
     time.sleep(random.uniform(2, 4))  

     search_query = random.choice(search_terms)
     print(f"Searching in tab {i+1}: {search_query}")

     search_box = driver.find_element(By.NAME, "q")
     search_box.clear()
     search_box.send_keys(search_query)
     search_box.submit()

     time.sleep(random.uniform(3, 6))


finally:
    print("Closing browser...")
    driver.quit()
