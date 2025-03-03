import requests
from bs4 import BeautifulSoup
import os
import re

def sanitize_filename(filename):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', filename)

def save_article_as_html(url, output_folder="saved_articles"):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "article"
        sanitized_title = sanitize_filename(title)
        filename = sanitized_title + ".html"
        filepath = os.path.join(output_folder, filename)

        os.makedirs(output_folder, exist_ok=True)

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(soup.prettify())

        print(f"Article saved: {filepath}")
    except Exception as e:
        print(f"Error saving article: {e}")


# Példa használatra
url = "https://example.com/sample-article"
save_article_as_html(url)
