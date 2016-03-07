from bs4 import BeautifulSoup
from collections import namedtuple
import urllib.request

url_base = "http://www.allrecipes.com"


def get_recipe_from_file(file):
    text = open(file).read()
    return get_recipe_from_text(text)


def get_recipe_from_url(url):
    text = urllib.request.urlopen(url).read()
    return get_recipe_from_text(text)


def get_recipe_from_text(text):
    soup = BeautifulSoup(text, 'html.parser')
    ingredient_spans = soup.find_all("span", "recipe-ingred_txt added")
    ingredients = list()
    for ingredSpan in ingredient_spans:
        ingredient = ingredSpan.get_text()
        ingredients.append(ingredient)

    recipe = {'name': soup.find('title').get_text(), 'ingredients': ingredients}

    return recipe


def get_recipe_links(url):
    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')

    links = soup.find_all(has_referrer_link)
    link_list = set()
    for link in links:
        link_text = link.get("href")
        if "recipe" in link_text and "allrecipes" not in link_text:
            link_list.add(url_base+link_text)

    return link_list


# Function to determine if a referrer link is present
def has_referrer_link(tag):
    return not tag.has_attr("data-click-id") and tag.has_attr("data-internal-referrer-link")
