__author__ = 'dancecommander'

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import cPickle
import gzip


#load the dataset
f = gzip.open('/Users/dancecommander/Programming/PyCharm Projects/Training Set/mnist.pkl.gz','rb')

train_set, valid_set, test_set = cPickle.load(f)
t = train_set[0]
im = t[0]
images = np.resize(im, (28, 28))
for i in range(1, 20, 1):
    im = t[i]
    im = np.resize(im, (28, 28))
    temp = np.append(images, im, 0)
    images = temp


plt.imshow(images)
plt.gray()
plt.show()




f.close()


