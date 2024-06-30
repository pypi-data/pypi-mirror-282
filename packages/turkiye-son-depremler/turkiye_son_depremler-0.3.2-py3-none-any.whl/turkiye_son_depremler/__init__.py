import re
import requests
from bs4 import BeautifulSoup


class DepremData():
    def __init__(self):
        response = requests.get('http://www.koeri.boun.edu.tr/scripts/sondepremler.asp')
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            pre = soup.find('pre')
            pre_text = pre.text
            lines = pre_text.splitlines()
            items = []
            for line in lines[7:507]:
                l = line.replace('-.-', '0.0')
                l = re.sub("\\s{2,}", "#", l)
                cols = l.split('#')
                item = {
                    'TarihSaat': cols[0],
                    'Enlem': cols[1],
                    'Boylam': cols[2],
                    'Derinlik': cols[3],
                    'Siddet': cols[5],
                    'Konum': cols[7]
                }
                items.append(item)
            self.data = items
            self.count = len(items)
        else:
            self.data = []
            self.count = 0
