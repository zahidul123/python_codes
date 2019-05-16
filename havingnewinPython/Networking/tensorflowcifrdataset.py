from keras.datasets import cifar10
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense,Flatten,Dropout,Activation
from keras.layers.convolutional import Conv2D,MaxPooling2D
from keras.optimizers import SGD,Adam,RMSprop
import matplotlib.pyplot as plt

IMG_CHANNEL=3
IMG_ROW=32
IMG_COLS=32

BATCH_SIZE=128
NB_EPOCH=20
NB_CLASSES=10
VERBOSE=1
VALIDATION_SPLIT=0.2
OPTIM=RMSprop()
(x_train,y_train),(x_test,y_test)=cifar10.load_data()
print('X_train shape ',x_train.shape)
print(x_train.shape[0],'x_train sample')
print(x_test.shape[0],'x_test sample')

y_train=np_utils.to_categorical(y_train,NB_CLASSES)
y_test=np_utils.to_categorical(y_test,NB_CLASSES)

x_train=x_train.astype('float32')
x_test=x_test.astype('float32')
x_train/=255
x_test/=255

model=Sequential()
model.add(Conv2D(32,(3,2),padding='same',input_shape=(IMG_ROW,IMG_COLS,IMG_CHANNEL)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(NB_CLASSES))
model.add(Activation('softmax'))
model.summary()

model.compile(loss="categorical_crossentropy",optimizer=OPTIM,metrics=['accuracy'])
model.fit(x_train,y_train,batch_size=BATCH_SIZE,epochs=NB_EPOCH,verbose=VERBOSE,validation_split=VALIDATION_SPLIT)
score=model.evaluate(x_test,y_test,batch_size=BATCH_SIZE,verbose=VERBOSE)

print("test score :",score[0])
print("test accuracy :",score[1])
model.summary()

import imageio.imread
import scipy.misc
image_name=['cats.jpg','dog.jpg']
import numpy as np
img=imageio.imread('cat-dog2.jpg')
img=scipy.misc.imresize(img,(32,32))
model.predict_classes(img.reshape(1,32,32,3))
model.predict_proba(img.reshape(1,32,32,3))









