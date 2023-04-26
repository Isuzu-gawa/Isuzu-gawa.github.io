#!/usr/bin/env python3
from requests_html import AsyncHTMLSession

URL = 'https://www.yahoo.co.jp'
def wait_render():
    assesion = AsyncHTMLSession()

    async def process():
        r = await assesion.get(URL)
        await r.html.arender(wait=5, sleep=5)
        return r

    r = assesion.run(process)[0]
    print(r.html)

    print(r.html.find('#tabpanelTopics1', first=True).text)



if __name__ == "__main__":
    wait_render()