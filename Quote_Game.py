from bs4 import BeautifulSoup
import requests
import time
import random


class QuotesQuizGame:
    _high_score = 0
    # http://quotes.toscrape.com/page/{page_no}/
    _url = "http://quotes.toscrape.com"
    _no_of_pages = 2  # max can be 10

    def __init__(self, guesses=4, quotes=[]):
        self.guesses = guesses
        self.quotes = quotes
        self._scrape_quotes()

    def _scrape_quotes(self):
        page_nos = []
        for i in range(self._no_of_pages + 1):
            num = random.randint(1, 10)
            if not num in page_nos:
                page_nos.append(num)
        for page_no in page_nos:
            res = requests.get(f"{self._url}/page/{page_no}/")
            soup = BeautifulSoup(res.text, 'html.parser')
            quotes = soup.select(".quote")
            for quote in quotes:
                data = {
                    "quote_text": quote.find(class_="text").get_text(),
                    "author": quote.find(class_="author").get_text(),
                    "author_bio": quote.find("a")["href"]
                }
                self.quotes.append(data)
            page_no += 1
            # wait 10 sec before next request
            time.sleep(5)

    def _remove_quote(self, quote):
        self.quotes.remove(quote)

    def get_all_quotes(self):
        return self.quotes

    def get_quote(self):
        if len(self.quotes) > 0:
            quote = random.choice(self.quotes)
            self._remove_quote(quote)
            return quote
        else:
            return None

    def get_author_bio(self, author_bio):
        res = requests.get(f"{self._url}{author_bio}/")
        soup = BeautifulSoup(res.text, 'html.parser')
        author_born_date = soup.select(".author-born-date")[0].getText()
        author_born_location = soup.select(
            ".author-born-location")[0].getText()
        return {
            "author_born_date": author_born_date,
            "author_born_location": author_born_location
        }

    def author_name_hint(self, author):
        name_array = author.split(" ")
        firstName_letter = name_array[0][0].upper()
        lastName_letter = name_array[-1][0].upper()
        return {
            "first_name": firstName_letter,
            "last_name": lastName_letter
        }
