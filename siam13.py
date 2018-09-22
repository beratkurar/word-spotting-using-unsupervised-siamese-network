from __future__ import absolute_import
from __future__ import print_function

# -*- coding: utf-8 -*-
import numpy as np
import random
from keras.layers import Input, Flatten, Dense, Dropout, Lambda, merge,Activation,BatchNormalization
from keras.callbacks import ModelCheckpoint, EarlyStopping,CSVLogger
from keras.optimizers import Adam,SGD,RMSprop
import os
from keras.models import Model, load_model, Sequential
from keras.layers.merge import concatenate
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from sklearn.metrics import accuracy_score as accuracy
import h5py
from keras.regularizers import l2
from random import shuffle

os.environ["CUDA_VISIBLE_DEVICES"]="1"
input_shape=(75,105,1)  
train_set='train'
validation_set='validations'
version='3'
learning_rate=0.00001
epochs=200
batch_size=16

continue_from_best=False
continue_from_version='0'

def get_data(set_ref):
    f1 = h5py.File("fold1.hdf5", "r")
    fold1 = {'train': list(zip(f1['train_left_images'], f1['train_right_images'], f1['train_labels'])),
         'test': list(zip(f1['test_left_images'], f1['test_right_images'], f1['test_labels'])),
         'validations': list(zip(f1['validation_left_images'], f1['validation_right_images'], f1['validation_labels']))}
    left=[]
    right=[]
    labels=[]
    for i in range(len(fold1[set_ref])):
        left.append(fold1[set_ref][i][0])
        right.append(fold1[set_ref][i][1])
        labels.append(fold1[set_ref][i][2])
    return np.array(left), np.array(right), labels

def create_data_pairs(left,right,labels):
    np.random.seed(6)
    random.seed(6)
    left = left.reshape(left.shape[0],left.shape[1],left.shape[2],1)
    right = right.reshape(right.shape[0],right.shape[1],right.shape[2],1)
    left = left.astype('float32')
    right = right.astype('float32')
    left /= 255.
    right /= 255.
    input_size = left.shape[0] 
    pairs = []
    plabels = []
    for i in range(input_size):
        pairs.append([left[i],right[i]])
        if(labels[i]==1):
            plabels.append(1)
        else:
            plabels.append(0)
    pairs=np.array(pairs)
    plabels=np.array(plabels)
    ind = [i for i in range(plabels.shape[0])]
    shuffle(ind)
    pairs =pairs[ind,:,:,:,:]
    plabels = plabels[ind,]
    return pairs,plabels


def create_base_network(input_dim):
    inputs = Input(shape=input_dim)
    conv_1=Conv2D(64,(5,5),padding="same",activation='relu',name='conv_1')(inputs)

    conv_1=MaxPooling2D(pool_size=(2, 2))(conv_1)
    conv_2=Conv2D(128,(5,5),padding="same",activation='relu',name='conv_2')(conv_1)
    conv_2=MaxPooling2D(pool_size=(2, 2))(conv_2)
    conv_3=Conv2D(256,(3,3),padding="same",activation='relu',name='conv_3')(conv_2)
    conv_3=MaxPooling2D(pool_size=(2, 2))(conv_3)
    conv_4=Conv2D(512,(3,3),padding="same",activation='relu',name='conv_4')(conv_3)
    conv_5=Conv2D(512,(3,3),padding="same",activation='relu',name='conv_5')(conv_4)
    dense_1=MaxPooling2D(pool_size=(2, 2))(conv_5)

    dense_1=Flatten()(dense_1)
    dense_1=Dense(4096,activation="relu")(dense_1)
    #dense_2=Dropout(0.2)(dense_1)
    dense_2=Dense(4096,activation="relu")(dense_1)
    #dense_3=Dropout(0.2)(dense_2)
    return Model(inputs, dense_2)



tr_left, tr_right, tr_labels = get_data(train_set)
tr_pairs,tr_y=create_data_pairs(tr_left,tr_right,tr_labels)

te_left, te_right, te_labels = get_data(validation_set)
te_pairs,te_y=create_data_pairs(te_left,te_right,te_labels)

if (continue_from_best):
    model=load_model('bestmodel'+continue_from_version)
else:
    base_network = create_base_network(input_shape)
    input_a = Input(shape=input_shape)
    input_b = Input(shape=input_shape)
    processed_a = base_network(input_a)
    processed_b = base_network(input_b)
    fc6=concatenate([processed_a, processed_b])
    fc7=Dense(4096, activation = 'relu')(fc6)
    fc8=Dense(4096, activation = 'relu')(fc7)
    fc9=Dense(1, activation='sigmoid')(fc8)
    model = Model([input_a, input_b], fc9)
    model.summary()
mcp = ModelCheckpoint('bestmodel'+version, monitor='val_acc', verbose=1, save_best_only=True,mode='max')
logs = CSVLogger('log'+version)

adam=Adam(lr=learning_rate)
#sgd = SGD(lr=learning_rate)
#rms = RMSprop(lr=learning_rate)

model.compile(loss='binary_crossentropy', optimizer=adam, metrics=['accuracy'])
model.fit([tr_pairs[:, 0], tr_pairs[:, 1]], tr_y,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=([te_pairs[:, 0], te_pairs[:, 1]], te_y),
          callbacks=[mcp,logs])

del model
model=load_model('bestmodel'+version)

#y_pred = model.predict([tr_pairs[:, 0], tr_pairs[:, 1]])
#tr_acc = accuracy(tr_y, y_pred.round())
y_pred = model.predict([te_pairs[:, 0], te_pairs[:, 1]])
te_acc = accuracy(te_y, y_pred.round())
#print('* Accuracy on training set: %0.4f%%' % (100 * tr_acc))
print('* Accuracy on test set: %0.4f%%' % (100 * te_acc))