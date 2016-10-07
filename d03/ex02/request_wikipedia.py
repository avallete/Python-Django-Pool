# -*- coding: utf-8 -*-

import requests
import json
import dewiki
import sys

class WikiApi(object):

    class WikiApiException(Exception):

        def __init__(self, msg=""):
            Exception.__init__(self, msg)

    endpoint = 'https://fr.wikipedia.org/w/api.php'
    search_params = {
        "format": "json",
        "action": "query",
        "generator": "prefixsearch",
        "gpslimit": "1",
        "prop": "revisions",
        "rvprop": "content",
        "redirects": ""
    }

    def __init__(self, search=None):
        if search == None:
            raise self.WikiApiException("You must specify something to search")
        if isinstance(search, str) and search.strip():
            self.filename = "_".join(search.split()) + ".wiki"
            self.search_params['gpssearch'] = search.lower().strip()
        else:
            raise self.WikiApiException("You must specify something to search")

    def parse_errors(self, response):
        if 'error' in response.keys():
            raise self.WikiApiException("Error in response: %s" % response['error']['info'])
        if 'warnings' in response.keys():
            raise self.WikiApiException("Warnings in response: %s" % response['warnings'])
        if 'query' not in response.keys():
            raise self.WikiApiException("No result for the search.")

    def search(self):
        rep = requests.get(self.endpoint, params=self.search_params)
        if rep.ok == False:
            raise self.WikiApiException("Error %s  :: %s" % (rep.status_code, rep.reason))
        self.parse_errors(rep.json())
        return rep.json()

    def get_text(self, response):
        pages = response["query"]["pages"]
        _, page_info = pages.popitem()
        return dewiki.from_string(page_info['revisions'][0]["*"])

    def fetch_and_write(self):
        data = self.search()
        data_string = self.get_text(data)
        with open(self.filename, 'w') as fd:
            fd.write(data_string)

def run(search):
    try:
        wiki = WikiApi(search)
        wiki.fetch_and_write()
    except WikiApi.WikiApiException as e:
        print(e)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        print("Bad number of arguments")