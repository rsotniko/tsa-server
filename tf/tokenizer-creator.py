import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np

# for reproducibility
from numpy.random import seed
from tensorflow import set_random_seed
import pickle

random_seed = 1
seed(random_seed)
random_seed += 1
set_random_seed(random_seed)
random_seed += 1

from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, Activation, Embedding, Dropout, SpatialDropout1D
from keras.layers import LSTM, Conv1D, MaxPooling1D
from sklearn.model_selection import train_test_split

print('reading CSV')

csv = pd.read_csv('../input/training.1600000.processed.noemoticon.csv', encoding = "ISO-8859-1", header=None)

print('parsing CSV')

X, Y = [], []

for index, row in csv.iterrows():
    X.append(row[5])
    y_part = row[0]
    if y_part == 0:
        yy = np.array([0])
    elif y_part == 4:
        yy = np.array([1])
    else:
        raise Exception('Invalid y_part value=' + y_part)
    Y.append(yy)

print('build words map')

max_features = 50000
tokenizer = Tokenizer(num_words=max_features)
tokenizer.fit_on_texts(X)
with open('../tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
