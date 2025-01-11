TensorFlow is a library to train deep learning models and Keras is higher level abstraction on the top of TensorFlow. Keras used to be separate library but from tensorflow 2+ version, keras became part of the tensorflow library. The libraries can be installed using pip install tensorflow (for CPU and GPU). However, additional setup is required to integrate TensorFlow with GPU.

Neural networks expect an image of a certain size, therefore, we need to provide the image size in target_size parameter of the load_img function.
Each image consists of pixel and each of these pixels has the shape of 3 dimensions (height, width, color channels)

A typical color image consists of three color channels: red, green and blue (RGB). Each color channel has 8 bits or 1 byte and can represent distinct values between 0-256 (uint8 type).

***USE PRE-TRAINED MODEL*** 
Pre-trained model is a model that has been trained before. In keras, there are image recognition models that have been trained on many images. 