# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 23:53:07 2017

@author: yanua
"""
#fusing multiple txt

import os

def iteratorDir(dirname):
    sent = []
    for file in os.listdir(dirname):
        if file.endswith(".txt"):
            f = open(dirname+file, "r")
            proc = f.read().split()
            f.close()
            sent.append(proc)

    return sent


# import modules & set up logging

import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def w2v(sent, savename):
    # train word2ve
    model = gensim.models.Word2Vec(sent, min_count=5, size=150)
    model.save(savename)
    return model

#load saved model w2v
def loadw2v(filename):
    model = gensim.models.Word2Vec.load(filename)
    return model    

#sent = iteratorDir("newsHoax/")
#model = w2v(sent, "hoaxW2vModel")
model = loadw2v("hoaxW2vModel")
print model.wv.similarity('islam', 'radikalisme')



