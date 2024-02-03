import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from classes import Beverage
from text_proccesser import init_beer
import time

LOAD_MORE_LENGTH = 20

s = Service('/Users/linusritchie/Desktop/CODE/genius/chromedriver')
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service = s, options = options)

def init_browser(link = "https://www.liquorland.co.nz/"):
    """google"""
    driver.get(link)
    yes = driver.find_element(By.CLASS_NAME, "col-6")
    yes.click()


def select_location(location = "Upper Riccarton"):
    location_button = driver.find_element(By.CLASS_NAME, "m-b-0")
    location_button.click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "locationName")))
    location_search = driver.find_element(By.ID, "locationName")
    location_search.send_keys(location)
    time.sleep(1)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'dropdown-item')))
    location_search.send_keys(Keys.RETURN)
    location_search.send_keys(Keys.RETURN)
    """select first option"""
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loadedStores"]/div[1]/div/div[3]/a')))
    first_option = driver.find_element(By.XPATH, '//*[@id="loadedStores"]/div[1]/div/div[3]/a')
    first_option.click()

def choose_instock():
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "showInStockItemsOnlyDesktop")))
    in_stock = driver.find_element(By.ID, "showInStockItemsOnlyDesktop")
    in_stock.click()

def get_info_from_page():
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "detail-title")))
        title = driver.find_element(By.CLASS_NAME, "detail-title")
        description = driver.find_element(By.ID, "collapseOne")
        price = driver.find_element(By.CLASS_NAME, "current-price")
        price = price.text[1:]
        return title, description, price

def get_beer_from_string(drink_name):
    """select beverage"""
    time.sleep(1)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "Query")))
    search = driver.find_element(By.ID, "Query")
    search.send_keys(drink_name + Keys.ENTER)
    """select first option"""
    # time.sleep(2)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'list-item')))
    first_option = driver.find_element(By.CLASS_NAME, 'list-item')
    first_option.click()
    """will have to check for out of stock and weather they match the description acuratley"""
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "detail-title")))
    title = driver.find_element(By.CLASS_NAME, "detail-title")
    description = driver.find_element(By.ID, "collapseOne")
    price = driver.find_element(By.CLASS_NAME, "current-price")
    price = price.text[1:]
    drink = init_beer(title.text, description.text, price)
    return drink

def get_beers_from_list(drink_names):
    init_browser()
    select_location()
    drinks = []
    for drink_name in drink_names:
        drinks.append(get_beer_from_string(drink_name))
    driver.close()
    return drinks

def get_beer_data():
    """
    Get all the beers on the page sequentially 
    then add them to the beers list
    Need to get the beer data then scroll 
    to the next beer and repeat untill 
    the end of page is reached and load more 
    is clicked or there are no more 
    beers and the program ends and driver is quit.
    """
    beers = []
    init_browser("https://www.liquorland.co.nz/shop/beer")
    select_location()
    choose_instock()
    content = 0
    while True:
        if content % LOAD_MORE_LENGTH == 0:
            try:
                load_more = driver.find_element(By.ID, "productListLoadMore")
                ActionChains(driver).scroll_to_element(load_more).perform()
                load_more.click()
                time.sleep(2)
            except:
                print("No More Pages")
        try:
            """click beer"""
            beer = driver.find_element(By.XPATH, '//a[@data-position="'+str(content)+'"]')
            ActionChains(driver).scroll_to_element(beer).perform()
            beer.click()
            """get beer data"""
            title, description, price = get_info_from_page()
            drink = init_beer(title.text, description.text, price)
            driver.back()
            beers.append(drink)
            content += 1
        except:
            print("No More Beers")
            break
    # driver.quit()
    return beers


