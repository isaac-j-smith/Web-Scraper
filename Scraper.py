import requests
from bs4 import BeautifulSoup as bs


class Scraper:
    def __init__(self, url, container, category):

        self.category = category.split(", ")
        self.container = container
        self.url = url.strip()
        self.soup = None
        self.container_list = []

    def create_soup(self):
        temp_page = requests.get(self.url)
        if temp_page.status_code == 200:
            self.soup = bs(temp_page.content, 'html.parser')

    def grab_values(self, current_container):
        result = []
        for item in self.category:
            result.append(current_container.find(class_=item).get_text())

        return result

    def get_containers(self):
        self.container_list = self.soup.find_all(class_=self.container)

    def run(self):

        self.create_soup()

        self.get_containers()
        r = []
        for item in self.container_list:
            r.append(self.grab_values(item))

        return r
