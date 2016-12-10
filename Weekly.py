#!/usr/bin/env python
__author__ = 'ASHISH'
import re, requests, bs4, time, sys


class Weekly():
    u_choice = []

    def __init__(self, show, se, ep):
        self.show = show
        self.se = se
        self.ep = ep
        self.u_choice = [self.show, self.se, self.ep]
        self.homepage()

    def extract(self, url, css):
        self.url = url
        self.css = css
        while True:
            try:
                global res
                res = requests.get(url, stream=True)
            except (Exception, requests.RequestException, ConnectionError, TimeoutError) as e:
                print(e)
                time.sleep(10)
                continue
            else:
                break
        if css == 'res1':
            return res
        else:
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            data = soup.select(css)
            return data
    def matching(self, term, data):
        self.data = data
        self.term = term
        tosearch= re.compile(self.term)
        for d in self.data:
            search = tosearch.search(d.text.lower())
            if search:
                return d.get('href')

    def homepage(self):
        url = "http://tvshows4mobile.com/search/list_all_tv_series/"
        css = '.data a'
        for choices in self.u_choice:
            shows_list = self.extract(url, css)
            url = self.matching(choices,shows_list)
        self.down(url)

    def down(self, arg):
        post_percent = 0
        dl = 0
        self.arg = arg
        css = '.data a'
        data = self.extract(self.arg, css)
        filename = data[0].text.replace('(TvShows4Mobile.Com).mp4', '')
        f_link = data[0].get('href')
        res = self.extract(f_link, 'res1')
        size = int(res.headers.get('content-length'))
        ask = input('Do you want to enter download location? : ')
        if ask == 'y' or ask == 'yes':
            down_loc = input('Enter the download location: ')
        else:
            down_loc = "C:\\downloads"
        print('\n\nFile Size: %.2f Mb' %(float(size/(1024*1024))))
        file = open('%s\%s.mp4' % (down_loc, filename), 'wb')
        for chunk in res.iter_content(chunk_size=1024):
            file.write(chunk)
            dl += len(chunk)
            percent = int((dl/size) * 100)
            if (percent % 2) == 0 and percent > post_percent:
                sys.stdout.write("\rDownloaded : %s%%" % percent)
                sys.stdout.flush()
                post_percent = percent
        print("\n\nCompleted")

