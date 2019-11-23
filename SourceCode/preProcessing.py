import os

# import Sastrawi package
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
#import NLTK tokenizer
from nltk.tokenize import word_tokenize

def removeLines(dirname):
    count = 0
    delWord = ['Reporter', 'Foto']
    for file in os.listdir(dirname):
        count+=1
        if file.endswith(".txt"):
            f = open(dirname+"/"+file, "r")
            proc = f.readlines()
            f.close()
            path = "newsClean2/Clean_"+file
            wrCln = open(path, "w")
            
            for i in proc:
                if not any (dWord in i for dWord in delWord):
                    wrCln.write(i.lower().replace('.','').replace(',',''))
            wrCln.close()



def removeStop(dire):  
    
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()          
    r = open("stopwords_indo.txt", 'r')
    stopW = r.read()
    sW = stopW.split('\n')
    sW = set(sW)
    r.close()
    leng = 0
    for file in os.listdir(dire):
        if file.endswith(".txt"):
            leng+=1
    now = 0
    for file in os.listdir(dire):
        filtered = []
        if file.endswith(".txt"):
            rr = open(dire+"/"+file, "r")
            wToken = word_tokenize(stemmer.stem(rr.read()))
            rr.close()
            ss = open(dire+"/"+file, "w")
            for w in wToken:
                if w not in sW:
                    ss.write(w+" ")
                    filtered.append(w)
            #temp = rr.readlines()
            #for asd in rr:
            #    stemmer.stem(asd)
            ss.close()
            rr.close()
            now +=1
        print "Progess {} of {}.".format(now,leng)

def saringHoax(dire, tujuan):
    leng = 0
    for file in os.listdir(dire):
        if file.endswith(".txt"):
            leng+=1
    now = 0
    for file in os.listdir(dire):
        if file.endswith(".txt"):
            r = open(dire+"/"+file, "r")
            tmp = r.readlines()
            r.close()
            w = open(tujuan+"/"+file, "w")
            w.writelines(tmp[3:-20])
            w.close()
        now+=1
        print "Progess {} of {}.".format(now,leng)


#removeStop("news2")
#removeLines("news2")



#r = open('newsHoax/irjen-pol-tito-karnavian-diangkat-jadi-kepala-bnpt.txt', 'r')
#te = r.readlines()
#print te[3:-20]
#tas = open('Test.txt', 'w')
#tas.writelines(te[3:-20])
#tas.close()
#removeStop("newsHoaxClean")
#saringHoax("newsHoax", "newsHoaxClean")


