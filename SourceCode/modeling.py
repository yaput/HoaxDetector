# Create first network with Keras
from keras.models import Sequential
from keras.layers import Dense
import keras
from keras.preprocessing import text
import numpy

# load pima indians dataset
r = open("newsClean/Clean_Rumah_Mewah_di_Lebak_Bulus_Terbakar.txt","r")
a = r.read()
r.close()
r = open("newsClean/Clean_Saluran_di_Kota_Tua_Diminta_Dibenahi.txt","r")
b = r.read()
r.close()
lis = []
lis.append(a)
lis.append(b)
t = keras.preprocessing.text.Tokenizer()
t.fit_on_texts(lis)

# split into input (X) and output (Y) variables
X = t.texts_to_matrix(lis, mode='tfidf')
print len(X[0])
ou = [1,1]
Y = numpy.array(ou)
# create model
model = Sequential()
model.add(Dense(12, input_dim=137, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, nb_epoch=150, batch_size=10,  verbose=2)
# calculate predictions
predictions = model.predict(X)
# round predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)