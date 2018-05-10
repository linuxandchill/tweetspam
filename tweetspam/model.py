#import libraries

from keras.layers.core import Dense
from keras.models import Sequential

#split data

#preprocess
#vectorize x and labels

#model architecture
model = models.Sequential()
model.add(layers.Dense(8, activation='relu', input_shape=(4000,)))
model.add(layers.Dense(8, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])

#compile

#fit

#evaluate
