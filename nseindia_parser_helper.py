from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time, random
from dotenv import dotenv_values

class Helper:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--no-sandbox")
        proxy_config = dotenv_values(".env")
        proxy = {
                "proxy":
                    {
                        "https":f"{proxy_config['PROXY_TYPE']}" + 
                        f"://{proxy_config['PROXY_LOGIN']}:{proxy_config['PROXY_PASSWORD']}@{proxy_config['PROXY_IP']}:{proxy_config['PROXY_PORT']}"
                    }
            }
        self.driver = webdriver.Chrome(options=options, seleniumwire_options=proxy)
        print("[Log] WebDriver was create")

    def __hover_and_click_elemnt(self, element, element_name):
        try:
            self.__hover(element)
            print(f"[Log] Hover to element ({element_name})")
            self.__sleep(1, 5)
            element.click()
            print(f"[Log] Click on element ({element_name})")

        except NoSuchElementException or ElementNotInteractableException:
            print(f"[Error] Element ({element_name}) was not found or not interactable")
            exit()
    
    def __sleep(self, start_number, end_number):
        time.sleep(random.randint(start_number, end_number))

    def __hover(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def go_to_main_page(self):
        self.driver.get("https://www.nseindia.com")
        print("[Log] Going to website")
        self.__sleep(1, 5)

    def first_activity(self):
        try:
            self.__hover(self.driver.find_element(By.XPATH, "//a[text()='Market Data']"))
            print("[Log] Hover to Market Data")
            self.__sleep(1, 5)

        except NoSuchElementException or ElementNotInteractableException:
            print("[Error] Market Data button was not found or not interactable")
            exit() 
        self.__hover_and_click_elemnt(self.driver.find_element(By.XPATH, "//a[text()='Pre-Open Market']"), "Pre_Open_Market_button")
        time.sleep(random.randint(10, 15))

    def parse_data(self):
        try:
            filename = "TotalCost.csv"
            print("[Log] File for parsing was create")
            with open(filename,"w") as file:
                for element in self.driver.find_elements(By.XPATH, "//*[@id='livePreTable']/tbody/tr"):
                    name = element.find_element(By.XPATH, f"td[{1}]").text
                    final_price = element.find_element(By.XPATH, f"td[{6}]").text
                    print(f"[Log] Write Name: {name}; Final price: {final_price}")
                    file.write(name+";"+final_price+"\n")
            print("[Log] Writing data was finished")

        except Exception as ex:
            print(f"[Error] Writing failed: ({ex})")
            exit()
    
    def fake_activity(self):
        try:
            serach_bar = self.driver.find_element(By.ID, "header-search-input")
            self.__hover_and_click_elemnt(serach_bar, "Serach_bar")
            self.__sleep(1, 5)

            text_for_serach = self.driver.find_element(By.XPATH, f"//tr[{random.randint(2, 49)}]/td[{2}]").text
            serach_bar.send_keys(text_for_serach)
            print(f"[Log] Serach for {text_for_serach}")
            time.sleep(0.5)

            serach_bar.send_keys(Keys.ENTER)
            self.__sleep(1, 5)

        except NoSuchElementException or ElementNotInteractableException:
            print("[Error] Serach bar was not found or not interactable")
            exit() 

        try:
            scheight = 9.9
            while scheight > 0:
                self.driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight/{scheight});")
                scheight -= .01
            print("[Log] Window was scrolled")
            self.__sleep(1, 5)
        except Exception as ex:
            print(f"[Error] Scroll failed ({ex})")
            exit()

        self.__hover(self.driver.find_element(By.XPATH, "//a[text()='Market Data']"))
        print("[Log] Move to top menu")
        self.__sleep(1, 5)

        self.__hover_and_click_elemnt(self.driver.find_element(By.XPATH, 
            "//a[text()='Derivatives Market']"), "Derivatives_Market_button")
        self.__sleep(1, 5)

        self.__hover_and_click_elemnt(self.driver.find_element(By.XPATH, 
            "//div[@class='nav nav-tabs']/a[text()='Currency Derivatives']"), "Currency_Derivatives_button")
        self.__sleep(1, 5)

        self.__hover_and_click_elemnt(self.driver.find_element(By.ID, "table-currency"), "Table_currency")
        self.__sleep(1, 5)

        try:
            for element in self.driver.find_elements(By.CSS_SELECTOR, "tbody:nth-child(2) tr"):
                self.driver.execute_script("arguments[0].scrollIntoView(false)", element)
                time.sleep(0.0001)
            print("[Log] Scrolling table")
            self.__sleep(1, 5)
        except Exception as ex:
            print(f"[Error] Scroll failed ({ex})")
            exit()

    def close_driver(self):
        self.driver.quit()