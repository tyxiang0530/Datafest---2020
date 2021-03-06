'''
FREE GOURDS
TAI XIANG
GUY THAMPAKKUL
SAM MILLETTE
build_model trains the most optimal model output by optimize_lstm and saves it for later use
'''

from keras import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout
from keras.preprocessing import sequence
from keras import backend as K
import pickle
import tensorflow as tf
from keras.callbacks import TensorBoard

# Load in dataset
X_train = pickle.load(open("50k_train.pickle", "rb"))
y_train = pickle.load(open("50k_label.pickle", "rb"))
labels_test = pickle.load(open("new_gen_label.pickle", "rb"))
test = pickle.load(open("new_gen_test.pickle", "rb"))
print(len(X_train),len(y_train),len(labels_test),len(test))

# Define model
vocab_content = 61409
embedding_size = 128
model = Sequential()
model.add(Embedding(vocab_content, embedding_size, input_length=500))
model.add(LSTM(32))
model.add(Dense(32, activation = 'sigmoid'))
model.add(Dense(1, activation = 'sigmoid'))
print(model.summary())

model.compile(loss = 'binary_crossentropy',
              optimizer = 'adam',
              metrics = ['accuracy'])

batch_size = 64
num_epochs = 3

# Run model
X_valid, y_valid = X_train[:1000], y_train[:1000]
X_train2, y_train2 = X_train[1000:], y_train[1000:]

model.fit(X_train2, y_train2, validation_data=(X_valid, y_valid),
          batch_size=batch_size, epochs=num_epochs)
          
# save the model
model.save('youtube_runner.h5')
