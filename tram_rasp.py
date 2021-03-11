import requests
from bs4 import BeautifulSoup
import math

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.400',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}


def start(s):
    URL = 'https://busti.me/krasnodar/tramway-' + s + '/?hl=ru'

    stopsname1 = []
    stopsname2 = []

    def get_html(url, params=None):
        r = requests.get(url, HEADERS)
        return r

    def get_content(html):
        stroka = ""
        timestr = ""
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('table'):
            if link.get('id') == 'd0':
                for item in link.find_all('tr'):
                    if item.find_all('div', class_='ui labels'):
                        stroka = item.find('div', class_='ft').get_text() + " " + item.b.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname1.append(stroka)
                    else:
                        stroka = item.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname1.append(stroka)
            elif link.get('id') == 'd1':
                for item in link.find_all('tr'):
                    if item.find_all('div', class_='ui labels'):
                        stroka = item.find('div', class_='ft').get_text() + " " + item.b.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname2.append(stroka)
                    else:
                        stroka = item.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname2.append(stroka)

    def result():
        side1 = ""
        side2 = ""
        for item in range(len(stopsname1)):
            side1 = side1 + str(stopsname1[item]) + "\n"
        for item in range(len(stopsname2)):
            side2 = side2 + str(stopsname2[item]) + "\n"
        return "От " + side1 + "\nОт " + side2

    def parse():
        html = get_html(URL)
        if html.status_code == 200:
            get_content(html.text)
        else:
            print('Error')

    parse()
    return result()


def krastrolleybus(s):
    URL = "https://busti.me/krasnodar/trolleybus-" + s + "/"

    stopsname1 = []
    stopsname2 = []

    def get_html(url, params=None):
        r = requests.get(url, HEADERS)
        return r

    def get_content(html):
        stroka = ""
        timestr = ""
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('table'):
            if link.get('id') == 'd0':
                for item in link.find_all('tr'):
                    if item.find_all('div', class_='ui labels'):
                        stroka = item.find('div', class_='ft').get_text() + " " + item.b.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname1.append(stroka)
                    else:
                        stroka = item.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname1.append(stroka)
            elif link.get('id') == 'd1':
                for item in link.find_all('tr'):
                    if item.find_all('div', class_='ui labels'):
                        stroka = item.find('div', class_='ft').get_text() + " " + item.b.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname2.append(stroka)
                    else:
                        stroka = item.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname2.append(stroka)

    def result():
        side1 = ""
        side2 = ""
        for item in range(len(stopsname1)):
            side1 = side1 + str(stopsname1[item]) + "\n"
        for item in range(len(stopsname2)):
            side2 = side2 + str(stopsname2[item]) + "\n"
        return "От " + side1 + "\nОт " + side2

    def parse():
        html = get_html(URL)
        if html.status_code == 200:
            get_content(html.text)
        else:
            print('Error')

    parse()
    return result()


def krasbus(s):
    URL = "https://busti.me/krasnodar/bus-" + s + "/"

    stopsname1 = []
    stopsname2 = []

    def get_html(url, params=None):
        r = requests.get(url, HEADERS)
        return r

    def get_content(html):
        stroka = ""
        timestr = ""
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('table'):
            if link.get('id') == 'd0':
                for item in link.find_all('tr'):
                    if item.find_all('div', class_='ui labels'):
                        stroka = item.find('div', class_='ft').get_text() + " " + item.b.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname1.append(stroka)
                    else:
                        stroka = item.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname1.append(stroka)
            elif link.get('id') == 'd1':
                for item in link.find_all('tr'):
                    if item.find_all('div', class_='ui labels'):
                        stroka = item.find('div', class_='ft').get_text() + " " + item.b.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname2.append(stroka)
                    else:
                        stroka = item.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname2.append(stroka)

    def result():
        side1 = ""
        side2 = ""
        for item in range(len(stopsname1)):
            side1 = side1 + str(stopsname1[item]) + "\n"
        for item in range(len(stopsname2)):
            side2 = side2 + str(stopsname2[item]) + "\n"
        return "От " + side1 + "\nОт " + side2

    def parse():
        html = get_html(URL)
        if html.status_code == 200:
            get_content(html.text)
        else:
            print('Error')

    parse()
    return result()

def rastbus(s):
    URL = "https://busti.me/rostov/bus-" + s + "/"

    stopsname1 = []
    stopsname2 = []

    def get_html(url, params=None):
        r = requests.get(url, HEADERS)
        return r

    def get_content(html):
        stroka = ""
        timestr = ""
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('table'):
            if link.get('id') == 'd0':
                for item in link.find_all('tr'):
                    if item.find_all('div', class_='ui labels'):
                        stroka = item.find('div', class_='ft').get_text() + " " + item.b.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname1.append(stroka)
                    else:
                        stroka = item.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname1.append(stroka)
            elif link.get('id') == 'd1':
                for item in link.find_all('tr'):
                    if item.find_all('div', class_='ui labels'):
                        stroka = item.find('div', class_='ft').get_text() + " " + item.b.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname2.append(stroka)
                    else:
                        stroka = item.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname2.append(stroka)

    def result():
        side1 = ""
        side2 = ""
        for item in range(len(stopsname1)):
            side1 = side1 + str(stopsname1[item]) + "\n"
        for item in range(len(stopsname2)):
            side2 = side2 + str(stopsname2[item]) + "\n"
        return "От " + side1 + "\nОт " + side2

    def parse():
        html = get_html(URL)
        if html.status_code == 200:
            get_content(html.text)
        else:
            print('Error')

    parse()
    return result()

def rastrolleubus(s):
    URL = "https://busti.me/rostov/trolleybus-" + s + "/"

    stopsname1 = []
    stopsname2 = []

    def get_html(url, params=None):
        r = requests.get(url, HEADERS)
        return r

    def get_content(html):
        stroka = ""
        timestr = ""
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('table'):
            if link.get('id') == 'd0':
                for item in link.find_all('tr'):
                    if item.find_all('div', class_='ui labels'):
                        stroka = item.find('div', class_='ft').get_text() + " " + item.b.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname1.append(stroka)
                    else:
                        stroka = item.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname1.append(stroka)
            elif link.get('id') == 'd1':
                for item in link.find_all('tr'):
                    if item.find_all('div', class_='ui labels'):
                        stroka = item.find('div', class_='ft').get_text() + " " + item.b.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname2.append(stroka)
                    else:
                        stroka = item.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname2.append(stroka)

    def result():
        side1 = ""
        side2 = ""
        for item in range(len(stopsname1)):
            side1 = side1 + str(stopsname1[item]) + "\n"
        for item in range(len(stopsname2)):
            side2 = side2 + str(stopsname2[item]) + "\n"
        return "От " + side1 + "\nОт " + side2

    def parse():
        html = get_html(URL)
        if html.status_code == 200:
            get_content(html.text)
        else:
            print('Error')

    parse()
    return result()

def rastram(s):
    URL = "https://busti.me/rostov/tramway-" + s + "/"

    stopsname1 = []
    stopsname2 = []

    def get_html(url, params=None):
        r = requests.get(url, HEADERS)
        return r

    def get_content(html):
        stroka = ""
        timestr = ""
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('table'):
            if link.get('id') == 'd0':
                for item in link.find_all('tr'):
                    if item.find_all('div', class_='ui labels'):
                        stroka = item.find('div', class_='ft').get_text() + " " + item.b.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname1.append(stroka)
                    else:
                        stroka = item.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname1.append(stroka)
            elif link.get('id') == 'd1':
                for item in link.find_all('tr'):
                    if item.find_all('div', class_='ui labels'):
                        stroka = item.find('div', class_='ft').get_text() + " " + item.b.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname2.append(stroka)
                    else:
                        stroka = item.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname2.append(stroka)

    def result():
        side1 = ""
        side2 = ""
        for item in range(len(stopsname1)):
            side1 = side1 + str(stopsname1[item]) + "\n"
        for item in range(len(stopsname2)):
            side2 = side2 + str(stopsname2[item]) + "\n"
        return "От " + side1 + "\nОт " + side2

    def parse():
        html = get_html(URL)
        if html.status_code == 200:
            get_content(html.text)
        else:
            print('Error')

    parse()
    return result()

def mrast(s):
    URL = "https://busti.me/rostov/bus-intercity-" + s + "/"

    stopsname1 = []
    stopsname2 = []

    def get_html(url, params=None):
        r = requests.get(url, HEADERS)
        return r

    def get_content(html):
        stroka = ""
        timestr = ""
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('table'):
            if link.get('id') == 'd0':
                for item in link.find_all('tr'):
                    if item.find_all('div', class_='ui labels'):
                        stroka = item.find('div', class_='ft').get_text() + " " + item.b.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname1.append(stroka)
                    else:
                        stroka = item.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname1.append(stroka)
            elif link.get('id') == 'd1':
                for item in link.find_all('tr'):
                    if item.find_all('div', class_='ui labels'):
                        stroka = item.find('div', class_='ft').get_text() + " " + item.b.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname2.append(stroka)
                    else:
                        stroka = item.get_text()
                        stroka = stroka.replace('   ', '')
                        stroka = stroka.replace('\n', '')
                        stopsname2.append(stroka)

    def result():
        side1 = ""
        side2 = ""
        for item in range(len(stopsname1)):
            side1 = side1 + str(stopsname1[item]) + "\n"
        for item in range(len(stopsname2)):
            side2 = side2 + str(stopsname2[item]) + "\n"
        return "От " + side1 + "\nОт " + side2

    def parse():
        html = get_html(URL)
        if html.status_code == 200:
            get_content(html.text)
        else:
            print('Error')

    parse()
    return result()
