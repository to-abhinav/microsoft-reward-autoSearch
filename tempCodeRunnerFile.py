from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import random
import os

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")  # Uncomment if you don't want to see the browser

# Optional: Set path to chromedriver manually
CHROMEDRIVER_PATH = "./msedgedriver"  # Replace with path if needed

# Start WebDriver
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Edge(service=service)

# List of random search terms
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

# Open Bing and perform searches
try:
    for i in range(10):  # Do 10 searches
        driver.get("https://www.bing.com")
        time.sleep(random.uniform(2, 4))  # Wait for page load

        # Choose a random search term
        search_query = random.choice(search_terms)
        print(f"Searching: {search_query}")

        # Find the search box and enter the term
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(search_query)
        search_box.submit()

        # Wait randomly between 3 to 6 seconds
        time.sleep(random.uniform(3, 6))

finally:
    print("Closing browser...")
    driver.quit()
