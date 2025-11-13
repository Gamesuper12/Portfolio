import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep


def parsing():
    with webdriver.Chrome() as browser:
        browser.get('https://example.con')
        sleep(5)

        seen_products = set()

        wait = WebDriverWait(browser, 20)

        clicks = 0
        all_parced = 0
        #пагинация по кнопке "Показать ещё"
        while clicks < 6:
            print(f'Начинаем цикл {clicks + 1}')

            products = wait.until(ec.visibility_of_all_elements_located(('some selector')))
            for product in products:
                
                name = product.find_element('some selector')
                    
                price = WebDriverWait(product, 20).until(ec.presence_of_element_located(('some selector')))
                    
                available = WebDriverWait(product, 20).until(ec.presence_of_element_located(('some selector')))

                link = product.find_element('some selector')

                yield {'name': name, 'price': price, 'available': available, 'link': link}
            
            
                btn = wait.until(ec.element_to_be_clickable(('some selector')))

                browser.execute_script('arguments[0].scrollIntoView();', btn)

                browser.execute_script('arguments[0].click();', btn)
                clicks += 1

                wait.until(ec.presence_of_element_located(('some selector')))

