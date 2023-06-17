import numpy as np
import os

from tflite_model_maker.config import ExportFormat
from tflite_model_maker import model_spec
from tflite_model_maker import object_detector

import tensorflow as tf
assert tf.__version__.startswith('2')

tf.get_logger().setLevel('ERROR')
from absl import logging
logging.set_verbosity(logging.ERROR)

use_custom_dataset = True

dataset_is_split = True 

if use_custom_dataset:

  # The ZIP file you uploaded:
  # Your labels map as a dictionary (zero is reserved):
  label_map = {1:'waste'} 
  #||CHANGELABELMAPACCORDING||
  if dataset_is_split:
    # If your dataset is already split, specify each path:
    train_images_dir = 'train'
    train_annotations_dir = 'train'
    val_images_dir = 'valid'
    val_annotations_dir = 'valid'
    test_images_dir = 'test'
    test_annotations_dir = 'test'
#   else:
#     # If it's NOT split yet, specify the path to all images and annotations
#     images_in = 'dataset/images'
#     annotations_in = 'dataset/annotations'

if use_custom_dataset:
  if dataset_is_split:
    train_data = object_detector.DataLoader.from_pascal_voc(
        train_images_dir, train_annotations_dir, label_map=label_map)
    validation_data = object_detector.DataLoader.from_pascal_voc(
        val_images_dir, val_annotations_dir, label_map=label_map)
    test_data = object_detector.DataLoader.from_pascal_voc(
        test_images_dir, test_annotations_dir, label_map=label_map)
    

    
  print(f'train count: {len(train_data)}')
  print(f'validation count: {len(validation_data)}')
  print(f'test count: {len(test_data)}')


spec = object_detector.EfficientDetLite0Spec()

model = object_detector.create(train_data=train_data, 
                               model_spec=spec, 
                               validation_data=validation_data, 
                               epochs=5, 
                               batch_size=10, 
                               train_whole_model=True)

model.evaluate(test_data)


#TFLITE_FILENAME = 'efficientdet-lite-salad.tflite'
#LABELS_FILENAME = 'salad-labels.txt'

TFLITE_FILENAME = 'GarbageModel.tflite'
LABELS_FILENAME = 'Garbagelabels.txt'

model.export(export_dir='.', tflite_filename=TFLITE_FILENAME, label_filename=LABELS_FILENAME,
             export_format=[ExportFormat.TFLITE, ExportFormat.LABEL])

model.evaluate_tflite(TFLITE_FILENAME, test_data)


files.download(TFLITE_FILENAME)
files.download(LABELS_FILENAME)