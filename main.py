import requests
from bs4 import BeautifulSoup as bs


def create_soup(url):
    temp_page = requests.get(url)
    if temp_page.status_code == 200:
        return bs(temp_page.content, 'html.parser')
    return None


def grab_values(container, classes):
    result = []
    for item in classes:
        result.append(container.find(class_=item).get_text())

    return result


def get_containers(_soup, container):
    return _soup.find_all(class_=container)


if __name__ == "__main__":
    print("Enter a url:")  # "https://webscraper.io/test-sites/e-commerce/allinone ")

    soup = create_soup(input().strip())
    print("Enter container class name")
    _container = get_containers(soup, input())
    print("Enter class fields. Enter empty line when finished:")
    c = []
    a = input()
    while str(a) != "":
        c.append(a)
        a = input()

    print('Scraping data...\n\n\n')

    for item in _container:
        print(grab_values(item, c))
