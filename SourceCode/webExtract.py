import urllib2 as ul
from bs4 import BeautifulSoup
import re, time, json, progressbar
import datetime as dt

#class for extract news from URL
class Extraction(object):
    url = ""
    def __init__(self, url):
        self.url = url
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

    def _doLog(self, info):
        l = open("log.txt", "a")
        l.write("\n{}: {}".format(dt.datetime.now(),info))
        l.close()

    def _generateTxtNews(self, filename, folder):
        startTime = time.time()
        source = open(filename, 'r')
        counter = 0
        length = self._getUrlLength(filename)
        error = 0
        percentage = 0.00
        
        for item in source:
            reItem = item.replace(',','').replace('_&_','').replace('?','').replace('+','').replace('*','').replace("'","").replace('!','').replace('"','')
            request = ul.Request(reItem)
            print reItem
            try:
                response = ul.urlopen(request)
            except ul.HTTPError, e:
                print "Error: %s"% str(e.code)
            except ul.URLError, e:
                print "Error: %s"% str(e.reason)
            try:
                page = response.read()
            except ul.httplib.IncompleteRead as e:
                page = e.partial
            
            soup1 = BeautifulSoup(page, "html.parser")
            arrItems = reItem.split('/')
            fName = "%s.txt"%arrItems[5].replace('\n', '').replace(':','').replace('*','').replace('?','').replace('"', '').replace('>','').replace('<','')
            try:
                write = open(folder+fName, 'w')
            except Exception as e:
                print e.message
            try:
                write.write(soup1.find('article').text.encode('utf-8').strip())
            except Exception as e:
                print e.message

            write.close()
            response.close()
            counter+=1
            #print "news/%s.txt" % arrItems[5].replace('\n', '')

            percentage = float(counter)/float(length)*100.00
            print round(percentage,2),"% Complete"
            #time.sleep(5)
        print "Total URL: %f" % length
        percenErr = 0.00
        percenErr = float(error)/float(length)*100.00
        print "Broken URL: ", percenErr, "%(", error, ")"
        elapsedTime = time.time()-startTime
        print "Time elapsed : %d" % elapsedTime
        source.close()
        lFile = "Last Text File Processed: {}".format(filename)
        self._doLog(lFile)

    def _getLinkFromPage(self, startz,sizeP, url):
        start = startz
        end = sizeP+1
        mVal = end - start
        cnt = 0
        bar = progressbar.ProgressBar(maxval=mVal, widgets=[progressbar.Bar(),' ', progressbar.Percentage()])
        bar.start()
        writeit = open('generateUrlBeritaHoax.txt', 'a')
        for x in range(start,end):
            ur = url+str(x)
            req = ul.Request(ur, headers={'User-Agent' : "Magic Browser"})
            try:
                res = ul.urlopen(req)
            except ul.HTTPError as e:
                print str(e)
            except ul.URLError as e :
                print str(e)
                input()
               
            try:
                page = res.read()
            except Exception as e:
                print e
            soup = BeautifulSoup(page, "html.parser")
            hasil = []
            for a in soup.find('div',id="detail-left").find_all('a', href=True):
                if "/read/" in a['href']:
                    #writeit.write("http://www.voa-islam.com"+a['href']+"\n")
                    hasil.append(a['href'])
                    
            newHasil = set(hasil)
            lastHasil = list(newHasil)
            
            for item in lastHasil:
                tulis = "http://www.voa-islam.com"+item+"\n" 
                writeit.write(tulis)
            cnt+=1
            bar.update(cnt)
            time.sleep(0.1)
                
        bar.finish()
            #time.sleep(2)
        writeit.close()
        
    def _generateTxtNewsHoax(self, filename, folder):
        startTime = time.time()
        source = open(filename, 'r')
        counter = 0
        length = self._getUrlLength(filename)
        error = 0
        percentage = 0.00
        print filename
        print "===================================="
        for item in source:
            reItem = item.replace(',','').replace('_&_','').replace('?','').replace('+','').replace('*','').replace('\n','')
            request = ul.Request(reItem,headers={'User-Agent' : "Magic Browser"})
            #print reItem
            try:
                response = ul.urlopen(request)
            except ul.HTTPError, e:
                print "Error: %s"% str(e.code)
                input()
            except ul.URLError, e:
                print "Error: %s"% str(e.reason)
                input()

            page = response.read()
            soup1 = BeautifulSoup(page, "html.parser")
            arrItems = reItem.split('/')
            fName = "%s.txt"%arrItems[9].replace('\n', '').replace(':','').replace('*','').replace('?','').replace('"', '').replace('>','').replace('<','')
            
            
            try:
                write = open(folder+fName, 'w')
            except Exception as e:
                print e.message
                input()
            try:
                write.write(soup1.find('div', id='the-content').text.encode('utf-8').strip())
            except Exception as e:
                print e.message
                input()

            write.close()
            response.close()
            counter+=1
            #print "news/%s.txt" % arrItems[5].replace('\n', '')
            
            percentage = float(counter)/float(length)*100.00
            print round(percentage,2),"% Complete"
            #time.sleep(5)
            
        print "Total URL: %f" % length
        percenErr = 0.00
        percenErr = float(error)/float(length)*100.00
        print "Broken URL: ", percenErr, "%(", error, ")"
        elapsedTime = time.time()-startTime
        print "Time elapsed : %d seconds" % elapsedTime
        source.close()
        lFile = "Last Text File Processed: {}".format(filename)
        self._doLog(lFile)
        print "=============================="
        print "End Of {}".format(filename)
        
        
        
url = "http://118.97.66.109/ro/dataset/databeritayangdipublish"
e = Extraction(url)
print e._generateTxtNews('tempgeneratenews.txt','news3/')
#listFiles = ['generateUrlBerita1.txt', 'generateUrlBerita2.txt', 'generateUrlBerita3.txt', 'generateUrlBerita4.txt', 'generateUrlBerita5.txt']
#threads = [threading.Thread(target=e._generateTxtNews, args=(fl,)) for fl in listFiles]
#for thread in threads:
#    thread.start()
#for thread in threads:
#    thread.join()

#e._generateTxtNews('generateUrlBerita2.txt')
#u = 'http://www.voa-islam.com/rubrik/politik-indonesia/page/'
#Get URL of the news 1-350 page.
#e._getLinkFromPage(251,350, u)
#Extract hoax news
#e._generateTxtNewsHoax('generateUrlBeritaHoax17.txt', 'newsHoax/')



