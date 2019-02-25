from bs4 import BeautifulSoup
import requests


# TODO: fix this! for example, anchor tags not showing
def tag_visible(element):
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
    return " ".join(split) + "..."
