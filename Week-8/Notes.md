TensorFlow is a library to train deep learning models and Keras is higher level abstraction on the top of TensorFlow. Keras used to be separate library but from tensorflow 2+ version, keras became part of the tensorflow library. The libraries can be installed using pip install tensorflow (for CPU and GPU). However, additional setup is required to integrate TensorFlow with GPU.

Neural networks expect an image of a certain size, therefore, we need to provide the image size in target_size parameter of the load_img function.
Each image consists of pixel and each of these pixels has the shape of 3 dimensions (height, width, color channels)

A typical color image consists of three color channels: red, green and blue (RGB). Each color channel has 8 bits or 1 byte and can represent distinct values between 0-256 (uint8 type).

## USE PRE-TRAINED MODEL
Pre-trained model is a model that has been trained before. In keras, there are image recognition models that have been trained on many images. 

## CONVUTIONAL NEURAL NETWORK
A convolutional neural network, also know as CNN or ConvNet, is a feed-forward neural network that is generally used to analyze visual images by processing data with grid-like topology

The convoluion operation forms the basis of any CNN. In a convolution operation, the arrays are multiplied element-wise, and the dot product is summed to create a new array, which represents Wx.

Layers in a Convolutional Neural Network
A Convolution neural network has multiple hidden layers that help in extracting information from an image. The four important layers in CNN are:
- Convolution layer
- ReLU layer
- Pooling layer
- Fully connected layer (also called Dense layer)

1. Convolution layer

This is the first step in the process of extracting valuable features from an image. A convolution layer has several filters that perform the convolution operation. Every image is considered as a matrix of pixel values.

2. ReLU layer

Once the feature maps are extracted, the next step is to move them to a ReLU layer. ReLU (Rectified Linear Unit) is an activation function which performs an element-wise operation and sets all the negative pixels to 0. It introduces non-linearity to the network, and the generated output is a rectified feature map. The relu function is: f(x) = max(0,x).

3. Pooling layer

Pooling is a down-sampling operation that reduces the dimensionality of the feature map. The rectified feature map goes through a pooling layer to generate a pooled feature map. The pooling layer uses various filters to identify different parts of the image like edges, shapes etc.

4. Fully Connected layer

The next step in the process is called flattening. Flattening is used to convert all the resultant 2D arrays from pooled feature maps into a single linear vector. This flattened vector is then fed as input to the fully connected layer to classify the image.

## Transfer Learning
Transfer learning is a machine learning method where a model developed for a task is reused as the starting point for a model on a second task. Usually a pretrained model is trained with large volume of images and that is why the convolutional layers and vector representation of this model can be used for other tasks as well.

## Adjusting Learning Rate
One of the most important hyperparameters of deep learning models is the learning rate. It is a tuning parameter in an optimization function that determines the step size (how big or small) at each iteration while moving toward a mininum of a loss function.

The goal is to find the right reading pace, or learning rate, that balances comprehension and efficiency. Reading too fast may result in superficial understanding, while reading too slowly might mean not acquiring knowledge quickly enough to meet your goals. By maintaining a moderate, balanced pace, you can maximize understanding and effectively apply what you've learned.

A balanced learning rate ensures the model acquires sufficient knowledge and performs well on both training and validation data.

## Checkpointing Model
ModelCheckpoint (function on keras) callback is used with training the model to save a model or weights in a checkpoint file at some interval, so the model or weights can be loaded later 

## Adding Layers 
It is also possible to add one or more layers between the vector representation layer and the output layer to perform intermediate processing of the vector representation.
These layer(s) are the same dense layers as the output but the difference is that these layers use relu activation 

Note: It may not always be possible that the model improves

## Dropout and Regularization
Methods for deep learning to prevent overfitting by randomly dropping nodes of a layer during training. 
Note: Because we introduce dropout in the neural networks, we will need to train our model for longer, hence, number of epochs is set to 30.

## Data Augmentation
Data augmentation is a process of artifically increasing the amount of data by generating new images from existing images. This includes adding minor alterations to images by flipping, cropping, adding brightness and/or contrast, and many more.

In Keras, you can use ImageDataGenerator function.