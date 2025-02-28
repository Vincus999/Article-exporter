import requests
from bs4 import BeautifulSoup
import os

#This code is going to export articles to a local folder and storages it in HTML format.
def save_article_as_html(url, output_folder="saved_articles"): #This will create a folder, where the saved articles go
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "article"
        filename = "_".join(title.split()) + ".html"
        filepath = os.path.join(output_folder, filename)

        os.makedirs(output_folder, exist_ok=True)

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(soup.prettify()) #With this you can save articles in the same format as you downloaded them

        print(f"Article saved: {filepath}")
    except Exception as e:
        print(f"Error saving article: {e}")


#Example input format
url = "https://example.com/sample-article"
save_article_as_html(url)

