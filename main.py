from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

def main():
    url = "https://example.com/"
    repetitions = 1000  # how many times u wanna bot the site

    for _ in range(repetitions):
        driver = setup_chrome()
        
        driver.get(url)
        time.sleep(0.5)  # timefor page to load

        driver.quit()
        time.sleep(0)  # close browsercooldown

if __name__ == "__main__":
    main()
