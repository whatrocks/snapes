from bs4 import BeautifulSoup
from bs4.element import Comment
import requests

# TODO: fix this!
# anchor tags not showing
def tag_visible(element):
    # if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
    #     return False
    # if isinstance(element, Comment):
    #     return False
    # return True
    if element.parent.name not in ['p', 'b', 'i']:
        return False
    return True

def get_text_from_url(url: str) -> str:
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = list(filter(tag_visible, texts))
    scraped = " ".join(t.strip() for t in visible_texts)
    split = scraped.split(' ')[:50]
    print(split)
    return " ".join(split) + "..."