# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print("--- {0} seconds ---".format(time.time() - start_time))
        return res
    return wrapper


class Crawler():
    def __init__(self, web_address):
        self.full_html = ""
        self.web_address = web_address

        a = requests.get(web_address)# .content
        self.is_banned = False
        if a.status_code != 200:
            self.is_banned = True
        else:
            self.full_html = a.text
            self.relative_and_absolute_links = self.throught_the_html(self.full_html)
            self.urls_on_the_page = self.convert_relative_links(self.relative_and_absolute_links, web_address)
            text = self.get_readable_text(self.full_html)
            self.clear_text = text[1]
            self.string_text = text[0]
            self.count_of_words = len(self.clear_text)
            self.title = self.get_title(self.full_html)
        # print("words:" + str(self.count_of_words) + "->",)
        # print(text[2])
        # print(self.full_html)




    def get_html_on_the_page(self,web_aderess):
        a = requests.get(web_aderess)
        if a.status_code != 200:
            print("site doesn't like us")
        else:
            return a.text

    def get_title(self, text):
        # need h1..h6
        # b em i small strong sub sup ins del
        # code kbd samp var pre
        # abbr bdo blockquote q cite dfn p br hr
        soup = BeautifulSoup(text, 'html.parser')
        return soup.title.text

    def get_readable_text(self, text):
        # need h1..h6
        # b em i small strong sub sup ins del
        # code kbd samp var pre
        # abbr bdo blockquote q cite dfn p br hr
        soup = BeautifulSoup(text, 'html.parser')
        docs = []
        words = []
        text = ""
        # docs.append(soup.title.text)
        tag_array = {
            "a",
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "h6",
            "title",
            "span",
            "b",
            "p", 
        }

        for tag in tag_array:
            for content in soup.find_all(tag):
                docs.append(content.get_text())

        for frase in docs:
            if len(frase) != 0:
                text += frase + " "
                for word in frase.split(" "):
                    e = word.replace("'", "")
                    e = (e.replace(",", "")
                         .replace("(", "")
                         .replace(")", "")
                         .replace(")", "")
                         .replace("+", "")
                         .replace(".", "")
                         .replace("=", "")
                         .replace("[", "")
                         .replace("]", "")
                         .replace("{", "")
                         .replace("}", "")
                         # .replace(" ", "")
                         .lower()
                         .replace("\n", ""))
                    if len(e) == 0:
                        continue
                    words.append(e)
        return text, words, docs


    def throught_the_html(self, html_text):
        list_of_urls = []
        soup = BeautifulSoup(html_text, 'html.parser')
        for link in soup.find_all('a'):
            list_of_urls.append(link.get('href'))
        return list_of_urls

    def convert_relative_links(self, list_of_all_links, web_address):
        new_list = []
        # https and http

        if web_address.startswith("https"):
            web_address = re.findall(r'https://.+\.+[a-z]+', web_address)[0]
        else:
            web_address = re.findall(r'http://.+\.+[a-z]+', web_address)[0]

        for link in list_of_all_links:
            if link is None:
                continue
            if link.startswith("#"):
                continue
            if link.startswith("/"):
                new_list.append(web_address + link)
            if link.startswith("http"):
                new_list.append(link)
        return new_list

@benchmark
def main():
    c = Crawler("https://en.wikipedia.org/wiki/Free_content")
    print(c.string_text)


if __name__ == '__main__':
    main()
