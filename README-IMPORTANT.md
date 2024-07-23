This File is Emotion classifier 

It works on Deep neural Networks using Conv2D and best fit activation functions

we start by checking the good image extension. if image extension is not in specified bounds we will remove it using os.remove()

using a best data pipeline from keras helps us to pre convert data into array of numbers
use : keras.utils.image_dataset_from_directory("your data directory here")

and using .map funtion with the loaded dataset helps to assign it function to every element of it 

use data = data.map(lambda x,y: (x/255, y))

lambda : It is a minimal python fucntion aims to establish given operation

by here we resize the images by dividing with 255
reason : the pixels extend from 0 - 255 black having 0 , white having 255 ::: we aim to bring everything between 0 and 1

and specifing a batch with numpy iterator helps to visualise data such that we can know which label is encoded with which class ::: In this model angry class was assinged 0 and happy class was assigned 1

and using matplotlib.pyplot to plot images

then finally scalling the data into train, test, validation set using tensorflow .take(), .skip() methods

and creating a neural network with keras.models.Sequential() and keras.layers constructs the Deep Learning Network

other two blocks aims to plot performance of validation_loss and training_loss and accuracy

Since the output is between 0 and 1 we can use sigmoid function which classifies the data into angry / happy

and Your testing is all the way
