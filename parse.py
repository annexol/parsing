from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import typing


class ParseApps:
    DELAY_TIME = 3.5  # waiting time to load page

    def __init__(self):
        self.url = 'https://apps.microsoft.com/store/category/Business'
        self.driver = self.scroll_page()
        self.links = self.get_links()[:200]
        self.data = self.get_information()

    def scroll_page(self, count=10) -> webdriver:

        """
        Scrolling page to get 200 apps links
        :param count:
        :return:
        """


        counter = 0
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)
        while counter < count:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(self.DELAY_TIME)
            counter += 1
        return self.driver

    def get_links(self) -> typing.List:

        """
        Getting apps links
        :return:
        """

        links = []
        content = self.driver.find_element(By.ID, 'all-products-listall-list-container').find_elements(By.TAG_NAME, 'a')
        for item in content:
            links.append(item.get_attribute('href'))
        return links

    def get_information(self) -> typing.List[typing.Dict]:

        """
        Getting data
        :return:
        """
        data = []
        for item in self.links:
            app = dict()
            self.driver.get(item)
            time.sleep(self.DELAY_TIME)
            app['name'] = self.driver.find_element(
                By.XPATH, '//*[@id="main"]/div/div/div[1]/div[2]/div[1]/div').find_element(By.TAG_NAME, 'h1').text

            realise_year = self.driver.find_elements(
                By.XPATH, '//*[@id="main"]/div/div/div[1]/div[3]/div[2]/div/div[1]/span/div/span'

            )

            if realise_year:
                realise_year = self.driver.find_element(
                    By.XPATH, '//*[@id="main"]/div/div/div[1]/div[3]/div[2]/div/div[1]/span/div/span'

                )
                realise_year = int(realise_year.text.split(': ')[-1])
            else:
                realise_year = None

            app['release_year'] = realise_year

            app['company_name'] = self.driver.find_element(
                By.XPATH, '//*[@id="main"]/div/div/div[1]/div[2]/div[1]/div/a').text

            button = self.driver.find_elements(By.CSS_SELECTOR, '#contactInfoButton_desktop')
            if button:
                self.driver.find_element(By.CSS_SELECTOR, '#contactInfoButton_desktop').click()

                email = self.driver.find_element(
                    By.XPATH, '//*[@id="main"]/div/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/p').text
            else:
                email = None

            app['email'] = email

            data.append(app)
        return data
