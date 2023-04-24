#!/usr/bin/env python3

from requests_html import HTMLSession
session = HTMLSession()
url = "https://isuzu-gawa.github.io/getlocation/gps-json.html"
r = session.get(url)
r.html.render()
print(type(r.html))
print(r.html.find('#resdiv', first=True).text)
