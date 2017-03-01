import urllib2 as ul
from bs4 import BeautifulSoup
import re, os, json

class Extraction(object):
    def __init__(self, url):
        req = ul.Request(url)
        response = ul.urlopen(req)
        page = response.read()
        self.soup = BeautifulSoup(page, "html.parser")

    def _getSourceSite(self):
        return self.soup.prettify()

    def _getTitle(self):
        return self.soup.title

    def _getListNewsUrl(self):
        return self.soup.find_all(href=re.compile('json\?url'))

    def _getUrlLength(self):
        return self._getListNewsUrl().__len__()

    def _writeUrltoTxt(self, filename):
        save = open(filename, 'w')
        for x in self._getListNewsUrl():
            save.write(x['href']+'\n')
        save.close()
        return True

    def _extractUrlFromFile(self, filename):
        load = open(filename, 'r+')
        url = []
        for link in load:
            url.append(link.replace('\n',''))
        load.close()
        tulisUrl = open('generateUrlBerita.txt', 'w')
        for item in url:
            jsonReq = ul.Request(item)
            jsonRes = ul.urlopen(jsonReq)
            data = json.load(jsonRes)
            for d in data:
                tulisUrl.write(d['link']+'\n')

        tulisUrl.close()

    def _getUrlLength(self, filename):
        hitung = open(filename, 'r')
        hasil = 0
        for it in hitung:
            hasil+=1

        return hasil

    def _generateTxtNews(self, filename):
        source = open(filename, 'r')
        counter = 0
        length = self._getUrlLength(filename)
        error = 0
        percentage = 0.00
        for item in source:
            try:
                request = ul.Request(item.replace('\n', ''))
                response = ul.urlopen(request)
                page = response.read()
                soup1 = BeautifulSoup(page, "html.parser")
                fName = "news/berita"+str(counter)+".txt"
                write = open(fName, 'w')
                write.write(soup1.find('article').text)
                write.close()
            except:
                error+=1

            counter+=1

            percentage = float(counter)/float(length)*100.00
            print round(percentage,2),"% Complete"
        print "Total URL: ", length
        percenErr = 0.00
        percenErr = float(error)/float(length)*100.00
        print "Broken URL: ", percenErr, "%(", error, ")"
        source.close()

url = "http://118.97.66.109/ro/dataset/databeritayangdipublish"
e = Extraction(url)
print e._generateTxtNews('generateUrlBerita.txt')





