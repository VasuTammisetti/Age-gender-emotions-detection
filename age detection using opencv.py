# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:37:23 2023

@author: tammisetti
"""

import tensorflow as tf
import keras
from keras.models import load_model

emotion_model = load_model('emotion_detection_model_100epochs.h5', compile=False)
gender_model = load_model('gender_model_50epochs.h5', compile=False)
age_model = load_model('age_model_50epochs.h5', compile=False)

converter = tf.lite.TFLiteConverter.from_keras_model(emotion_model)
#converter.optimizations = [tf.lite.Optimize.DEFAULT] #Uses default optimization strategy to reduce the model size
tflite_model = converter.convert()
open("emotion_detection_model_100epochs_no_opt.tflite", "wb").write(tflite_model)


converter = tf.lite.TFLiteConverter.from_keras_model(gender_model)
#converter.optimizations = [tf.lite.Optimize.DEFAULT] #Uses default optimization strategy to reduce the model size
tflite_model = converter.convert()
open("gender_detection_model_50epochs_no_opt.tflite", "wb").write(tflite_model)


converter = tf.lite.TFLiteConverter.from_keras_model(age_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT] #Uses default optimization strategy to reduce the model size
tflite_model = converter.convert()
open("age_detection_model_50epochs_opt.tflite", "wb").write(tflite_model)