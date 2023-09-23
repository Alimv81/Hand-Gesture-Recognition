# Hand Gesture Recognition CNN Model

## Overview

This project is a Convolutional Neural Network (CNN) model built using the TensorFlow library for the purpose of hand gesture recognition. The model is trained to distinguish between 10 different hand shapes or states. Hand gesture recognition has applications in various fields, including sign language interpretation, human-computer interaction, and virtual reality.

## Dataset

The dataset used for training and testing the CNN model can be obtained from [https://www.kaggle.com/datasets/gti-upm/leapgestrecog]. The dataset consists of images of hand gestures, each labeled with one of the 10 different hand states.

### Model Directory Structure

- To use this project and the trained model, only make sure to organize your direcory in such a way that best_model.h5 and main.py have the same path.
- To train the model the code will automatically download the essential datasets, running it would be enough

## Dependencies

Before running the code, ensure you have the following dependencies installed:

- TensorFlow
- NumPy
- sklearn
- opencv-python
- Matplotlib (for visualization)

You can install these dependencies using pip, others maybe optional to use

## Usage

the code that train the model is put in the project is HandGestureRecognitionTrainingModel.ipynb
for using the model and not training it run the man.python, it will use the systems webcam to predict the hand gesture in the image

1. download and extract the model
2. open projects directory
3. run main.py


## Model Architecture

- The CNN model architecture used for this project consists of 3 of 2 Conv2D layers stacked over each other with increasing number of filters (64 to 256) and filters shape
- connected to a Dense layer with 256 units and after that a Dense layer with 10 (number of prediction classes) with softmax activation to predict the possibility of existance of each class 


## Results

- achieved the accuracy score of 0.9974 for the train dataset
- achieved the accuracy score of 0.9990 for the validation dataset
- achieved the accuracy score of 1.0 for the test dataset

## Contact Information

If you have any questions or suggestions, feel free to contact the project maintainer:

- [Ali Mohammdi Variani]
- [amv.ai.wizard@gmail.com]
