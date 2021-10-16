import requests
from bs4 import BeautifulSoup
import json

URL = 'https://saikaiscan.com.br/series'
def main(url_part_name_novel):
    """
    pass the novel name as a parameter, how is the url of the saikai website,
    to receive the informations.
    """

    url_format = f'{URL}/{url_part_name_novel}'

    page_source = requests.get(url_format)
    soup = BeautifulSoup(page_source.text, 'html.parser')

    def try_and_try(name, content):
        for pos , i in enumerate(content):
            if name in i:
                return pos + 1

    content = soup.find(class_ = '__content')
    content = content.text.split("\n")
    content = [i.strip() for i in content]
    content = [i for i in content if i != '']

    novel = {}

    img = soup.find(class_ = '__left').find('img')
    novel['image'] = img.attrs['src']

    name_and_initals = content[1].rsplit(' ', 1)
    novel['name_of_novel'] = name_and_initals[0]
    novel['initals'] = name_and_initals[1]

    novel['genre_of_novel'] = content[2]
    novel['chapters_of_novel'] = int(content[3].split(' ')[0])
    novel['status_of_active'] = content[5]

    rated_novel = content[6].strip().split(')')[0].split('(')
    novel['rated_novel'] = {"average":float(rated_novel[0].strip()),
                            "people_ratings":int(rated_novel[1].strip().split(' ')[0])}

    novel['original_language'] = content[7]
    try:
        novel['author'] = content[try_and_try('Autor', content)]
    except:
        pass

    novel['group'] = {}
    try:
        novel['group']['translator'] = content[try_and_try('Tradutor', content)]
    except:
        pass
    try:
        novel['group']['reviewer'] = content[try_and_try('Revisor', content)]
    except:
        pass
    try:
        novel['group']['QC'] = content[try_and_try('QC', content)]
    except:
        pass


    content_main = soup.find(id='synopsis-content').text
    novel['synopsis'] = content_main
    return novel

