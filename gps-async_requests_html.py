#!/usr/bin/env python3
from requests_html import AsyncHTMLSession

URL = "https://isuzu-gawa.github.io/getlocation/gps-json.html"
def wait_render():
    assesion = AsyncHTMLSession()

    async def process():
        r = await assesion.get(URL)
        await r.html.arender(wait=5, sleep=5)
        return r

    r = assesion.run(process)[0]
    print(r.html)

    print(r.html.find('#resdiv', first=True).text)



if __name__ == "__main__":
    wait_render()