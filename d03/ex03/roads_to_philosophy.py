# -*- coding: utf-8 -*-

import sys
import requests
from bs4 import BeautifulSoup

class WikiTools(object):

    endpoint = "https://en.wikipedia.org"

    class WikiException(Exception):

        def __init__(self, msg="Error: Wikipedia"):
            Exception.__init__(self, msg)

    def __init__(self):
        self.visited_pages = []
        self.road_len = 0

    def get_page_text(self, url):
        try:
            rep = requests.get(url)
        except Exception as e:
            raise self.WikiException("Error with requests.get module: %s" % str(e))
        if rep.ok == False:
            raise self.WikiException("Error get %s :: %s  :: %s" % (url, rep.status_code, rep.reason))
        return rep.text

    def get_url_formated_text(self, string):
        if (isinstance(string, str) and string.strip()):
            return ("/w/index.php?search=" + "+".join(string.split()))
        else:
            raise self.WikiException("Error: Your parameter must be a non-empty string.")

    def get_page_title(self, soup):
        if soup.h1:
            return soup.h1.get_text()
        else:
            raise self.WikiException("Error: No title on the webpage.")

    def get_page_redirections(self, soup):
        redirect_links = []
        for redirect in soup.find_all("span", {"class": "mw-redirectedfrom"}):
            redirect_links.append(redirect.a.get_text())
        return redirect_links

    def isarticle(self, url):
        if url[0:6] == "/wiki/" and url[6:].find(':') == -1:
            return True
        return False

    def get_next_link(self, soup):
        content = soup.find("div", {"id": "mw-content-text"})
        if not content or not content.find("p", recursive=False):
            raise self.WikiException("It leads to a dead end !")
        for link in soup.find("div", {"id": "mw-content-text"}).find("p", recursive=False).find_all("a"):
            if 'href' in link.attrs.keys() and self.isarticle(link.attrs['href']):
                return "%s%s" % (self.endpoint, link.attrs['href'])
        raise self.WikiException("It leads to a dead end !")

    def road_to(self, start, dest="Philosophy"):
        html_string = self.get_page_text(self.endpoint + start)
        soup = BeautifulSoup(html_string, 'html.parser')
        while 42:
            if (self.get_page_title(soup) not in self.visited_pages):
                self.visited_pages += self.get_page_redirections(soup)
                self.visited_pages.append(self.get_page_title(soup))
                self.road_len += 1
                if self.get_page_title(soup) == dest:
                    return (self.visited_pages, self.road_len)
                html_string = self.get_page_text(self.get_next_link(soup))
                soup = BeautifulSoup(html_string, 'html.parser')
            else:
                raise self.WikiException("It leads to an infinite loop !")

def run(search):
    try:
        wt = WikiTools()
        road, road_len = wt.road_to(wt.get_url_formated_text(search), "Philosophy")
        for way in road:
            print(way)
        print("%s roads from %s to philosophy" % (road_len, search))
    except WikiTools.WikiException as e:
        print(e)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        print("Bad number of arguments")

